# -*- coding: utf-8 -*-
"""
Created on 2018-05-15
@author: lenovo
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


# 用id等待文字的出现，使用场景：切换页面出现某个字符串
def wait_text_by_id(self, id_name, text):
    driver = self.driver
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.text_to_be_present_in_element((By.ID, id_name), text))


# 用xpath等待文字的出现，使用场景：切换页面出现某个字符串
def wait_text_by_xpath(self, xpath, text):
    driver = self.driver
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.text_to_be_present_in_element((By.XPATH, xpath), text))


# 用id等待element的出现，使用场景：切换页面出现某个element
def wait_visibility_of_any_elements_by_id(self, idname):
    driver = self.driver
    wait = WebDriverWait(driver, 30)
    wait.until(expected_conditions.visibility_of_any_elements_located((By.ID, idname)))


# 用xpath等待element的出现，使用场景：切换页面出现某个element
def wait_visibility_of_any_elements_by_xpath(self, xpath):
    driver = self.driver
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.visibility_of_any_elements_located((By.XPATH, xpath)))


# 用id等待element的消失，使用场景：切换页面消失某个element
def wait_invisibility_of_element_by_id(self, idname):
    driver = self.driver
    wait = WebDriverWait(driver, 30)
    wait.until(expected_conditions.invisibility_of_element_located((By.ID, idname)))


# 用xpath等待element的消失，使用场景：切换页面消失某个element
def wait_invisibility_of_element_by_xpath(self, xpath):
    driver = self.driver
    wait = WebDriverWait(driver, 30)
    wait.until(expected_conditions.invisibility_of_element_located((By.XPATH, xpath)))

