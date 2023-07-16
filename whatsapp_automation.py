import subprocess
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from image_generator import generate_image_with_random_color

class WhatsappAutomation:
    def __init__(self, driver):
        self.driver = driver
        self.color_generator = generate_image_with_random_color(1000, 1000, "/home/seluser/automate_whatsapp/random_color_image.png")

    def perform_key_action(driver):
        body = driver.find_element_by_tag_name("body")
        body.send_keys(Keys.DOWN)

    def change_profile_picture(self):
        self.color_generator = generate_image_with_random_color(1000, 1000, "/home/seluser/automate_whatsapp/random_color_image.png")
        # Open profile settings
        profile_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//span[@data-icon='menu']")))
        time.sleep(2)
        profile_button.click()
        time.sleep(1)
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        time.sleep(1)
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        time.sleep(1)
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        time.sleep(1)
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        time.sleep(1)
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        time.sleep(1)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        time.sleep(2)
        profile_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='g0rxnol2 f804f6gw ln8gz9je ppled2lx gfz4du6o r7fjleex g9p5wyxn i0tg5vk9 aoogvgrq o2zu3hjb bs7a17vp csshhazd _11JPr']")))
        time.sleep(2)
        profile_button.click()
        time.sleep(1)
        profile_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='_11JPr']")))
        profile_button.click()
        time.sleep(1)
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        time.sleep(1)
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        time.sleep(1)
        self.driver.switch_to.active_element.send_keys(Keys.DOWN)
        time.sleep(1)
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        time.sleep(1)
        subprocess.run(["xdotool", "key", "ctrl+l"])
        time.sleep(1)
        subprocess.run(["xdotool", "type", "/home/seluser/automate_whatsapp/random_color_image.png"])
        time.sleep(1)
        subprocess.run(["xdotool", "key", "Return"])
        time.sleep(1)
        final_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='p357zi0d gndfcl4n ac2vgrno mh8l8k0y k45dudtp i5tg98hk f9ovudaz przvwfww gx1rr48f f8jlpxt4 hnx8ox4h k17s6i4e ofejerhi os0tgls2 g9p5wyxn i0tg5vk9 aoogvgrq o2zu3hjb hftcxtij rtx6r8la e3b81npk oa9ii99z p1ii4mzz']")))
        final_button.click()
        # Wait for the picture to be uploaded
        time.sleep(3)
        back_buttom = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='kk3akd72 dmous0d2 fewfhwl7 ajgl1lbb ltyqj8pj']")))
        back_buttom.click()
        time.sleep(1)
        #back_buttom.click()
        back_buttom = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//span[@data-icon='back']")))
        back_buttom.click()
    def run(self):
        while True:
            self.change_profile_picture()
            time.sleep(10)  # Wait for the defined time (default seconds)
