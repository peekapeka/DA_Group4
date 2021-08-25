import unittest
import os

class WebReference(unittest.TestCase):
    def test(self):
        os.system("C:\\Users\\dexia\\PycharmProjects\\DA_Group4\\DA_Group4\\DA_Group4\\spiders\\Browser.py")
        os.system("C:\\Users\\dexia\\PycharmProjects\\DA_Group4\\DA_Group4\\DA_Group4\\spiders\\main.py")
        os.system("C:\\Users\\dexia\\PycharmProjects\\DA_Group4\\DA_Group4\\DA_Group4\\spiders\\images.py")

    if __name__ == "__main__":
        unittest.main()
