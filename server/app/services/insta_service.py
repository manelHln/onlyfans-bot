from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from config.logger import APP_LOG_CONFIG
from utils import utils

import logging.config
import logging


class Instagram:
    def __init__(self):
        logging.config.dictConfig(APP_LOG_CONFIG)
        self.logger = logging.getLogger('selenium')
        self.selenium_url = "http://selenium-hub:4444/wd/hub"
        self.chrome_options = webdriver.ChromeOptions()
        # Disable the sandbox (Docker-specific)
        self.chrome_options.add_argument("--no-sandbox")
        # Address resource issues
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.set_capability('se:name', 'instagram (ChromeTests)')
        # self.chrome_options.set_capability('se:recordVideo', False) #disable video recording
        # self.chrome_options.set_capability(capabilities)

    def register(self):
        try:
            driver = webdriver.Remote(command_executor=self.selenium_url,options=self.chrome_options)
            self.logger.debug("Navigating to instagram")
            driver.get("https://www.instagram.com/accounts/emailsignup/")
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "emailOrPhone")))

            driver.find_element(By.NAME, "emailOrPhone").send_keys(
                "udwhpghcdx@dygovil.com")
            driver.find_element(
                By.NAME, "fullName").send_keys("Emma Enders")
            driver.find_element(
                By.NAME, "username").send_keys("iamemma453")
            driver.find_element(By.NAME, "password").send_keys(
                "T5ui#jdh8_@=+tgzfvsbf")
            self.logger.debug("Send keys terminated")
            driver.find_element(
                By.XPATH, "//button[@type='submit']").click()
            self.logger.debug("submit button click")

            self.logger.debug("Waiting for the next page to load")
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body")))

            birthdate_dict = utils.get_birthdate()

            birth_month = Select(driver.find_element(
                By.XPATH, "//select[@title='Month:']"))
            birth_month.select_by_value(birthdate_dict.get(
                "month").zfill(2))  # Ensure two-digit month

            birth_day = Select(driver.find_element(
                By.XPATH, "//select[@title='Day:']"))
            birth_day.select_by_value(birthdate_dict.get("day"))

            birth_year = Select(driver.find_element(
                By.XPATH, "//select[@title='Year:']"))
            birth_year.select_by_value(
                birthdate_dict.get("year"))  # Year as string

            title = driver.title

            self.logger.debug(f"This is the title of the new page {title}")
            driver.close()
            return title
        except TimeoutException:
            self.logger.debug(
                "Timeout while waiting for the page to load or elements to appear")
        except NoSuchElementException as e:
            self.logger.debug(f"Element not found: {e}")
        except Exception as e:
            self.logger.debug(f"An error occurred: {e}")

    def login(self):
        pass

    def send_message(self):
        pass

    def follow_account(self):
        pass
    
    def get_user_followers(self):
        pass 
