
# coding: utf-8

# In[3]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

chromedriver_path = 'C:/Users/dell/Downloads/chromedriver.exe' # Change this to your own chromedriver path
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(1)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(randint(2,6))

username = webdriver.find_element_by_name('username')
username.send_keys('username')
password = webdriver.find_element_by_name('password')
password.send_keys('password')
sleep(1) ##react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > button'

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > button')
button_login.click()
sleep(2)  #//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/button/div
           ##react-root > section > main > div > article > div > div:nth-child(1) > div > form > div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB > button > div


# In[6]:


hashtag_list = ['stoofvlees']


new_followed = []
tag = -1
followed = 0
likes = 0
comments = 0

for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(4)
    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
    
    first_thumbnail.click()
    sleep(randint(1,10))    
    try:        
        for x in range(5):
                  # Liking the picture
                    button = webdriver.find_element_by_css_selector("body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > span")
                    heart=button.click()
               

                    # Comments and tracker
                    webdriver.find_element_by_css_selector("body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span._15y0l > button > span").click()
                    comment_box = webdriver.find_element_by_css_selector("body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > textarea")
                    comment_box.send_keys('soul satisfying!')
                    
                    sleep(1)
                        
                        # Enter to post comment
                    text_enter=comment_box.send_keys(Keys.ENTER)
                    sleep(2)
                    
                    #follow :
                    follow = webdriver.find_element_by_css_selector("body > div._2dDPU.vCf6V > div.zZYga > div > article > header > div.o-MQd > div.PQo_0 > div.bY2yH > button")
                    follow.click()
                    sleep(2)
                    
                    

                # Next picture
                   
                    images_trial = webdriver.find_element_by_link_text('Next').click()
                    print("next image processing")
                    sleep(randint(2,5))
                   
                   # button_2=webdriver.find_element_by_css_selector("body > div._2dDPU.vCf6V > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > span")
                   # button_2.click()
                    
                    
               
        else:
                    webdriver.find_element_by_link_text('Next').click()
                
             
    # some hashtag stops refreshing photos (it may happen sometimes), it continues to the next
    except:
        continue

