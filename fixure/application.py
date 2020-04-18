from selenium import webdriver
from fixure.session import Sessionhelper
from fixure.project import Projecthelper
from fixure.james import JamesHelper
from fixure.signup import SignupHelper
from fixure.mail import MailHelper
from fixure.soap import SoapHelper




class Application:

    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = Sessionhelper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.base_url = config['web']['baseurl']
        self.config = config
        self.project = Projecthelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
