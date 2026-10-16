from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

if TYPE_CHECKING:
    from pathlib import Path

    from selenium.webdriver.remote.webdriver import WebDriver


class Scraper(ABC):
    def __init__(
        self,
        driver_path: str | Path,
        url: str,
        time_to_wait: int,
        custom_options: list[str],
    ) -> None:
        self.time_to_wait = time_to_wait
        self.driver_path = str(driver_path)
        self.url = url
        self.custom_options = custom_options
        self.browser = self.make_browser()
        self.browser.get(url)

    @abstractmethod
    def make_browser(self) -> WebDriver: ...

    def fill_input(self, field_id: tuple[str, str], input_text: str) -> None:
        WebDriverWait(
            self.browser,
            self.time_to_wait,
        ).until(
            ec.element_to_be_clickable(field_id),
        ).send_keys(input_text)

    def clear_input(self, field_id: tuple[str, str]) -> None:
        WebDriverWait(
            self.browser,
            self.time_to_wait,
        ).until(
            ec.element_to_be_clickable(field_id),
        ).clear()

    def click(self, element_id: tuple[str, str]) -> None:
        WebDriverWait(
            self.browser,
            self.time_to_wait,
        ).until(
            ec.element_to_be_clickable(element_id),
        ).click()

    def press_enter(self, element_id: tuple[str, str]) -> None:
        WebDriverWait(
            self.browser,
            self.time_to_wait,
        ).until(
            ec.element_to_be_clickable(element_id),
        ).send_keys(Keys.ENTER)

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


class FirefoxScraper(Scraper):
    def make_browser(self) -> WebDriver:
        options = webdriver.FirefoxOptions()

        for option in self.custom_options:
            options.add_argument(option)

        service: FirefoxService = FirefoxService(
            executable_path=self.driver_path,
        )

        return webdriver.Firefox(
            service=service,
            options=options,
        )


class EdgeScraper(Scraper):
    def make_browser(self) -> WebDriver:
        options = webdriver.EdgeOptions()

        for option in self.custom_options:
            options.add_argument(option)

        service: EdgeService = EdgeService(
            executable_path=self.driver_path,
        )

        return webdriver.Edge(
            service=service,
            options=options,
        )


class ChromeScraper(Scraper):
    def make_browser(self) -> WebDriver:
        options = webdriver.ChromeOptions()

        for option in self.custom_options:
            options.add_argument(option)

        service: ChromeService = ChromeService(
            executable_path=self.driver_path,
        )

        return webdriver.Chrome(
            service=service,
            options=options,
        )
