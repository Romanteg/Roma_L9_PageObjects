from test_PageObject import RegistrationPage, Browser, Wait

registration_page = RegistrationPage()
browser_open = Browser()

    
def test_registration(): 
    
    registration_page.fill_first_name('Roman')
    registration_page.fill_last_name('Sergeev')
    registration_page.fill_email('test@test.ru')
    registration_page.gender.click()
    registration_page.fill_mobile_number('1234567890')
    registration_page.birthday.click()
    registration_page.birthday_year.click()
    registration_page.birthday_select.click()
    registration_page.birthday_day.click()
    registration_page.hobby1.click()
    registration_page.hobby2.click()
    registration_page.hobby3.click()
    registration_page.fill_adress('134358, Moscow, Tverskaya st. 15/1, r245')
    registration_page.state1.click()
    registration_page.state2.click() #Непонятно как найти элемент
    registration_page.state3.click()
    registration_page.state4.click()
    registration_page.submit.click()
    