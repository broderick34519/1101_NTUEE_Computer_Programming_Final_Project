# Code for creating bike



def main():
	from selenium import webdriver
	from bs4 import BeautifulSoup
	from selenium.webdriver.support.ui import Select
	import time
	op = webdriver.ChromeOptions()
	op.add_argument('headless')

	driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=op)
	#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver") 
	driver.get("http://127.0.0.1:8000/admin/")


	# Use admin account to login
	username =  driver.find_element_by_xpath('//*[@id="id_username"]')
	username.send_keys('admin')
	password = driver.find_element_by_name("password")
	password.send_keys('b07611008')
	login_button = driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input')
	login_button.click()

	add = driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[1]/td[1]/a')
	add.click()

	# Get bike brand
	print("="*50)
	brand = input("Please enter your bike brand. (Giant, Merida, Other)\n")
	while (brand != "Giant" and brand != "Merida" and brand != "Other"):
		brand = input("Invalid, Please enter your bike brand. (Giant, Merida, Other)\n")
	 
	bike = Select(driver.find_element_by_name('bike'))
	temp = [i.text for i in bike.options]
	pos = temp.index(brand)
	bike.select_by_index(pos) 

	# Enter bike model
	print("="*50)
	model = input("Please enter your bike model. (8 digits number)\n")
	bike_model = driver.find_element_by_xpath('//*[@id="id_bike_model"]')
	bike_model.send_keys(model)

	# Enter Color
	print("="*50)
	color = input("Please enter your bike color. \n")
	bike_color = driver.find_element_by_xpath('//*[@id="id_color"]')
	bike_color.send_keys(color)

	# Get owner
	print("="*50)
	owner = input("Please enter your name. \n")
	bike_owner = driver.find_element_by_xpath('//*[@id="id_owner"]')
	bike_owner.send_keys(owner)
	card_ins = driver.find_element_by_xpath('//*[@id="id_Card_number"]')
	temp = '0'
	card_ins.send_keys(temp)

	save = driver.find_element_by_xpath('//*[@id="bikeinstance_form"]/div/div/input[1]')
	save.click()
	time.sleep(1)
# main()
