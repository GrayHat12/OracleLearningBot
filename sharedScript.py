from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("test-type");
chrome_options.add_argument("--enable-javascript")


# replace path with chromedriver path on your system
driver = webdriver.Chrome(executable_path=r"C:\Users\Rahul\PaidProjects\PythonInstagram\gray-scraper\chromedriver.exe",chrome_options=chrome_options)

url = 'https://ilearning.oracle.com/ilearn/en/learner/jsp/login.jsp?site=OracleAcad'
uname = 'username_here' # your username here
passw = 'password_here' # your password here

driver.get(url)
time.sleep(3)

e_uname = driver.find_element_by_name('username')
e_uname.send_keys(uname)
e_pass = driver.find_element_by_name('password')
e_pass.send_keys(passw)
login = driver.find_element_by_xpath('//a[contains(@class,"ButtonText")]')
login.click()

st = 'javascript:launchContent(-1,2374678804,"N","","");'
play = driver.find_element_by_xpath('//a[contains(@href,\'javascript:launchContent(-1,2374680237,"N","","");\')]') # for Java Foundations 2019 Learner - English
#play = driver.find_element_by_xpath('//a[contains(@href,\'javascript:launchContent(-1,2374678804,"N","","");\')]') # for Java Fundamentals 2019 Learner - English
play.click();
time.sleep(30)
nxt = None
i = 0
print(i+1)
def getNext(drivr):
    print('in')
    nnext = None
    while nnext==None:
        try:
            nnext = drivr.find_element_by_xpath('//a[contains(@href,"javascript:next()")]')
        except Exception as ex:
            print(ex)
            time.sleep(5)
    print('out')
    return nnext
driver.switch_to_frame("toolbar_frame")
nxt = getNext(driver)
while nxt!=None:
    i+=1
    print(i+1)
    nxt.click()
    time.sleep(30)
    nxt = getNext(driver)
print('Done')