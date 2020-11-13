from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time
import pync
import os
import datetime

driver = webdriver.Chrome()
driver.get("https://www.bseindia.com/corporates/ann.html")
driver.find_element_by_xpath("//select[@id='ddlAnnType']/option[text()='Equity']").click()
driver.find_element_by_xpath("//select[@id='ddlPeriod']/option[text()='Result']").click()


stockEvent = open("stockEvent.txt","r") 
stocks = stockEvent.readlines()
resultsOut=[]

while True:

	for stock in stocks:
		securityName=stock

		#securityName = input("Enter the stock name: ")

		driver.find_element_by_xpath("//input[@id='scripsearchtxtbx']").clear()

		time.sleep(1)

		securityNameInput = driver.find_element_by_xpath("//input[@id='scripsearchtxtbx']")
		securityNameInput.send_keys(securityName)
		securityNameInput.submit()

		time.sleep(5)

		securityNameClick = driver.find_element_by_xpath("//ul[@id='ulSearchQuote2']").click()

		submit = driver.find_element_by_xpath("//input[@id='btnSubmit']").click()
		time.sleep(5)
		pdf = driver.find_elements_by_xpath("//td[@class='tdcolumngrey ng-scope']/a[@href]")
		if len(pdf) > 0:
			pync.notify(securityName +'\n'+ str(datetime.datetime.now().time()), title='Results!!!',sound="default",open=driver.find_element_by_xpath("//td[@class='tdcolumngrey ng-scope']/a").get_attribute('href'),appIcon="/Users/pranjal/Desktop/Stock/bse-logo.png")
			resultsOut.append(securityName)

	for results in resultsOut:
		stocks.remove(results)

file1.close()

