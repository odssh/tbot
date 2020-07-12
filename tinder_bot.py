from selenium import webdriver
from time import sleep
import random
from secrets import username, password

class TinderBot():
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument("--headless")
        option.add_argument("--window-size=1920,1080")
        option.add_argument("--disable-gpu")
        option.add_argument("log-level=3")
        option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
        # option.add_argument('--disable-dev-shm-usage')
        # option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
        # option.add_experimental_option('excludeSwitches', ['enable-automation'])
        # option.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=option)

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(2)
        try:
            self.driver.find_element_by_xpath('//span[contains(text(), "I Accept")]').click()
        except:
            pass
        try:
            self.driver.find_element_by_xpath('//button[contains(text(), "More Options")]').click()
        except:
            pass
        sleep(5)
        print("click to fb login")
        self.driver.find_element_by_xpath('//span[contains(text(), "Log in with Facebook")]').click()
        print("done fb login click")
        sleep(5)

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to.window(base_window)
        sleep(5)

        # popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        # popup_1.click()

        # popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        # popup_2.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//button[@aria-label="Like"]').click()
        # like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        #like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            count = 0
            randomDelay = random.randrange(1,2)
            sleep(randomDelay)
            try:
                try:
                    self.like()
                except Exception:
                    try:
                        self.close_popup()
                    except Exception:
                        self.close_match()
                count +=1
                print(count)
            except:
                sleep(5)
                # self.driver.refresh()
                # sleep(5)


    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()
bot.auto_swipe()
