from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

CHROME_DRIVER_PATH = "E:\Softwares\Chromedriver\chromedriver.exe"
TARGET_ACCOUNT = "433"
USERNAME = "testbazisina"
PASSWORD = "testbazisinaeshrati"


class InstaFollower:
    def __init__(self):
        self.service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        username = self.driver.find_element(By.NAME, 'username')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, 'password')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/")
        time.sleep(3)
        followings = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        followings.click()
        time.sleep(3)
        followings_list = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[3]')
        for n in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followings_list)
            time.sleep(3)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CLASS_NAME, 'y3zKF')
        for button in follow_buttons:
            button.click()
            time.sleep(1)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
