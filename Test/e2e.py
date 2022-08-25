from selenium import webdriver
import requests


# Grabbing the chromedriver in order to do tests
my_driver = webdriver.Chrome(executable_path="c:/Users/User/Desktop/study/chromedriver.exe")
requests.get("http://localhost:30000")
score = my_driver.find_element(by="id", value="score").text


def test_scores_service():
    if 1 < int(score) > 100:
        print("Works good")
        return True
    else:
        print("Works bad")
        return False


def main_functions():
    test_scores_service()
    if test_scores_service() == False:
        exit(-1)
    else:
        exit(0)
