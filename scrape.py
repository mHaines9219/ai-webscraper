from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from bs4 import BeautifulSoup

SBR_WEBDRIVER = "https://brd-customer-hl_5474feb0-zone-scraping_browser1-country-us:jz7h7fdenb9e@brd.superproxy.io:9515"


def scrape_website(website):
    print("Connecting to Scraping Browser...")

    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print("Connected! Navigating to " + website)
        driver.get(website)
        # CAPTCHA handling: If you're expecting a CAPTCHA on the target page, use the following code snippet to check the status of Scraping Browser's automatic CAPTCHA solver
        print("Waiting captcha to solve...")
        solve_res = driver.execute(
            "executeCdpCommand",
            {
                "cmd": "Captcha.waitForSolve",
                "params": {"detectTimeout": 10000},
            },
        )
        print("Captcha solve status:", solve_res["value"]["status"])
        print("Navigated! Scraping page content...")
        html = driver.page_source
        return html


def extract_body(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body = soup.body
    if body:
        return str(body)
    return ""


def clean_body(body):
    soup = BeautifulSoup(body, "html.parser")
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_body = soup.get_text(separator="\n")
    cleaned_body = "\n".join(
        line.strip() for line in cleaned_body.splitlines() if line.strip()
    )

    return cleaned_body


def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]
