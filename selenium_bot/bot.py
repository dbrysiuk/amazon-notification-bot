from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from alert import Alert


class Bot:

    def __init__(self, url, email):
        self.url = url
        self.email = email

    def check_product(self):
        # browser settings
        options = Options()
        options.headless = False
        options.add_experimental_option("detach", True)

        # browser init and call product url
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        browser.maximize_window()
        browser.get(self.url)

        # loop until article is available
        while True:
            try:
                # check if buy button is available with 10 sec page loading time
                WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.ID, 'buy-now-button'))
                )

                print("Product is available")
                # send email notification
                Alert.email_alert(browser.title + " is available !!!", browser.current_url, self.email)
                browser.quit()
                break
            except:
                print("Product is not available")
                # reload browser and try again
                browser.execute_script("location.reload(true);")
