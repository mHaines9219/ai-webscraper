# AI Web Scraper

The **AI Web Scraper** is a powerful tool designed to scrape and parse information from web pages, even those protected by CAPTCHAs. It utilizes Bright Data and Selenium for web scraping and BeautifulSoup for parsing HTML content. Additionally, it leverages the `langchain` framework to process and extract specific information from the scraped content using a language model (LLM).

## Features

- **Web Scraping with CAPTCHA Bypass**: Automatically handles CAPTCHA challenges using Bright Data's Scraping Browser and Selenium.
- **HTML Content Extraction**: Parses and extracts specific parts of the web page, such as the `<body>` content, using BeautifulSoup.
- **Content Cleaning**: Cleans the extracted content by removing unnecessary scripts, styles, and whitespace.
- **Custom Information Parsing**: Uses LLM (`llama3` model) to extract specific information from the cleaned content based on user-provided descriptions.
- **Streamlit Integration**: Provides a user-friendly web interface for scraping and parsing web pages interactively.

## Installation

1. **Clone this repository:**

    ```bash
    git clone https://github.com/mHaines9219/ai-web-scraper.git
    cd ai-web-scraper
    ```

2. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Bright Data and Selenium:**

    Ensure you have the necessary credentials for Bright Data's Scraping Browser and have set up your Selenium environment correctly.

## Usage

1. **Run the Streamlit App:**

    Start the Streamlit web application by running:

    ```bash
    streamlit run app.py
    ```

2. **Enter a URL:**

    Input the URL of the web page you want to scrape in the provided text input field.

3. **Scrape the Website:**

    Click the **"Scrape"** button to start the web scraping process. The app will connect to the Scraping Browser, solve any CAPTCHAs, and retrieve the page content.

4. **View and Parse Content:**

    After scraping, the content will be displayed in a text area. Describe the information you want to parse and click **"Parse Content"** to extract specific data using the LLM (`llama3`).

## Code Overview

- **`scrape_website(website)`**: Connects to the Scraping Browser using Selenium and Bright Data, navigates to the specified website, and returns the HTML content.
- **`extract_body(html_content)`**: Extracts the `<body>` content from the HTML.
- **`clean_body(body)`**: Cleans the extracted body content by removing scripts, styles, and unnecessary whitespace.
- **`split_dom_content(dom_content, max_length)`**: Splits the cleaned content into chunks of a specified maximum length for processing.
- **`parse_with_llama3(dom_chunks, parse_description)`**: Parses the cleaned and chunked content using the `llama3` model to extract specific information based on the user-provided description.

## Dependencies

- Python 3.x
- Selenium
- BeautifulSoup4
- Streamlit
- langchain
- Bright Data Scraping Browser credentials

## Setup Notes

- **CAPTCHA Handling**: The scraper uses Bright Data's automated CAPTCHA-solving service. Ensure your account is properly configured for this functionality.
- **Selenium Setup**: Make sure you have the correct version of ChromeDriver or another WebDriver compatible with your browser.

## Known Issues
- UI is a bit ugly
- LLM runs VERY slow, to scale this project I will need to implement cloud computing to effectively handle the load

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any ideas or improvements.

## Credit Inspiration

Inspired to do the project and build off the work of Tech With Tim on youtube.

## Contact

For any questions or feedback, please reach out to [mhaines9219@gmail.com](mailto:mhaines9219@gmail.com).
