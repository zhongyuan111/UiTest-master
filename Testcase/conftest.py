from selenium import webdriver
from page_object.login import LoginPage
from common.readconfig import ini
import  pytest
import  time
driver = None


@pytest.fixture(scope='session', autouse=True)
def browser(request):
    global driver

    if driver is None:
        driver = webdriver.Chrome()  # GUI界面运行
        driver.maximize_window()

        def fn():
            driver.quit()

        request.addfinalizer(fn)
        return driver

    return driver  # 返回驱动
# 参数autouse=True时，无需传login函数，测试用例在执行前都会先执行login函数
@pytest.fixture(scope='session', autouse=True)
def login(browser):
    login = LoginPage(browser)
    login.get_url(ini.url)
    time.sleep(2)
    login.input_name(ini.user_username())
    login.input_pwd(ini.user_password())
    login.click_login()
    time.sleep(5)




