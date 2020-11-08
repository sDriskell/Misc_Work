"""Automated Tool that plays 2048 game to demonstrate passing keystrokes
using Selenium: https://play2048.co/"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#TODO: write function for inputing keystrokes
#TODO: check to see if game is over
#TODO: start new game if game is over
#TODO: track high score

def main():
    url = "https://play2048.co/"

    browser = webdriver.Firefox()
    browser.get(url)

    html = browser.find_element_by_tag_name('html')
    while True:
        html.send_keys(Keys.UP)
        html.send_keys(Keys.DOWN)
        html.send_keys(Keys.LEFT)
        html.send_keys(Keys.RIGHT)


if __name__ == '__main__':
    main()
