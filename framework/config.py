from os import getenv
from dotenv import load_dotenv

load_dotenv(verbose=True)

SITE = getenv("SITE@", "http://automationpractice.com")
IMPLICIT_WAIT = 10

BROWSER = getenv("BROWSER", "chrome")
SUPPORTED_BROWSERS = ["chrome", "firefox"]

VALID_USER_EMAIL = getenv("USER_EMAIL@", "test19@gmail.com")
INVALID_USER_EMAIL = getenv("USER_EMAIL@", "test")
