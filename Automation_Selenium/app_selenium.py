import time
import itertools
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def open_browser_chrome(path, site):
    driver = ''
    try:
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(executable_path=path, options=options)
    except OSError as e:
        print(e)
    except NameError as error:
        print(error)
    else:
        driver.get(site)
    finally:
        return driver


def open_browser_firefox(path, url):
    driver = ''
    try:
        driver = webdriver.Firefox(executable_path=path)

    except OSError as e:
        print(e)
    except NameError as error:
        print(error)
    else:
        driver.get(url)
    finally:
        return driver


def fill_search_box(driver, input_string, element_name, screenshots_path):
    image_name = ''
    try:
        WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.NAME, element_name)))
    except NameError as error:
        print(error)
    else:
        search_box = driver.find_element_by_name(element_name)
        search_box.clear()
        search_box.send_keys(input_string)
        image_name = 'test_' + input_string + '_input'
        print_screen(driver, screenshots_path, image_name)
        search_box.send_keys(Keys.ENTER)
    finally:
        return image_name


def look_for_xpath(driver, xpath):
    try:
        WebDriverWait(driver, 15).until(ec.presence_of_element_located((By.XPATH, xpath)))
    except NameError as error:
        print(error)
    else:
        driver.find_element_by_xpath(xpath)


def get_text_by_xpath(driver, xpath):
    element_text = ''
    try:
        element_text = driver.find_element_by_xpath(xpath).text
    except NameError as error:
        print(error)
    finally:
        return element_text


def print_screen(driver, folder_path, image_name):
    # S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
    # driver.set_window_size(S('Width'), S('Height'))
    # driver.find_element_by_tag_name('body').screenshot(folder_path + '\\' + time.strftime("%Y-%m-%d") + '_' + image_name + '.png')
    driver.get_screenshot_as_file(folder_path + '\\' + time.strftime("%Y-%m-%d") + '_' + image_name + '.png')


def test_cep(path, url, cep, table_xpath, table_test_xpath, table_data_xpath, screenshots_path):
    count = 0
    results = {}
    test = {}
    test_name = []
    info_test = Test()
    driver = open_browser_chrome(path, url)
    input_image_name = fill_search_box(driver, cep, 'cep', screenshots_path)
    look_for_xpath(driver, table_xpath)
    image_name = 'test_' + cep + '_result'
    print_screen(driver, screenshots_path, image_name)
    for test_xpath in table_test_xpath:
        test_name.append(get_text_by_xpath(driver, test_xpath))
    for data_xpath in table_data_xpath:
        results[str(cep) + '_' + test_name[count]] = get_text_by_xpath(driver, data_xpath)
        count += 1

    info_test.get_input_string(cep)
    info_test.get_results(results)
    info_test.get_input_screenshot(screenshots_path + '\\' + time.strftime("%Y-%m-%d") + '_' + input_image_name + '.png')
    info_test.get_result_screenshot(screenshots_path + '\\' + time.strftime("%Y-%m-%d") + '_' + image_name + '.png')

    if results[str(cep) + '_' + test_name[4]] == 'Failed':
        test[cep] = 'Failed'
    elif results[str(cep) + '_' + test_name[5]] == 'Failed':
        test[cep] = 'Failed'
    else:
        test[cep] = 'Passed'

    info_test.get_general_results(test)
    driver.close()

    return info_test


class Test:
    new_id = itertools.count()

    def __init__(self):
        self.id_test = next(self.new_id) + 1
        self.input_string = ''
        self.general_result = ''
        self.results = ''
        self.input_screenshot = ''
        self.result_screenshot = ''

    def get_input_string(self, input_string):
        self.input_string = input_string

    def get_general_results(self, general_result):
        self.general_result = general_result

    def get_results(self, results):
        self.results = results

    def get_input_screenshot(self, input_screenshot):
        self.input_screenshot = input_screenshot

    def get_result_screenshot(self, result_screenshot):
        self.result_screenshot = result_screenshot
