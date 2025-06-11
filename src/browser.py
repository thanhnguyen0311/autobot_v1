from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def create_browser():
    """Set up and return a Selenium WebDriver instance."""
    # Configure browser options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start browser maximized
    chrome_options.add_argument("--disable-infobars")  # Disable infobars
    chrome_options.add_argument("--disable-extensions")  # Disable extensions
    chrome_options.add_argument("--headless")  # Run in headless mode (optional, for testing/scripted runs)

    # Set up WebDriver using WebDriver Manager
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=chrome_options)

    return browser


def close_browser(browser):
    """Gracefully close the browser."""
    if browser:
        browser.quit()