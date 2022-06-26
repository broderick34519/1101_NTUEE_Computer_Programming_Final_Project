# Code for borrowing bikes


def main():
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from selenium.webdriver.support.ui import Select
    import pandas as pd


    op = webdriver.ChromeOptions()
    op.add_argument('headless')


    user = input("Please enter your username. ")
    pw = input("Please enter your password. ")
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

    # Select bikeinstance
    bikeins = driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[1]/th/a')
    bikeins.click()

    soup = BeautifulSoup(driver.page_source, "html.parser")
    tags = soup.select('td')
    table = soup.find('table', {'id':'result_list'})
    head = [th.text.replace('\n','') for th in table.find('thead').find_all('th')][1:]
    trs  = [th.text.replace('\n','') for th in table.find('tbody').find_all('td')]
    name = [th.text.replace('\n','') for th in table.find('tbody').find_all('th')]

    row = list()
    length = len(trs) // 9
    for i in range(length):
        trs[9*i] = name[i]
        row.append(trs[9*i:9*i+9])
    df = pd.DataFrame(data=row, columns = head)
    print(df[['Bike','Bike model','Color', 'Owner', 'Status','Borrower','Card number', 'Due back']]) 
    
    number = int(input(f"Please enter the index of bike you want to rent(0 ~ {len(name)-1}). "))
    while number < 0 or number >= len(row) or row[number][4] != "Available":
        number = int(input(f"Invalid bicycles, Please enter the index of bike you want to rent(0 ~ {len(name)-1}). "))
    number += 1
    bike_model = driver.find_elements_by_xpath(f'//*[@id="result_list"]/tbody/tr[{number}]/th/a')
    # print(bike_model)
    bike_model[0].click() 

    status = Select(driver.find_element_by_name('status'))
    status.select_by_index(2) # Set On Loan
    due = driver.find_element_by_name('due_back')
    due.clear()
    due.send_keys('2022-02-21')


    borrower = Select(driver.find_element_by_name('borrower'))
    temp = [i.text for i in borrower.options]
    pos = temp.index(user)
    borrower.select_by_index(pos)
    
    with open('card_ID.txt', 'r') as f:
        card_num = f.read()
    card_ins = driver.find_element_by_xpath('//*[@id="id_Card_number"]')
    card_ins.send_keys(card_num)
    
    
    
    save = driver.find_element_by_xpath('//*[@id="bikeinstance_form"]/div/div/input[1]')
    save.click()

    # driver.close()
# main()
