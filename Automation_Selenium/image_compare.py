from app_selenium import open_browser_firefox

driver_path = r'C:\IBM\Treinamentos\Automation_Selenium\drivers\firefox_geckodriver.exe'
url = 'https://www.cnnbrasil.com.br/'

driver = open_browser_firefox(driver_path, url)

dir = r'C:\Users\DiegoDeFreitasMaia\Downloads'
local_img = "{}\{}".format(dir, "cnn.jpg")

print(local_img)

