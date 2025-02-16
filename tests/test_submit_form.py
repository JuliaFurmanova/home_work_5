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
    browser.element('#subjectsInput').send_keys('Biology').press_enter()

    browser.all('.custom-control-label').element_by(have.text('Sports')).click()
    browser.element('#currentAddress').type('Komsomolskaya street 90,kv 13')
    browser.element('#state').click().element('div[id^="react-select-3-option"]').click()
    browser.element('#city').click().element('div[id^="react-select-4-option"]').click()

    browser.element('#submit').press_enter()

    browser.element('.modal-content').should(be.visible)
    browser.element('.table').should(have.text('Julia Petrova'))
    browser.element('.table').should(have.text('ulapetrova@mail.ru'))
    browser.element('.table').should(have.text('Female'))
    browser.element('.table').should(have.text('8925222334'))
    browser.element('.table').should(have.text('1 October,1987'))
    browser.element('.table').should(have.text('Biology'))

    browser.element('.table').should(have.text('Komsomolskaya street 90,kv 13'))
    browser.element('.table').should(have.text('NCR Delhi'))