from django.test import TestCase

# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.
class ShowAttendanceTest(LiveServerTestCase):

  def test(self):
    driver.close()
    driver = webdriver.Chrome(executable_path=r"/Users/nadiahansen/SkoleProtocol/venv/chromedriver")
    #Choose your url to visit
    driver.get('http://127.0.0.1:8000/attendancecode/showattendance/')
    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(5) # gives an implicit wait for 20 seconds
    #find the elements you need to submit form

    username = driver.find_element_by_id('id_username')
    password = driver.find_element_by_id('id_password')
    login = driver.find_element_by_id("login")

    username.send_keys('andrea44')
    password.send_keys('Mor12345')

    login.send_keys(Keys.RETURN)
    
    driver.implicitly_wait(3)
    
    class_name = driver.find_element_by_name('class')
    subject_name = driver.find_element_by_name('subject')

    submit = driver.find_element_by_name('submit')

    #populate the form with data
    class_name.send_keys('SDi21')
    subject_name.send_keys('Testing')
 

    #submit form
    submit.send_keys(Keys.RETURN)

  driver.close()
    #check result; page source looks at entire html document
    # assert 'SDi21' in selenium.page_source