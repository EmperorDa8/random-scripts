from selenium import webdriver

url = "https://web.whatsapp.com/"
driverpath = "Downloads//chromedriver.exe"
dr = webdriver.Chrome(driverpath)
dr.get(url)


def message_chat():
    # this function will recieve input for name and messsage to send

    name = input("enter your name")
    message = input("enter your chat")
    count = int(input("enter no of count to send the chat :"))

    recieve = dr.find_element_by_xpath('//span@[title - "{}"]'.format(name)).click()

    text_input = dr.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')

    for m in range(count):
        text_input.send_keys(message)
        butn_send = dr.find_element_by_class_name('_4sWnG').click()


def nn():
    print("do you want send the chat ?")
    ask = input("press y for yes or n for no!")
    if ask == "y":
        message_chat()
        nn()
    elif ask == "no":
        print("ok thank you!")
    else:
        print("pls enter valid request:\n")
        nn()


nn()
