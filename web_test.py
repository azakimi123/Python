from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# calculated = input("Enter the calculated ip: ")
# port = input("Enter port number: ")

browser = webdriver.Chrome('/Users/aaronzakimi/Desktop/AZ-Dev/February 2021/Python Learning/chromedriver')



browser.get("https://www.google.com/")
# browser.get("{calculated}{port}")

browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("pizza recipe")
browser.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/center/input[1]').click()
# element_to_hover_over = browser.find_element_by_xpath("/html/body/nav/div[2]/div[2]/nav/div[4]/div/div[2]")

# hover = ActionChains(browser).move_to_element(element_to_hover_over)
# hover.perform()
# time.sleep(2)
# browser.find_element_by_xpath("/html/body/nav/div[2]/div[2]/nav/div[4]/nav/div/div/div[3]/a").click()
# time.sleep(2)
# browser.find_element_by_xpath("/html/body/section[3]/div/div/div/div/div/div/div[1]/ul/li[10]/ul/li/a").click()