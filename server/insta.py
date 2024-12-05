from selenium import webdriver
from selenium.webdriver.common.by import By

class Instagram:
    def __init__(self):
        selenium_url = "http://localhost:4444/wd/hub"
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")  # Disable the sandbox (Docker-specific)
        options.add_argument("--disable-dev-shm-usage")  # Address resource issues
        options.set_capability('se:name', 'instagram (ChromeTests)')
        # options.set_capability('se:recordVideo', False) #disable video recording
        # options.set_capability(capabilities)
        self.driver = webdriver.Remote(command_executor=selenium_url, options=options)

    def register(self):
        self.driver.get("https://www.instagram.com/accounts/emailsignup/")
        title = self.driver.title
        email_input = self.driver.find_element(By.XPATH, "") 
        password_input = self.driver.find_element(By.XPATH, "")
        fullname_input = self.driver.find_element(By.XPATH, "")
        username_input = self.driver.find_element(By.XPATH, "")
        print(title)

    def login(self):
        pass

    def send_message(self):
        pass

    def follow_account(self):
        pass