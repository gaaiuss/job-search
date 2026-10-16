import os
from time import sleep

from dotenv import load_dotenv
from rich import print
from selenium.common import TimeoutException

from path_vars import CHROME_DRIVER, DOTENV_PATH
from scrap_vars import (
    APPLY,
    DATE_POSTED,
    EMAIL_FIELD,
    JOB_ELEMENT,
    JOB_SEARCH_INPUT,
    LOGIN_BTN,
    PASSWORD_FIELD,
    PAST_24,
    SHOW_RESULTS,
)
from scraper import ChromeScraper


def main() -> None:
    # .env
    load_dotenv(DOTENV_PATH)
    msg_not_found = ".env variable not found! Check your .env file"
    email = os.environ.get("EMAIL", msg_not_found)
    password = os.environ.get("PASSWORD", msg_not_found)

    # Linkedin vars
    url = "https://www.linkedin.com/jobs"
    job = "desenvolvedor junior"
    links: list[str] = []

    # Web scraping variables (Selenium)
    time_to_wait = 10  # Time limit between each interaction (Timeout)

    # webdriver setup
    options: list[str] = [
        "--start-maximized",
        "--incognito",
    ]
    web_scraper = ChromeScraper(
        driver_path=CHROME_DRIVER,
        url=url,
        time_to_wait=time_to_wait,
        custom_options=options,
    )

    # Login session
    web_scraper.fill_input(EMAIL_FIELD, email)  # fill email
    web_scraper.fill_input(PASSWORD_FIELD, password)  # fill pass
    web_scraper.click(LOGIN_BTN)  # click sign in

    # Job search session
    try:  # captcha check
        web_scraper.fill_input(JOB_SEARCH_INPUT, job)  # fill job description
    except TimeoutException:
        web_scraper.pause_for_captcha()  # pause execution until the captcha is done
        web_scraper.fill_input(JOB_SEARCH_INPUT, job)  # tries again after the check

    web_scraper.press_enter(JOB_SEARCH_INPUT)  # fill job description

    ## Filters
    web_scraper.click(DATE_POSTED)
    web_scraper.click(PAST_24)

    ## Show results
    web_scraper.click(SHOW_RESULTS)

    # Get all jobs
    jobs = web_scraper.find_all_elements(JOB_ELEMENT)

    for job in jobs:
        sleep(1)
        web_scraper.click_web_element(job)
        links.append(web_scraper.get_link(APPLY))

    print(links)


if __name__ == "__main__":
    main()
