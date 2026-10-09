from typing import TYPE_CHECKING

from selenium import webdriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    StaleElementReferenceException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from path_vars import DRIVER_PATH

if TYPE_CHECKING:
    from selenium.webdriver.remote.webdriver import WebDriver


class WebScraper:
    def __init__(self, url: str, time_to_wait: int, options: list[str]) -> None:
        self.time_to_wait = time_to_wait
        self.url = url
        self.options = options
        self.browser = self.make_firefox_browser()
        self.browser.get(url)

    def make_firefox_browser(self) -> WebDriver:
        firefox_options = webdriver.FirefoxOptions()

        for option in self.options:
            firefox_options.add_argument(option)

        firefox_service: Service = Service(
            executable_path=str(DRIVER_PATH),
        )

        return webdriver.Firefox(
            service=firefox_service,
            options=firefox_options,
        )

    def fill_input(self, field_id: tuple[str, str], input_text: str) -> None:
        try:
            WebDriverWait(self.browser, self.time_to_wait).until(
                ec.element_to_be_clickable(field_id),
            ).send_keys(input_text)
        except StaleElementReferenceException:
            self.fill_input(field_id, input_text)

    def clear_input(self, field_id: tuple[str, str]) -> None:
        try:
            WebDriverWait(self.browser, self.time_to_wait).until(
                ec.element_to_be_clickable(field_id),
            ).clear()
        except StaleElementReferenceException:
            self.clear_input(field_id)

    def click_element(self, btn_id: tuple[str, str]) -> None:
        try:
            WebDriverWait(self.browser, self.time_to_wait).until(
                ec.element_to_be_clickable(btn_id),
            ).click()
        except StaleElementReferenceException:
            self.click_element(btn_id)
        except ElementClickInterceptedException:
            if self.not_found():
                self.click_element(btn_id)

    def switch_to_inner_frame(self, frames: list[tuple[str, str]]) -> None:
        for frame in frames:
            table_iframe = self.browser.find_element(*frame)
            self.browser.switch_to.frame(table_iframe)

    def not_found(self) -> None:
        try:
            WebDriverWait(self.browser, 2).until(
                ec.element_to_be_clickable((By.XPATH, '//*[@id="pt1:d8_ok"]/a')),
            ).click()
        except ElementClickInterceptedException:
            self.not_found()
        except (
            TimeoutException,
            StaleElementReferenceException,
            ElementNotInteractableException,
        ):
            print("Not found!")
