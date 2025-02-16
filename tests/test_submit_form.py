from selene import browser , have, be


def test_submit_practice_form():
    browser.element('#firstName').send_keys('Julia')
    browser.element('[placeholder="Last Name"]').send_keys('Petrova')
    browser.element('#userEmail').send_keys('ulapetrova@mail.ru')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('[placeholder="Mobile Number"]').send_keys('89252223344')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="9"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1987"]').click()
    browser.element('.react-datepicker__day--001').click()
    # browser.all('[for="hobbies-checkbox-3"]').click()
    browser.element('#currentAddress').type('Komsomolskaya street 90,kv 13')

    browser.element('#state').click().element('div[id^="react-select-3-option"]').click()
    browser.element('#city').click().element('div[id^="react-select-4-option"]').click()

    browser.element('#submit').press_enter()