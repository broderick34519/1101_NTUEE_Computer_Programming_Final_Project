# Code for creating user
def check_username(s):
    if len(s) > 150:
        return False
        
    # Check if input only contain letters, digits, @, ., +, -, _
    available_list = [43, 45, 46] + list(range(48, 58, 1)) + [64] + list(range(65, 91, 1)) + [95] + list(range(97, 123, 1))
    # print(available_list)
    
    for char in s:
        if ord(char) not in available_list:
            return False
    
    return True
            
def check_passwd(password, username):
    if password == username:
        return False
    if len(password) < 8:
        return False
    if password.isdigit():
        return False
    
    return True
    
def main():
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from selenium.webdriver.support.ui import Select


    op = webdriver.ChromeOptions()
    op.add_argument('headless')

    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=op)
    # driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver") 
    driver.get("http://127.0.0.1:8000/admin/")


    # Use admin account to login
    username =  driver.find_element_by_xpath('//*[@id="id_username"]')
    username.send_keys('admin')
    password = driver.find_element_by_name("password")
    password.send_keys('b07611008')
    login_button = driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/input')
    login_button.click()

    add = driver.find_element_by_xpath('//*[@id="content-main"]/div[1]/table/tbody/tr[2]/td[1]/a')
    add.click()

    # username
    print("="*50)
    user = input("Please enter your username. \n Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. \n")
    while not check_username(user):
        user = input("Invalid, Please enter your username. \n Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only. \n")
    user_input = driver.find_element_by_xpath('//*[@id="id_username"]')
    user_input.send_keys(user)
    print("="*50)
    # password
    pw = input("Please enter your password. \n Your password can't be too similar to your other personal information. \nYour password must contain at least 8 characters.\nYour password can't be a commonly used password.Your password can\'t be entirely numeric.\n")
    while not check_passwd(pw, user):
        pw = input("Invalid, Please enter your password. \n Your password can't be too similar to your other personal information. \nYour password must contain at least 8 characters.\nYour password can't be a commonly used password.Your password can\'t be entirely numeric.\n")
    pw_input = driver.find_element_by_xpath('//*[@id="id_password1"]')
    pw_input.send_keys(pw)
    print("="*50)
    # password confirmation
    pwc = input("Enter the same password as before, for verification.\n")
    while pwc != pw:
        print("Your password is not the same as before.\n")
        pwc = input("Enter the same password as before, for verification.\n")
    pwc_input = driver.find_element_by_xpath('//*[@id="id_password2"]')
    pwc_input.send_keys(pwc)

    save = driver.find_element_by_xpath('//*[@id="user_form"]/div/div/input[1]')
    save.click()

