from selene import browser, have
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Wait:
    def __init__(self):
        self.wait = WebDriverWait(browser, 10)
        
class Browser:
    def __init__(self):
        driver_options = webdriver.ChromeOptions()
        driver_options.page_load_strategy = 'eager'
        browser.config.driver_options = driver_options
        browser.config.window_width = 1920  # задает ширину окна браузера
        browser.config.window_height = 1080  # задает высоту окна браузера
        browser.config.base_url = 'https://demoqa.com/automation-practice-form'
        browser.open('/')
        
        
class RegistrationPage:
    def __init__(self):        
        self.first_name = browser.element('input[id="firstName"]')
        self.last_name = browser.element('input[id="lastName"]')
        self.email = browser.element('input[id="userEmail"]')
        self.gender = browser.element('label[for="gender-radio-1')
        self.mobile_number = browser.element('input[id="userNumber"]')
        self.birthday = browser.element('input[id="dateOfBirthInput"]')
        self.birthday_year = browser.element('[class="react-datepicker__year-select"]>[value="1986"]')
        self.birthday_select = browser.element('[class="react-datepicker__month-select"]>[value="3"]')
        self.birthday_day = browser.element('[aria-label="Choose Sunday, April 20th, 1986"]')
        self.hobby1 = browser.element('label[for="hobbies-checkbox-1"]')
        self.hobby2 = browser.element('label[for="hobbies-checkbox-2"]')
        self.hobby3 = browser.element('label[for="hobbies-checkbox-3"]')
        self.adress = browser.element('textarea[id="currentAddress"]')
        
        self.state1 = browser.element('[id="state"]')
        self.state2 = browser.element('[id="state"]>[class=" css-26l3qy-menu"]>[class=" css-11unzgr"]>[id="react-select-3-option-0"]')
        self.state3 = browser.element('[id="city"]')
        self.state4 = browser.element('[id="city"]>[class=" css-26l3qy-menu"]>[class=" css-11unzgr"]>[id="react-select-4-option-0"]')
        self.submit = browser.element('[id=submit]')
    def fill_first_name(self, value):
        self.first_name.type(value)
        return self
    def fill_last_name(self, value):
        self.last_name.type(value)
        return self   
    def fill_email(self, value):
        self.email.type(value)
        return self       
    def fill_gender(self, value):
        self.gender.type(value)
        return self
    def fill_mobile_number(self, value):
        self.mobile_number.type(value)
        return self
    def fill_adress(self, value):
        self.adress.type(value)
        return self

    
    

    
