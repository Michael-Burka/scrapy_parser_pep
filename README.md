# PEP Parser Project

## Overview

The PEP Parser is a specialized tool designed for scraping and analyzing Python Enhancement Proposals (PEPs) directly from the official Python website. It leverages Scrapy for efficient web scraping and handles data processing and storage using custom pipelines and settings. The tool outputs the scraped information into two CSV files: one containing the list of all PEPs and their statuses, and another providing a summary of the count of PEPs by status.

### Key Features

- **Comprehensive PEP Scraping**: Gathers all PEPs including their numbers, titles, and statuses.
- **Status Summary**: Generates a summary of PEP statuses, showing the count of documents in each status.
- **Customizable Settings**: Allows configuration of scraping parameters to suit different project requirements.
- **Data Storage**: Saves scraped data into CSV files for easy access and analysis.

### Usage Scenarios

- **Python Community Contributors**: Helps contributors monitor and analyze the status of PEPs.
- **Researchers and Analysts**: Useful for tracking the evolution and current status of Python enhancements.
- **Developers**: Provides a framework for developers to build upon for custom PEP-related scraping projects.

## Getting Started

### Installation and Usage

1. **Clone the repository**: Find the project on GitHub and clone it to your local machine.
    ```bash
    git clone <repository-url>
    ```
2. **Set up a virtual environment**: Before installing the dependencies, create a virtual environment to keep them isolated from your global Python environment.
    ```bash
    python -m venv venv
    # On Unix/macOS:
    source venv/bin/activate
    # On Windows:
    .\venv\Scripts\activate
    ```
3. **Install dependencies**: Install the required dependencies by running the following command within your virtual environment.
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the spider**: Execute the Scrapy spider with the desired options by running:
    ```bash
    scrapy crawl pep_spider
    ```

### Configuration

Update the `settings.py` file with your specific configurations for the scraping tasks. This includes settings for user-agent, download delay, item pipelines, and more to ensure efficient and polite scraping.

## Detailed Functionality

### PEP Spider (`pep_spider`)

The PEP Spider is the core component that defines how to crawl and extract data from the PEP pages. It starts from the base URL `https://peps.python.org/` and follows links to individual PEP documents. The spider extracts the PEP number, title, and status using CSS or XPath selectors.

### Items (`items.py`)

Defines the data structures for the scraped data. The `PepParseItem` class includes three attributes:
- `number`: The PEP number.
- `name`: The PEP title.
- `status`: The PEP status as listed on the page.

### Pipelines (`pipelines.py`)

The pipelines process the scraped data before storing it. They handle tasks such as saving the PEP list to a CSV file and generating a status summary. A custom pipeline sums the number of PEPs in each status and writes this summary to a separate CSV file.

### Output Files

1. **PEP List**: Saved in the `results/` directory with the filename format `pep_<datetime>.csv`. This file contains three columns: number, name, and status.
2. **Status Summary**: Also saved in the `results/` directory with the filename format `status_summary_<datetime>.csv`. This file contains two columns: "Status" and "Count", with a final row showing the total number of PEPs.

## Example Usage

To start the spider and save the output:
```bash
scrapy crawl pep_spider
```

This will generate the PEP list and status summary CSV files in the `results/` directory.

## Security Considerations

When using this parser, it is crucial to:

- Respect the `robots.txt` file and terms of service of the target websites.
- Avoid overwhelming the target servers by setting appropriate download delays and concurrent requests.
- Ensure that sensitive data is handled securely and in compliance with relevant data protection regulations.

## Contributing

Contributions are welcome! Whether you're fixing bugs, improving the documentation, or suggesting new features, your input is valuable. Please feel free to submit pull requests or open issues on the GitHub repository.

### Files Overview

1. **pep.py**: Contains the spider logic for scraping PEP data.
2. **pipelines.py**: Handles data processing and writing to CSV files.
3. **settings.py**: Configuration file for Scrapy settings.
4. **items.py**: Defines the data structure for scraped items.

By following these guidelines, you can efficiently use and contribute to the PEP Parser project.

---

## Feedback and Contact

If you have suggestions, inquiries, or just wish to discuss any aspect of this project:

- **Name**: Michael Burka 
- **Email**: [contact@michaelburka.com](mailto:contact@michaelburka.com) 
- **GitHub**: [Michael-Burka's GitHub Profile](https://github.com/Michael-Burka/) 
- **LinkedIn**: [Michael-Burka's LinkedIn Profile](https://www.linkedin.com/in/michael-burka-485832251/) 
