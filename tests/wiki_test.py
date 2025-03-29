import allure
from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.tag("Mobile")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "AleksSH")
@allure.story("Поиск")
@allure.feature("Проверка страниц")
def test_skip_pages():
    with allure.step('Проверка первой страницы'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('The Free Encyclopedia\n…in over 300 languages'))

    with allure.step('Проверка второй страницы'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('New ways to explore'))

    with allure.step('Проверка третьей страницы'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Reading lists with sync'))

    with allure.step('Проверка четвёртой страницы'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(have.text('Data & Privacy'))


@allure.tag("Mobile")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "AleksSH")
@allure.story("Поиск")
@allure.feature("Поиск в википедии текста 'Appium'")
def test_search_wiki_appium():
    with step('Ввести "Appium" в поиске Википедии'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Проверяем наименование результата'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))

    with step('Кликаем элемент'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.click()


@allure.tag("Mobile")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "AleksSH")
@allure.story("Поиск")
@allure.feature("Поиск в википедии текста 'Motorcycle'")
def test_search_wiki_moto():
    with step('Ввести "Motorcycle" в поиске Википедии'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Motorcycle')

    with step('Проверяем наименование результата'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Motorcycle'))

    with step('Кликаем элемент'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.click()

