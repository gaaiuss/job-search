from time import sleep

from dotenv import load_dotenv

from firefox_scraper import WebScraper
from path_vars import DOTENV_PATH

if __name__ == "__main__":
    # .env
    load_dotenv(DOTENV_PATH)
    msg_not_found = ".env variable not found! Check your .env file"
    URL = ""
    # USER = os.environ.get("USER", msg_not_found)
    # PASSWORD = os.environ.get("PASSWORD", msg_not_found)

    # Web scraping variables (Selenium)
    TIME_TO_WAIT = 60  # Time limit between each interaction (Timeout)

    # webdriver setup
    options: list[str] = ["start-maximized", "incognito"]  # opens on maximized screen
    web_scraper = WebScraper(URL, TIME_TO_WAIT, options)

    # # Login session
    # web_scraper.fill_input(EMAIL_FIELD, USER)  # fill email
    # web_scraper.click_element(NEXT_BUTTON)  # click Next
    # web_scraper.fill_input(PASSWORD_FIELD, PASSWORD)  # fill pass
    # web_scraper.click_element(NEXT_BUTTON)  # click Login - same id?
    # web_scraper.click_element(NO_BUTTON)  # click No
    # web_scraper.click_element(X_BUTTON)  # click X on popup

    # # Web scraping
    # # focus on the inner HTML that contains the table used for scraping
    # web_scraper.switch_to_inner_frame([FIRST_FRAME, SECOND_FRAME])
    # # setup exact match to filter only one product at a time
    # web_scraper.click_element(EXACT_MATCH)

    sleep(TIME_TO_WAIT)
