from selenium import webdriver
from selenium.webdriver.common.by import By
import requests


# Grabbing the chromedriver in order to do tests

def test_scores_service():
    my_driver = webdriver.Chrome(executable_path="C:/Users/User/Desktop/study/chromedriver.exe")
    my_driver.get("http://127.0.0.1:30000/")
    score_element = int(my_driver.find_element(by="id", value="score"))
    if 1000 >= score_element >= 1:
        return True
    else:
        return False


def main_functions():
    test_scores_service()
    if test_scores_service() == False:
        exit(-1)
    else:
        exit(0)


test_scores_service()
main_functions()
