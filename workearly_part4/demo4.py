import unittest
from lib2to3.pgen2 import driver

import self as self
from selenium import webdriver
from webdriver_manager.Chrome import ChromeDriverManager


class python_Test(unittest.TestCase):
    def pysearch(self):
        self.driver=webdriver.chrome(ChromeDriverManager().install())

    def search_test(self):
        driver = self(self.driver)





driver.get("https://www.python.org")

self.assetIn("python",driver.title)
