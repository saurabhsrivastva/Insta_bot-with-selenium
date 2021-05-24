from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def login_insta(username, password):
    global driver
    driver=webdriver.Chrome(executable_path="/home/saurabh/Videos/chromedriver_linux64/chromedriver")
    driver.get("https://www.instagram.com/")
    print(driver.title)
    sleep(2)
    userid =driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    userid.send_keys(username)
    sleep(1)
    passid=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    passid.send_keys(password)
    sleep(4)
    
    
    
login_insta("ankitshr2021", "@Atul_402")

def login_button():
    login=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
    login.click()
    sleep(2)
    notsave=driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')[0]
    notsave.click()
    turnon=driver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')[0]
    turnon.click()
    

login_button()  

def searchit(find_ur_person):

    id_searching= driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    id_searching.send_keys(find_ur_person)
    sleep(1)

    rex=driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a/div')
    rex.click()
    sleep(2)
    
searchit('rex_srivastva')  


try:

 def follow():
    
    follow_button=driver.find_element_by_xpath('//button[contains(text(), "Follow")]')
    follow_button.click()
    sleep(1)

 follow()
except Exception:
 pass

def like(limit=3):
    like_button=driver.find_element_by_class_name('eLAPa')
    like_button.click()
    sleep(1)
    for i in range(limit):
        clicklike=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
        clicklike.click()
        nextimg=driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a")
        nextimg.click()
        sleep(2)


    
like()

   
    


  



