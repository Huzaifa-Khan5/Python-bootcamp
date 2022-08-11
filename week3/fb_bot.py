from selenium import webdriver
from getpass import getpass
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def share_post():
    share_button=driver.find_element_by_xpath('//*[@id="MPhotoLowerContent"]/div/footer/div/div/div[3]/a')
    share_button.click()
    write_post_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="share-with-message-button"]')))
    write_post_button.click()
    message_box=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="share_msg_input"]')))
    message='''This post was shared using a bot that I learnt to create from Python Bootcamp 2020 held by DSC@DSU. 
                #DSCDSU #DeveloperStudentClubs #DSCPakistan #Python #Bot'''
    message_box.send_keys(message)
    post_button=driver.find_element_by_xpath('//*[@id="share_submit"]').click()

def like_post():
    like_button=WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div[data-sigil="ufi-inline-actions"] div')))
    like_button.click()
   

def post_link():
    post_link=input("enter link which you want to share:")
    driver.get(post_link)
    like_post()
    share_post()
    

def not_now_button():
    not_now_button= WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="root"]/div[1]/div/div/div[3]/div[1]/div/div/a')))
    not_now_button.click()


def login_info():
    email_field=driver.find_element_by_xpath('//*[@id="m_login_email"]')
    password_field=driver.find_element_by_xpath('//*[@id="m_login_password"]')
    login_button=driver.find_element_by_css_selector('button[data-sigil="touchable login_button_block m_login_button"]')
    email="03349159978"
    password=getpass("password: ")
    email_field.send_keys(email)
    password_field.send_keys(password)
    login_button.click()
    not_now_button()
   
    


def initiate_browser():
    driver=webdriver.Chrome()
    return driver

def login(url):
    driver.get(url)

def main():
    global driver
    driver=initiate_browser()
    login("https://m.facebook.com")
    login_info()
    post_link()
    driver.quit()

if __name__ == '__main__':
    main()