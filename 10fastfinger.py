'''
website = https://10fastfingers.com/typing-test/english
element = <span wordnr="0" class="highlight">left</span>

input_keyboard = <input type="text" class="form-control" id="inputfield" value="" dir="ltr" placeholder="" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false">


plan

connecting selenium with webdriver
checking browser on specified port
checking if website opened
    if not then opening it
fetching words
sending keys to input input_keyboard
repeating until element is not found
    stop the process and present the count of words written


'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


website = "https://10fastfingers.com/typing-test/english"

chromedriver = "path_to_latest_chrome_driver"

def opening_website():
    global s, driver
    s = Service(chromedriver)
    driver = webdriver.Chrome(service=s)
    driver.get(website)




''' checking for cookie messages
    element to click = <button id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll" class="CybotCookiebotDialogBodyButton" tabindex="0" lang="en">Allow all cookies</button>
    '''
def checking_cookie_messages():
    driver.implicitly_wait(10)
    try :
        cookie_button = driver.find_element_by_id("CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        cookie_button.click()
    except NoSuchElementException:
        pass

''' fetching words and writing '''

def fetching_words():
    while True:
        try:
            word = driver.find_element_by_class_name("highlight")
            word = word.text
            print(word) #debugging purpose
            input_field = driver.find_element_by_id("inputfield")
            input_field.send_keys(word + " ")
            driver.implicitly_wait(1)

        except NoSuchElementException:
            break

opening_website()
checking_cookie_messages()

fetching_words()
