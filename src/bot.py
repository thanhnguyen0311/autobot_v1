from src.browser import create_browser, close_browser
from src.actions import perform_actions


def run_bot(url):
    """
    The main function to execute the bot's logic.
    :param url: The URL to navigate to.
    """
    browser = None
    try:
        # Initialize the browser
        print("[INFO] Launching browser...")
        browser = create_browser()

        # Navigate to the target URL
        print(f"[INFO] Navigating to: {url}")
        browser.get(url)

        # Perform specific actions on the page
        print("[INFO] Performing actions...")
        perform_actions(browser)

        print("[INFO] Bot completed successfully.")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
    finally:
        # Close the browser in the end
        print("[INFO] Closing the browser...")
        close_browser(browser)