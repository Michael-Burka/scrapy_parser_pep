import csv
import logging
import os
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import (BASE_DIR, FILENAME_DATETIME_FORMAT,
                                OUTPUT_RESULTS_DIR)


class PepParsePipeline:
    """Pipeline for parsing PEP data and writing results to a CSV file."""

    def __init__(self):
        """Initialize the pipeline and ensure the results directory exists."""
        self.output_results_dir = os.path.join(BASE_DIR, OUTPUT_RESULTS_DIR)
        os.makedirs(self.output_results_dir, exist_ok=True)
        logging.info(f"Results directory: {self.output_results_dir}")

    def open_spider(self, spider):
        """Initialize the counter for PEP statuses when the spider is opened.

        Args:
            spider (scrapy.Spider): The spider instance that is being opened.
        """
        self.status_counter = defaultdict(int)
        logging.info("Spider opened: %s", spider.name)

    def process_item(self, item, spider):
        """Process each item and count the occurrences of each status.

        Args:
            item (dict): The item scraped from the spider.
            spider (scrapy.Spider): The spider instance that scraped the item.

        Returns:
            dict: The processed item.
        """
        self.status_counter[item["status"]] += 1
        return item

    def close_spider(self, spider):
        """Write the summary of PEP statuses to a CSV file.

        Args:
            spider (scrapy.Spider): The spider instance that is being closed.
        """
        timestamp = dt.now().strftime(FILENAME_DATETIME_FORMAT)
        file_path = os.path.join(
            self.output_results_dir, f"status_summary_{timestamp}.csv")

        self.status_counter["Total"] = sum(self.status_counter.values())

        try:
            with open(file_path, "w", encoding="utf-8") as file:
                writer = csv.writer(
                    file, dialect=csv.unix_dialect(), quoting=csv.QUOTE_MINIMAL
                )
                writer.writerow(["Status", "Count"])
                for status, count in self.status_counter.items():
                    writer.writerow([status, count])

            logging.info(f"Status summary written to {file_path}")
        except IOError as e:
            spider.logger.error(f"Error writing CSV file: {e}")
            logging.error(f"Error writing CSV file to {file_path}: {e}")

        logging.info(f"Spider closed: {spider.name}")
