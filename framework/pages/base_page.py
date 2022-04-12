class BasePage:
    def __init__(self, driver=None):
        self.driver = driver if driver else driver.Chrome()

    def get(self, url):
        self.url = url

    def get_current_url(self):
        return self.driver.current_url

    def __repr__(self):
        return f'Base page object, class name: {self.__class__.__name__}'
    