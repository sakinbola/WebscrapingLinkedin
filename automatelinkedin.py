from selenium import webdriver
# allows automation of webbroswer
from selenium.webdriver.chrome.service import Service
# handles chrome driver as service 
from webdriver_manager.chrome import ChromeDriverManager
# ensures you have the correct version fo chromedrivermanager
from selenium.webdriver.common.keys import Keys
# allows you to interact why kjeys
from selenium.webdriver.common.by import By
# import keys module to simulate pressing keys 
from selenium.webdriver.common.keys import Keys 
# allows you to interact with element ids , classnames etc
from selenium.common.exceptions import NoSuchElementException
# if no element found 
import time
# for time.sleep etc
from selenium.webdriver.chrome.options import Options
# for add argument functions was recieveing these two errors 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os 
from dotenv import load_dotenv

# [5384:2080:0301/122825.925:ERROR:ssl_client_socket_impl.cc(877)] handshake failed; returned -1, SSL error code 1, net_error -201
# [5384:2080:0301/122825.948:ERROR:socket_manager.cc(147)] Failed to resolve address for stun.l.google.com., errorcode: -105
# 2nd one was like 50 of them 

# webdriver managaer automatically downlaods the correct chromedriver elimintatinf need for manual updatesd

# could make a try except function for all webdriver waits incase an element isnt found 
def setup():
    options = Options()
    options.add_argument("--disable-webrtc") 
    # disables webrtc stun errors

    options.add_argument("--log-level=3") 
    # stops excessive loggin look mroe into this 


    options.add_argument("--ignore-certificate-errors")
    # ignore ssl errors

    options.add_argument("--disable-blink-features=AutomationControlled")
    # prevents bot detections 

# try except if driver is working or chromse is installed 
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
    # service starts the chromedriver process and esnrues it can interac with chrome
    # options=options adds option arguments to driver
    return driver


def login(driver,email,password):

    driver.get("https://www.linkedin.com/jobs/")

    assert "LinkedIn" in driver.title
    # do you ahve right webpage 
    # login = driver.find_element(By.XPATH,"//*[@id='session_password']")
    # old way 

    sign_in = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='session_key']")))

    # new way 
    sign_in.clear()
    sign_in.send_keys(email)

    login = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='session_password']")))
    login.clear()
    login.send_keys(password)

    button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='main-content']/section[1]/div/div/form/div[2]/button")))
    button.click()
    driver.set_window_size(1920, 1080)


def search(driver):


    search_bar =  WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]")))
    search_bar.clear()
    job_input = input("What type of job are you looking for: ")
    search_bar.send_keys(job_input)
    search_bar.send_keys(Keys.RETURN)

    live = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]")))
    live_input =  input("Where do you live City , State or ZipCode ex Hamilton, Ontario, Canada is proper formatting: ")
    live.clear()
    live.send_keys(live_input)
    live.send_keys(Keys.RETURN) 

def filters(driver):
    print("hello")

    all_filters =  WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/div/div/button")))
    all_filters.click()

    reset =  WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"    /html/body/div[4]/div/div/div[3]/div/button[1]/span")))
    reset.click()


    most_recent = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[2]/ul/li[2]/fieldset/div/ul/li[1]/label")))
    most_recent.click()


    twntyfour_hours = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[4]/label")))
    twntyfour_hours.click()

    entry_level = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[2]/ul/li[4]/fieldset/div/ul/li[2]/label")))
    entry_level.click()

    internship = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[2]/ul/li[4]/fieldset/div/ul/li[1]/label")))
    internship.click()

    apply = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[3]/div/button[2]/span")))
    apply.click()

def good_stuff(driver):
    # algorithim to mass apply to jobs 
    # will add others later
    # for my goodstuff algo its going to be right now sometype 
    # of i choose easy apply , click first job easy apply ,
    # while loop or for loop , click second one use a formatted 
    # string to change xpath , if hit bottom of page , use a formatted 
    # string
    #     to click hnext page, and so on until theres no next paghe 
    pass


# code block that is true deeper explanaiton but not to into it for now 
if __name__ == "__main__":
    driver = setup()

    with open("linkedin_config.txt","r")as file:
        lines = file.readlines()

    email = lines[0].strip()
    password =  lines[1].strip()
    print(email)
    print(password)

    # this one uses a .txt file and strips the lines 
    # might add more so you just put everyting in the txt file instead of 
    #prompts 


    # this is os 
    # reall cool so set in cmd prompt , linkedin_meial to your email
    # then import os , .getenv and voila 
    # when using os method 


    try:
        login(driver,email,password)
        search(driver)
        filters(driver)
    # always exectues instead of except which only executes in certain cases 
    finally:
        var = True
        while var:
            choice = input("Type finish to exit: ").strip().lower()
            if choice == "finish":
                print("You have exited")
                var = False
            else:
                pass

        driver.quit()
