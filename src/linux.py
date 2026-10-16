import os
from time import sleep

from dotenv import load_dotenv

from path_vars import DOTENV_PATH, FIREFOX_DRIVER
from scrap_vars import (
    APPLY,
    DATE_POSTED,
    EMAIL_FIELD,
    JOB_SEARCH_INPUT,
    JOB_TAB_BTN,
    LOGIN_BTN,
    PASSWORD_FIELD,
    PAST_24,
    SHOW_RESULTS,
)
from scraper import FirefoxScraper

if __name__ == "__main__":
    # .env
    load_dotenv(DOTENV_PATH)
    msg_not_found = ".env variable not found! Check your .env file"
    EMAIL = os.environ.get("EMAIL", msg_not_found)
    PASSWORD = os.environ.get("PASSWORD", msg_not_found)

    # Linkedin vars
    URL = "https://www.linkedin.com/login/pt/"
    JOB = "desenvolvedor junior"

    # Web scraping variables (Selenium)
    TIME_TO_WAIT = 3  # Time limit between each interaction (Timeout)

    # webdriver setup
    options: list[str] = ["--start-maximized", "--private"]  # opens on maximized screen
    web_scraper = FirefoxScraper(
        driver_path=FIREFOX_DRIVER,
        url=URL,
        time_to_wait=TIME_TO_WAIT,
        custom_options=options,
    )

    # Login session
    # web_scraper.click(SIGNIN_BTN)  # click Next
    web_scraper.fill_input(EMAIL_FIELD, EMAIL)  # fill email
    web_scraper.fill_input(PASSWORD_FIELD, PASSWORD)  # fill pass
    web_scraper.click(LOGIN_BTN)  # click Next

    # Job search session
    web_scraper.click(JOB_TAB_BTN)
    web_scraper.fill_input(JOB_SEARCH_INPUT, JOB)  # fill email

    ## Filters
    web_scraper.click(DATE_POSTED)
    web_scraper.click(PAST_24)

    ## Show results
    web_scraper.click(SHOW_RESULTS)
    job_link = web_scraper.get_link(APPLY)

    print(job_link)

    sleep(TIME_TO_WAIT)
