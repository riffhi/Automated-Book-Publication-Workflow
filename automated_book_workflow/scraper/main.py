from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import os
import uuid

OUTPUT_FOLDER = "data"


def scrape_chapter(url):
    os.makedirs(f"{OUTPUT_FOLDER}/screenshots", exist_ok=True)
    os.makedirs(f"{OUTPUT_FOLDER}/chapters", exist_ok=True)
    
    print(f"Scraping: {url}")
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(3000)

        screenshot_path = f"{OUTPUT_FOLDER}/screenshots/{uuid.uuid4()}.png"
        page.screenshot(path=screenshot_path, full_page=True)

        content = page.content()
        soup = BeautifulSoup(content, "html.parser")
        main_text = soup.find("div", {"class": "mw-parser-output"}).get_text()

        text_path = f"{OUTPUT_FOLDER}/chapters/{uuid.uuid4()}.txt"
        with open(text_path, "w", encoding="utf-8") as f:
            f.write(main_text.strip())

        browser.close()
    print(f"Saved text to: {text_path}")
    return text_path
