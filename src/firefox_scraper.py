from typing import TYPE_CHECKING

from rich import print
from selenium import webdriver
from selenium.common.exceptions import (
    TimeoutException,
)
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

if TYPE_CHECKING:
    from pathlib import Path

    from selenium.webdriver.remote.webdriver import WebDriver


class WebScraper:
    def __init__(
        self,
        driver_path: str | Path,
        url: str,
        time_to_wait: int,
        options: list[str],
    ) -> None:
        self.time_to_wait = time_to_wait
        self.driver_path = str(driver_path)
        self.url = url
        self.options = options
        self.browser = self.make_firefox_browser()
        self.browser.get(url)

    def make_firefox_browser(self) -> WebDriver:
        firefox_options = webdriver.FirefoxOptions()

        for option in self.options:
            firefox_options.add_argument(option)

        firefox_service: Service = Service(
            executable_path=self.driver_path,
        )

        return webdriver.Firefox(
            service=firefox_service,
            options=firefox_options,
        )

    def fill_input(self, field_id: tuple[str, str], input_text: str) -> None:
        try:
            WebDriverWait(
                self.browser,
                self.time_to_wait,
            ).until(
                ec.element_to_be_clickable(field_id),
            ).send_keys(input_text)
        except TimeoutException:
            print(f"Input not found or not clickable: {field_id}")
            self.browser.refresh()

    def clear_input(self, field_id: tuple[str, str]) -> None:
        try:
            WebDriverWait(
                self.browser,
                self.time_to_wait,
            ).until(
                ec.element_to_be_clickable(field_id),
            ).clear()
        except TimeoutException:
            print(f"Input not found or not clickable: {field_id}")
            self.browser.refresh()

    def click(self, element_id: tuple[str, str]) -> None:
        try:
            WebDriverWait(
                self.browser,
                self.time_to_wait,
            ).until(
                ec.element_to_be_clickable(element_id),
            ).click()
        except TimeoutException:
            print(f"Element not found or not clickable: {element_id}")
            self.browser.refresh()

    def get_link(self, element_id: tuple[str, str]) -> str:
        element = WebDriverWait(
            self.browser,
            self.time_to_wait,
        ).until(
            ec.presence_of_element_located(element_id),
        )
        return element.get_attribute("href") or ""

    def switch_to_inner_frame(self, frames: list[tuple[str, str]]) -> None:
        for frame in frames:
            table_iframe = self.browser.find_element(*frame)
            self.browser.switch_to.frame(table_iframe)
