import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from whatsapp_automation import WhatsappAutomation

# Set up Chrome WebDriver
chrome_options = Options()
# Run Chrome in headless mode
#chrome_options.add_argument("--headless")
chrome_options.add_argument("user-data-dir=/home/seluser/.config/google-chrome/Default")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Specify the webpage URL here
webpage_url = "https://web.whatsapp.com/"

# Navigate to the webpage
driver.get(webpage_url)
# Initialize and run WhatsappAutomation
whatsapp_automation = WhatsappAutomation(driver)
#time.sleep(24 * 60 * 60)
whatsapp_automation.run()

# Quit the WebDriver
driver.quit()