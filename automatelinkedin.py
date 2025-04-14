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
import logging
from typing import Optional

# DISCLAIMER:
# This project was created for educational and personal learning purposes only.
# It is NOT intended for active use on LinkedIn, as automation of job applications



# updates to consider 
# use os.getenv to get email and password from environment variables
# clean up code and remove unnecessary comments
# improve testing and error handling 
# expand to be used for different filters , multiple accounts , retry if something occurs 
# ai integration 

def collect_element(driver,by,element):
    try:
        element = WebDriverWait(driver, 50).until(
            EC.presence_of_element_located((by, element))
        )
        return element
    except NoSuchElementException:
        print(f"Element with {by} '{element}' not found.")
        return None
    

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

    sign_in = collect_element(driver, By.ID, "session_key")
    if not sign_in:
        print("Sign-in element not found. Exiting...")
        driver.quit()
        exit()

    sign_in.clear()
    sign_in.send_keys(email)

    login = collect_element(driver, By.XPATH, "//*[@id='session_password']")
    login.clear()
    login.send_keys(password)

    button = collect_element(driver, By.XPATH, "//*[@id='main-content']/section[1]/div/div/form/div[2]/button")
    button.click()
    driver.set_window_size(1920, 1080)


def search(driver):


    search_bar = collect_element(driver, By.XPATH, "/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]")
    search_bar.clear()
    job_input = input("What type of job are you looking for: ")
    search_bar.send_keys(job_input)
    search_bar.send_keys(Keys.RETURN)

    live = collect_element(driver, By.XPATH, "/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div/input[1]")
    live_input =  input("Where do you live City , State or ZipCode ex Hamilton, Ontario, Canada is proper formatting: ")
    live.clear()
    live.send_keys(live_input)
    live.send_keys(Keys.RETURN) 

def filters(driver):
    # print("hello")

    all_filters = collect_element(driver, By.XPATH, "/html/body/div[6]/div[3]/div[4]/section/div/section/div/div/div/div/div/button")
    all_filters.click()

    # reset = collect_element(driver, By.XPATH, "/html/body/div[4]/div/div/div[3]/div/button[1]/span")
    # reset.click()

    # time.sleep(2)

    
    most_recent = collect_element(driver, By.XPATH, "/html/body/div[4]/div/div/div[2]/ul/li[2]/fieldset/div/ul/li[1]/label")
    most_recent.click()


    twntyfour_hours = collect_element(driver, By.XPATH, "/html/body/div[4]/div/div/div[2]/ul/li[3]/fieldset/div/ul/li[4]/label")
    twntyfour_hours.click()

    entry_level = collect_element(driver, By.XPATH, "/html/body/div[4]/div/div/div[2]/ul/li[4]/fieldset/div/ul/li[2]/label")
    entry_level.click()

    internship = collect_element(driver, By.XPATH, "/html/body/div[4]/div/div/div[2]/ul/li[4]/fieldset/div/ul/li[1]/label")
    internship.click()

    apply = collect_element(driver, By.XPATH, "/html/body/div[4]/div/div/div[3]/div/button[2]/span")
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
    try:
        #
        def algo(accum):
            while accum < 26:
                # click first job
                job_button = collect_element(driver, By.XPATH, f"/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[{accum}]/div/div") 
                job_button.click()

                time.sleep(2)
                
                # click easy apply 
                easy_apply_button = collect_element(driver, By.XPATH, f"/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div[5]/div/div/div/button/span")
                easy_apply_button.click()

                # wait 
                time.sleep(5)

                # click next button
                next_button1 = collect_element(driver, By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button/span")
                next_button1.click()

                # click next2

                next_button2 = collect_element(driver, By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span")
                next_button2.click()

                try:
                    input("Review Screen and add proper information Press Enter to exit the program...")
                except KeyboardInterrupt:
                    print("\nDone")
                finally:
                    print("Done")
                
                # click review 
                # could implement ai to fill out the review section 
                # json file to store info 
                
                review = collect_element(driver, By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span")
                review.click()

                submit_button =  collect_element(driver, By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]/span")
                submit_button.click()

                # wait 
                time.sleep(5)
                accum+=1

            return 1
        

        try:
            page_number = 1
            while True:
                if algo(1) == 1:  # does algo

                    # Check if next page exists 
                    next_page = collect_element(driver, By.XPATH, f"/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/div[2]/div[2]/ul/li[{page_number}]/button")
                    if next_page is None:
                        print("Reached last page. Finishing job applications...")
                        return  # Exit function cleanly
                    
                    next_page.click()
                    page_number += 1
                    time.sleep(5)
                    
        except Exception as e:
            print(f"An error occurred during pagination: {e}")
            return  # Exit function on error
        
        
    except NoSuchElementException:
        print("No more jobs to apply to.")
        return 

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        print("Finished processing all available jobs")
        return  # Exit function after completion


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
        # if something pressed program will exit 
        try:
            input("Press Enter to exit the program...")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
        finally:
            print("Closing browser...")
            driver.quit()
