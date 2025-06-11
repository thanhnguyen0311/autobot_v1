import pygetwindow as gw  # Dependency to interact with open windows

def focus_chrome_window():
    chrome_windows = [win for win in gw.getWindowsWithTitle("Chrome") if "Chrome" in win.title]
    if chrome_windows:
        chrome_windows[0].activate()  # Activate (focus on) the Chrome window
        return True
    return False


def close_browser(browser):
    """Gracefully close the WebDriver instance."""
    if browser:
        browser.quit()