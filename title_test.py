import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class OLXSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:/selenium/chromedriver.exe")

    def test_search_in_olx(self):
        driver = self.driver
        driver.implicitly_wait(5)
        driver.get("https://www.olx.pl")
        self.assertIn("Ogłoszenia", driver.title)
        element = driver.find_element(By.ID, "headerSearch")
        element.send_keys("samochud")
        element.send_keys(Keys.RETURN)
        curr_title = driver.title
        exp_title = "Samochud - OLX.pl"
        self.assertEqual(curr_title, exp_title)

    def TearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
