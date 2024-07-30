# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
import time
from datetime import datetime

# Инициализация веб-драйвера
driver = webdriver.Chrome()


class Selectors:
    URL_ONLINE = "online.sbis.ru"
    STAND_FIX = 'fix-'
    LOGIN = '[data-qa="auth-AdaptiveLoginForm__login"] .controls-Field'
    PASSWORD = '[data-qa="auth-AdaptiveLoginForm__password"] .controls-Field'
    BTN_CONT_IN_ACCORDEON = '[data-name="contacts"] [data-qa="NavigationPanels-Accordion__title"]'
    BTN_CONT_IN_REESTR = '[name="TabContent2"]'
    REESTR_CONTACTS = '[data-qa="tile-container"]'
    INPUT_CONTACTS = '[inputmode="text"]'
    INFO_CONTACT = '.msg-info-tile'
    SEND_MESSAGE = '[data-qa="cell"] [title="Отправить сообщение"]'
    INFO_PERSON = '.msg-person-tile-new'
    INPUT_FORM_MSG = '[role="textbox"] [data-slate-node="element"]'
    SEND_MSG = '[title="Отправить"]'
    NO_READ_MSG = '.msg-entity-info__unread-icon'
    MSG_CONTACT = '.msg-entity-layout__message-content_padding-right_default'
    DELETE_MSG = '.controls-Menu__content[title="Удалить"]'
    BUTTON_DELETE_YES = '[data-qa="controls-ConfirmationDialog__button-true"]'
    BUTTON_DELETE_OK = '[data-qa="controls-ConfirmationDialog__button-true"]'
    NOT_MSG = '[class="msg-EmptyList__message"]'
    PEOPLE_CONTENT = '.msg-PeopleBrowser'
    POP_UP = '.controls-Menu__popup-direction-vertical-bottom'
    NEED_NAME_CONTACT = '[title="Мел Артем Кон"]'


class Texts:
    LOGIN_MEL = "melartkon1"
    PASSWORD_MEL = "melartkon11"
    NAME_CONTACT = 'Мел'


def maximize_and_navigate(full_url):
    """
    Универсальный метод для перехода на страницу и максимизации окна браузера.

    :param: Full_url: Путь до страницы
    """
    driver.maximize_window()
    driver.get(full_url)  # Переход на указанную страницу


def auth(by_login, loc_login, by_pas, loc_pas):
    """
    Универсальный метод для авторизации на онлайне.

    :param by_login: Стратегия поиска локатора логина (например, By.CSS_SELECTOR)
    :param loc_login: Локатор логина (например, "Selectors.LOGIN")
    :param by_pas: Стратегия поиска локатора логина (например, By.CSS_SELECTOR)
    :param loc_pas: Локатор пароля (например, "Selectors.PASSWORD")
    """
    wait_element(driver, By.CSS_SELECTOR, Selectors.LOGIN)
    driver.find_element(by_login, loc_login).send_keys(Texts.LOGIN_MEL, Keys.ENTER)
    wait_element(driver, By.CSS_SELECTOR, Selectors.PASSWORD)
    driver.find_element(by_pas, loc_pas).send_keys(Texts.PASSWORD_MEL, Keys.ENTER)


def find_and_click_element(by, locator):
    """
    Универсальный метод для поиска элемента на странице и клика по нему.

    :param by: Метод поиска (например, By.CSS_SELECTOR)
    :param locator: Локатор элемента (например, "Selectors.ABOUT_LINK")
    :return: Найденный элемент или None, если элемент не найден
    """
    try:
        driver.find_element(by, locator).click()
    except NoSuchElementException:
        print(f"Элемент с локатором {locator} не найден")
        return None


def wait_element(driver, by, locator, timeout=10):
    """
    Ожидание появления элемента на странице.

    :param driver: Экземпляр веб-драйвера Selenium.
    :param by: Метод поиска (например, By.CSS_SELECTOR).
    :param locator: Локатор элемента (например, "Selectors.BUTTON_CONTACT").
    :param timeout: Время ожидания в секундах (по умолчанию 10 секунд).
    """
    try:
        WebDriverWait(driver, timeout).until(
            ec.presence_of_element_located((by, locator))
        )
        time.sleep(1)
    except TimeoutException:
        raise


def perform_action(driver, css_selector, action_type):
    """
    Выполняет указанное действие с элементом, найденным по CSS-селектору.

    Параметры:
    :param: driver: Экземпляр веб-драйвера Selenium.
    :param: css_selector (str): CSS-селектор для поиска элемента.
    :param: action_type (str): Тип действия, которое нужно выполнить ('context_click' или 'click').
    :return: bool: True, если действие выполнено успешно, иначе False.
    """
    try:
        element = driver.find_element(By.CSS_SELECTOR, css_selector)
        actions = ActionChains(driver)
        wait_element(driver, By.CSS_SELECTOR, css_selector)
        if action_type == 'context_click':
            actions.context_click(element).perform()
        elif action_type == 'click':
            actions.click(element).perform()
        else:
            raise ValueError("Unsupported action type: {}".format(action_type))
        return True
    except NoSuchElementException:
        print("Element not found: {}".format(css_selector))
        return False
    except Exception as e:
        print("An error occurred: {}".format(e))
        return False


try:
    maximize_and_navigate(f'https://{Selectors.STAND_FIX}{Selectors.URL_ONLINE}')
    auth(By.CSS_SELECTOR, Selectors.LOGIN, By.CSS_SELECTOR, Selectors.PASSWORD)
    wait_element(driver, By.CSS_SELECTOR, Selectors.BTN_CONT_IN_ACCORDEON)

    driver.get('https://fix-online.sbis.ru/page/contacts')
    wait_element(driver, By.CSS_SELECTOR, Selectors.INPUT_CONTACTS)
    message = driver.find_element(By.CSS_SELECTOR, Selectors.INPUT_CONTACTS)
    wait_element(driver, By.CSS_SELECTOR, Selectors.INPUT_CONTACTS)
    driver.find_element(By.CSS_SELECTOR, Selectors.INPUT_CONTACTS).send_keys(Texts.NAME_CONTACT)
    wait_element(driver, By.CSS_SELECTOR, Selectors.NEED_NAME_CONTACT)

    # Появление всплывающего окна на контакте
    perform_action(driver, Selectors.INFO_PERSON, 'context_click')
    wait_element(driver, By.CSS_SELECTOR, Selectors.SEND_MESSAGE)

    # Клик на "Отправить сообщение"
    perform_action(driver, Selectors.SEND_MESSAGE, 'click')
    wait_element(driver, By.CSS_SELECTOR, Selectors.INPUT_FORM_MSG)
    driver.find_element(By.CSS_SELECTOR, Selectors.INPUT_FORM_MSG).send_keys(Texts.NAME_CONTACT)

    print(f'Сообщение: "{Texts.NAME_CONTACT}" - написано')

    # Отправка сообщения
    wait_element(driver, By.CSS_SELECTOR, Selectors.SEND_MSG)
    find_and_click_element(By.CSS_SELECTOR, Selectors.SEND_MSG)

    # Появление всплывающего окна на контакте
    perform_action(driver, Selectors.INFO_PERSON, 'context_click')

    # Клик на "Отправить сообщение"
    msg = driver.find_element(By.CSS_SELECTOR, Selectors.SEND_MESSAGE)
    perform_action(driver, Selectors.SEND_MESSAGE, 'click')
    wait_element(driver, By.CSS_SELECTOR, Selectors.NO_READ_MSG)

    # Проверка отображения отправленного сообщения
    find_and_click_element(By.CSS_SELECTOR, Selectors.NO_READ_MSG)
    wait_element(driver, By.CSS_SELECTOR, Selectors.MSG_CONTACT)
    element = driver.find_element(By.CSS_SELECTOR, Selectors.MSG_CONTACT)
    assert f'{element.text[:3]}' == Texts.NAME_CONTACT
    print(f'Сообщение: "{element.text[:3]}" - отображается')
    perform_action(driver, Selectors.MSG_CONTACT, 'context_click')

    # Клик на "Удалить сообщение"
    wait_element(driver, By.CSS_SELECTOR, Selectors.DELETE_MSG)
    find_and_click_element(By.CSS_SELECTOR, Selectors.DELETE_MSG)
    wait_element(driver, By.CSS_SELECTOR, Selectors.BUTTON_DELETE_YES)
    find_and_click_element(By.CSS_SELECTOR, Selectors.BUTTON_DELETE_YES)
    time.sleep(1)
    try:
        element = driver.find_element(By.CSS_SELECTOR, Selectors.MSG_CONTACT).is_displayed()
        assert not element.is_displayed()
    except NoSuchElementException:
        pass
    print(f'Сообщение: "{Texts.NAME_CONTACT}" удалено и не отображается')

    not_msg = driver.find_element(By.CSS_SELECTOR, Selectors.NOT_MSG)
    assert not_msg.is_displayed()
    find_and_click_element(By.CSS_SELECTOR, Selectors.BUTTON_DELETE_OK)
    time.sleep(1)

    print(f'Тест успешно пройден')


finally:
    driver.quit()  # Закрытие браузера
