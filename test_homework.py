from selene import browser, have, be
from selenium import webdriver

def test_complete_todo():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options
    browser.config.window_width = 1920  # задает ширину окна браузера
    browser.config.window_height = 1080  # задает высоту окна браузера
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.open('/')
    #Ввод имени
    browser.element('input[id="firstName"]').should(be.blank)
    browser.element('input[id="firstName"]').click()
    browser.element('input[id="firstName"]').type('Roman')
    #Ввод фамилии
    browser.element('input[id="lastName"]').should(be.blank)
    browser.element('input[id="lastName"]').click()
    browser.element('input[id="lastName"]').type('Sergeev')
    #Ввод емейл
    browser.element('input[id="userEmail"]').should(be.blank)
    browser.element('input[id="userEmail"]').click()
    browser.element('input[id="userEmail"]').type('tester@test.ru')
    #Выбор пола
    browser.element('label[for="gender-radio-1"]').click()
    #Пустое и телефон
    browser.element('input[id="userNumber"]').should(be.blank)
    browser.element('input[id="userNumber"]').click()
    browser.element('input[id="userNumber"]').type('1234567890')
    #Дата рождения
    browser.element('input[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__year-select"]>[value="1986"]').click()
    browser.element('[class="react-datepicker__month-select"]>[value="3"]').click()
    browser.element('[aria-label="Choose Sunday, April 20th, 1986"]').click()
    #Хобби проверка кликами
    browser.element('label[for="hobbies-checkbox-1"]').click().click()
    browser.element('label[for="hobbies-checkbox-2"]').click().click()
    browser.element('label[for="hobbies-checkbox-3"]').click().click().click()
    #Адрес
    browser.element('textarea[id="currentAddress"]').type('134358, Moscow, Tverskaya st. 15/1, r245')
    #Меню штат
    browser.element('[id="state"]').click()
    browser.element('[id="state"]>[class=" css-26l3qy-menu"]>[class=" css-11unzgr"]>[id="react-select-3-option-0"]').click()
    browser.element('[id="state"]').click()
    browser.element('[id="state"]>[class=" css-26l3qy-menu"]>[class=" css-11unzgr"]>[id="react-select-3-option-1"]').click()
    browser.element('[id="state"]').click()
    browser.element('[id="state"]>[class=" css-26l3qy-menu"]>[class=" css-11unzgr"]>[id="react-select-3-option-2"]').click()
    browser.element('[id="state"]').click()
    browser.element('[id="state"]>[class=" css-26l3qy-menu"]>[class=" css-11unzgr"]>[id="react-select-3-option-3"]').click()
    #Меню город
    browser.element('[id="city"]').click()
    browser.element('[id="city"]>[class=" css-26l3qy-menu"]>[class=" css-11unzgr"]>[id="react-select-4-option-0"]').click()
    browser.element('[id="city"]').click()
    browser.element('[id="city"]>[class=" css-26l3qy-menu"]>[class=" css-11unzgr"]>[id="react-select-4-option-1"]').click()
    browser.element('[id="city"]').click()
    browser.element('[id="city"]>[class=" css-26l3qy-menu"]>[class=" css-11unzgr"]>[id="react-select-4-option-0"]').click()
    #Кнопка Submit
    browser.element('[id=submit]').click()
    browser.wait_until(5)
    browser.element('[id = "closeLargeModal"]').click()
    print(" Test run successful. Exit")
    browser.quit()
