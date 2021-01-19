from app_selenium import test_cep
from get_data import xls_read
from save_report import project_report

PATH = r'C:\IBM\Treinamentos\Automation_Selenium\drivers\chromedriver.exe'
url = 'http://127.0.0.1:6035/'
table_xpath = '/html/body/div/table'
file_path = r'C:\IBM\Treinamentos\Automation_Selenium\data\cep_list.xls'
table_data_xpath = [
    '/html/body/div/table/tbody/tr[2]/td[2]',
    '/html/body/div/table/tbody/tr[3]/td[2]',
    '/html/body/div/table/tbody/tr[4]/td[2]',
    '/html/body/div/table/tbody/tr[5]/td[2]',
    '/html/body/div/table/tbody/tr[6]/td[2]',
    '/html/body/div/table/tbody/tr[7]/td[2]'
]
table_test_xpath = [
    '/html/body/div/table/tbody/tr[2]/td[1]',
    '/html/body/div/table/tbody/tr[3]/td[1]',
    '/html/body/div/table/tbody/tr[4]/td[1]',
    '/html/body/div/table/tbody/tr[5]/td[1]',
    '/html/body/div/table/tbody/tr[6]/td[1]',
    '/html/body/div/table/tbody/tr[7]/td[1]'
]
screenshots_path = r'C:\IBM\Treinamentos\Automation_Selenium\outputs\screeshots'

if __name__ == '__main__':
    tests = []
    cep_list = xls_read(file_path)

    for cep in cep_list:
        tests.append(test_cep(PATH, url, cep, table_xpath, table_test_xpath, table_data_xpath, screenshots_path))

    project_report(tests)
    print('Report Created!')
