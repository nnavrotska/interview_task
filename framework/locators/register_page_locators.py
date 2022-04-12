from selenium.webdriver.common.by import By


class RegisterPageLocators:
    REGISTER_URL = 'http://automationpractice.com/index.php?controller=authentication&back=my-account'
    CREATE_AN_ACCOUNT_BTN = (By.XPATH, '//*[@id="SubmitCreate"]/span')
    USER_EMAIL = (By.XPATH, '//*[@id="email_create"]')
    INVALID_EMAIL_ALERT = (By.XPATH, '//*[@id="create_account_error"]')

    def __repr__(self):
        return f'Register Page Locators object, class name: {self.__class__.__name__}'
