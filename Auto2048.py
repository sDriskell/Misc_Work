"""
Automated Tool that plays 2048 game to demonstrate passing keystrokes
using Selenium: https://play2048.co/

Requires geckodriver to added to your PATH.

"""
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "https://play2048.co/"


def auto_input(browser: webdriver.Firefox) -> int:
    """Uses Selenium webdriver to manipulate inputs into browser game to simulate
    one or more games of 2048 for user."""
    html = browser.find_element_by_tag_name('html')
    retry_button = browser.find_element_by_class_name("retry-button")
    new_game_button = browser.find_element_by_class_name("restart-button")

    while True and not retry_button.is_displayed():
        html.send_keys(Keys.UP)
        html.send_keys(Keys.DOWN)
        html.send_keys(Keys.LEFT)
        html.send_keys(Keys.RIGHT)

    score = browser.find_element_by_class_name("score-container").text
    retry_button.click()
    new_game_button.click()
    return int(score)


def graph_results(total_score: list):
    """Visualize scores from total_score list in different forms of graphs"""
    plt.plot(total_score, 'ro')
    plt.xlabel('Game Number')
    plt.ylabel('Score')
    plt.show()


def main():
    browser = webdriver.Firefox()
    browser.get(URL)

    total_score = []
    games = int(input("How many times do you want to play? "))
    for i in range(0, games):
        total_score.append(auto_input(browser))
    graph_results(total_score)


if __name__ == '__main__':
    main()
