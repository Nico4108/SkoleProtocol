from random import random
from django.test import TestCase

# Create your tests here.
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import time, unittest
from random import randrange

# Create your tests here.
class ShowAttendanceTest(LiveServerTestCase, unittest.TestCase):

  att_code = randrange(500000)
  att_code2 = randrange(500000)
  # Create Attendance Code
  def test1(self):
    driver = webdriver.Chrome(executable_path=r"/Users/nicspiegelhauer/Documents/Skole/6. Semester SD/Testing/SkoleProtocol/venv/chromedriver")
    #Choose your url to visit
    driver.get('http://127.0.0.1:8000/accounts/login/')
    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(5) # gives an implicit wait for 5 seconds
    #find the elements you need to submit form

    username = driver.find_element_by_id('id_username')
    password = driver.find_element_by_id('id_password')
    login = driver.find_element_by_id("login")

    username.send_keys('andrea44')
    password.send_keys('Mor12345')

    self.assertIsNotNone(username, 'No Username input')
    self.assertIsNotNone(password, 'No Password input')    

    driver.implicitly_wait(3)
    time.sleep(1.5)
    login.send_keys(Keys.RETURN)
    
    driver.implicitly_wait(3)

    create_code = driver.find_element_by_id('id_cc')
    create_code.send_keys(Keys.RETURN)

    code = driver.find_element_by_id('id_code')
    keaclass = driver.find_element_by_id('id_keaclass')
    subject = driver.find_element_by_id("id_subject")

    code.send_keys(self.att_code)
    keaclass.send_keys('SDi21')
    subject.send_keys('Testing')
    time.sleep(1.5)
    submit = driver.find_element_by_id('submit')
    submit.send_keys(Keys.RETURN)

    code_registered = driver.find_element_by_id('code_registered').text
    correct_str = 'code registered'
    
    if self.assertEquals(code_registered, correct_str) is None:
      print('Attendance Code Registered test passed:', self.assertEquals(code_registered, correct_str) is None)
      time.sleep(1.5)
    driver.close()
    
  # Student login and registre attencdance code
  def test2(self):
    driver = webdriver.Chrome(executable_path=r"/Users/nicspiegelhauer/Documents/Skole/6. Semester SD/Testing/SkoleProtocol/venv/chromedriver")
    #Choose your url to visit
    driver.get('http://127.0.0.1:8000/accounts/login/')
    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(3) # gives an implicit wait for 3 seconds
    #find the elements you need to submit form

    username = driver.find_element_by_id('id_username')
    password = driver.find_element_by_id('id_password')
    login = driver.find_element_by_id("login")

    username.send_keys('nadi6548')
    password.send_keys('Mor12345')
    time.sleep(1.5)

    self.assertIsNotNone(username, 'No Username input')
    self.assertIsNotNone(password, 'No Password input')    

    driver.implicitly_wait(3)
    login.send_keys(Keys.RETURN)
    
    driver.implicitly_wait(3)
    
    submit = driver.find_element_by_id('create log')
    submit.send_keys(Keys.RETURN)

    id_ac = driver.find_element_by_id('id_attendanceCode')
    id_kc = driver.find_element_by_id('id_keaclass')
    id_sub = driver.find_element_by_id('id_subject')

    id_ac.send_keys(1)
    id_kc.send_keys('SDi21')
    id_sub.send_keys('Testing')
    time.sleep(1.5)
    
    self.assertIsNotNone(id_ac, 'No Attendance Code input')
    self.assertIsNotNone(id_kc, 'No Class input')
    self.assertIsNotNone(id_sub, 'No Subject input')
    
    submitt = driver.find_element_by_id('submit')
    submitt.send_keys(Keys.RETURN)

    driver.implicitly_wait(3)

    er = driver.find_element_by_id('error').text
    correct_str = 'heeeeej du forkert på den'
    
    if self.assertEquals(er, correct_str) is None:
      print('Wrong attendance code test passed: ', self.assertEquals(er, correct_str) is None)
      back = driver.find_element_by_id('Go Back')
      time.sleep(1.5)
      back.send_keys(Keys.RETURN)

      id_ac = driver.find_element_by_id('id_attendanceCode')
      id_kc = driver.find_element_by_id('id_keaclass')
      id_sub = driver.find_element_by_id('id_subject')

      id_ac.send_keys(self.att_code)
      id_kc.send_keys('SDi21')
      id_sub.send_keys('Testing')
      time.sleep(3)
      
      self.assertIsNotNone(id_ac, 'No Attendance Code input')
      self.assertIsNotNone(id_kc, 'No Class input')
      self.assertIsNotNone(id_sub, 'No Subject input')
      
      submitt = driver.find_element_by_id('submit')
      submitt.send_keys(Keys.RETURN)
      
      time.sleep(1.5)
      correct = driver.find_element_by_id('reg_ok').text
      correct_str = 'you been registered'
      print('Student registered corret code test passed: ', self.assertTrue(correct, correct_str) is None)

      driver.close() 

  # Attendance overview
  def test3(self):
      driver = webdriver.Chrome(executable_path=r"/Users/nicspiegelhauer/Documents/Skole/6. Semester SD/Testing/SkoleProtocol/venv/chromedriver")
      #Choose your url to visit
      driver.get('http://127.0.0.1:8000/attendancecode/showattendance/')
      driver.maximize_window() # For maximizing window
      driver.implicitly_wait(3) # gives an implicit wait for 5 seconds
      #find the elements you need to submit form

      username = driver.find_element_by_id('id_username')
      password = driver.find_element_by_id('id_password')
      login = driver.find_element_by_id("login")

      username.send_keys('Thea')
      password.send_keys('1234!')
      driver.implicitly_wait(3)
      time.sleep(1.5)
      login.send_keys(Keys.RETURN)

      driver.implicitly_wait(3)
      
      class_name = driver.find_element_by_name('class')
      subject_name = driver.find_element_by_name('subject')

      submit = driver.find_element_by_name('submit')
      
      class_name.clear()
      subject_name.clear()
      class_name.send_keys('SDi21')
      subject_name.send_keys('Testing')
      time.sleep(1.5)
      #submit form
      submit.send_keys(Keys.RETURN)

      stud_text = driver.find_element_by_id('students')
      corret_text = 'Studens'
      print('Show attendans list test passed: ', self.assertTrue(stud_text, corret_text) is None)
      time.sleep(3)
      driver.close()
  
  # Login test
  def test4(self):
      driver = webdriver.Chrome(executable_path=r"/Users/nicspiegelhauer/Documents/Skole/6. Semester SD/Testing/SkoleProtocol/venv/chromedriver")
      #Choose your url to visit
      driver.get('http://127.0.0.1:8000/accounts/login/')
      driver.maximize_window() # For maximizing window
      driver.implicitly_wait(3) # gives an implicit wait for 5 seconds
      #find the elements you need to submit for

      username_teacher = driver.find_element_by_id('id_username')
      password_teacher = driver.find_element_by_id('id_password')
      login_teacher = driver.find_element_by_id("login")

      username_teacher.send_keys('andrea44')
      password_teacher.send_keys('Far12345') # wrong
      login_teacher.send_keys(Keys.RETURN)

      testsucces = driver.find_element_by_id('login_text').text
      loginfail = 'Log In'
      print('Test for invalid teacher input passed: ', self.assertTrue(testsucces, loginfail) is None)

      username_new_teacher = driver.find_element_by_id('id_username')
      password_new_teacher = driver.find_element_by_id('id_password')
      login_new_teacher = driver.find_element_by_id("login")

      username_new_teacher.clear()
      password_new_teacher.clear()
      username_new_teacher.send_keys('andrea44')
      password_new_teacher.send_keys('Mor12345')
      login_new_teacher.send_keys(Keys.RETURN)

      login_suc = driver.find_element_by_id('choices').text
      login_suc_text = 'Choices'
      print('Test for valid teacher input passed: ', self.assertTrue(login_suc, login_suc_text) is None)
      
      if self.assertTrue(login_suc, login_suc_text) is None:
          print('Teacher is in')
          time.sleep(1)
          logout = driver.find_element_by_id("logout")
          logout.send_keys(Keys.RETURN)
      else:
        print('error')
      
      username_student = driver.find_element_by_id('id_username')
      password_student = driver.find_element_by_id('id_password')
      login_student = driver.find_element_by_id("login")

      username_student.send_keys('nadi6548')
      password_student.send_keys('Far12345') # wrong
      login_student.send_keys(Keys.RETURN)

      testsucces = driver.find_element_by_id('login_text').text
      loginfail = 'Log In'
      print('Test for invalid student input passed: ', self.assertTrue(testsucces, loginfail) is None)

      username_new_student = driver.find_element_by_id('id_username')
      password_new_student = driver.find_element_by_id('id_password')
      login_new_student = driver.find_element_by_id("login")

      username_new_student.clear()
      password_new_student.clear()
      username_new_student.send_keys('nadi6548') # correct
      password_new_student.send_keys('Mor12345')
      login_new_student.send_keys(Keys.RETURN)

      login_suc = driver.find_element_by_id('choices').text
      login_suc_text = 'Choices'
      print('Test for valid student input passed: ', self.assertTrue(login_suc, login_suc_text) is None)
      
      if self.assertTrue(login_suc, login_suc_text) is None:
          print('Student is in')
          time.sleep(1)
          logout = driver.find_element_by_id("logout")
          logout.send_keys(Keys.RETURN)
          time.sleep(1)
      else:
        print('error')
      
      driver.close()

  # Attendance code test
  def test5(self):
    driver = webdriver.Chrome(executable_path=r"/Users/nicspiegelhauer/Documents/Skole/6. Semester SD/Testing/SkoleProtocol/venv/chromedriver")
    #Choose your url to visit
    driver.get('http://127.0.0.1:8000/accounts/login/')
    driver.maximize_window() # For maximizing window
    driver.implicitly_wait(5) # gives an implicit wait for 5 seconds
    #find the elements you need to submit form

    username = driver.find_element_by_id('id_username')
    password = driver.find_element_by_id('id_password')
    login = driver.find_element_by_id("login")

    username.send_keys('andrea44')
    password.send_keys('Mor12345')

    self.assertIsNotNone(username, 'No Username input')
    self.assertIsNotNone(password, 'No Password input')    

    driver.implicitly_wait(3)
    time.sleep(1.5)
    login.send_keys(Keys.RETURN)
    
    driver.implicitly_wait(3)

    create_code = driver.find_element_by_id('id_cc')
    create_code.send_keys(Keys.RETURN)

    code = driver.find_element_by_id('id_code')
    keaclass = driver.find_element_by_id('id_keaclass')
    subject = driver.find_element_by_id("id_subject")

    code.send_keys(9101010101010)
    keaclass.send_keys('SDi21')
    subject.send_keys('Testing')
    submit = driver.find_element_by_id('submit')
    time.sleep(1.5)
    submit.send_keys(Keys.RETURN)

    chech_text = driver.find_element_by_id('create att code').text
    correct_str = 'Create attendance code'
    
    if self.assertEquals(chech_text, correct_str) is None:
      print('Attendance Code too long test passed: ', self.assertEquals(chech_text, correct_str) is None)
      time.sleep(1)

    code_new1= driver.find_element_by_id('id_code')
    keaclass_new1 = driver.find_element_by_id('id_keaclass')
    subject_new1 = driver.find_element_by_id("id_subject")

    code_new1.clear()
    code_new1.send_keys(self.att_code2)
    keaclass_new1.send_keys('SDi21')
    subject_new1.send_keys('Testing')

    submit = driver.find_element_by_id('submit')
    time.sleep(1.5)
    submit.send_keys(Keys.RETURN)

    code_registered = driver.find_element_by_id('code_registered').text
    correct_str = 'code registered'
    
    if self.assertEquals(code_registered, correct_str) is None:
      print('Correct Attendance Code Registered test passed: ', self.assertEquals(code_registered, correct_str) is None)
      time.sleep(1.5)

    logout = driver.find_element_by_id("logout")
    logout.send_keys(Keys.RETURN)
    time.sleep(1.5)
    
    username_new2 = driver.find_element_by_id('id_username')
    password_new2 = driver.find_element_by_id('id_password')
    login_new2 = driver.find_element_by_id("login")

    username_new2.send_keys('andrea44')
    password_new2.send_keys('Mor12345')

    self.assertIsNotNone(username_new2, 'No Username input')
    self.assertIsNotNone(password_new2, 'No Password input')    

    driver.implicitly_wait(3)
    time.sleep(1.5)
    login_new2.send_keys(Keys.RETURN)
    
    driver.implicitly_wait(3)

    create_code_new2 = driver.find_element_by_id('id_cc')
    create_code_new2.send_keys(Keys.RETURN)

    code_new2 = driver.find_element_by_id('id_code')
    keaclass_new2 = driver.find_element_by_id('id_keaclass')
    subject_new2 = driver.find_element_by_id("id_subject")

    code_new2.send_keys(self.att_code2)
    keaclass_new2.send_keys('')
    subject_new2.send_keys('Testing')
    time.sleep(1.5)
    submit_new2 = driver.find_element_by_id('submit')
    submit_new2.send_keys(Keys.RETURN)

    chech_text_new2 = driver.find_element_by_id('create att code').text
    correct_str_new2 = 'Create attendance code'
    
    if self.assertEquals(chech_text_new2, correct_str_new2) is None:
      print('Attendance Code wrong class test passed: ', self.assertEquals(chech_text_new2, correct_str_new2) is None)
      time.sleep(1.5)
      logout = driver.find_element_by_id("logout")
      logout.send_keys(Keys.RETURN)
      time.sleep(1.5)

    username_new3 = driver.find_element_by_id('id_username')
    password_new3 = driver.find_element_by_id('id_password')
    login_new3 = driver.find_element_by_id("login")

    username_new3.send_keys('andrea44')
    password_new3.send_keys('Mor12345')

    self.assertIsNotNone(username_new3, 'No Username input')
    self.assertIsNotNone(password_new3, 'No Password input')    

    driver.implicitly_wait(3)
    time.sleep(1.5)
    login_new3.send_keys(Keys.RETURN)
    
    driver.implicitly_wait(3)

    create_code_new3 = driver.find_element_by_id('id_cc')
    create_code_new3.send_keys(Keys.RETURN)

    code_new3 = driver.find_element_by_id('id_code')
    keaclass_new3 = driver.find_element_by_id('id_keaclass')
    subject_new3 = driver.find_element_by_id("id_subject")

    code_new3.send_keys(self.att_code)
    keaclass_new3.send_keys('SDi21')
    subject_new3.send_keys('')
    time.sleep(1.5)
    submit_new3 = driver.find_element_by_id('submit')
    submit_new3.send_keys(Keys.RETURN)

    chech_text_new3 = driver.find_element_by_id('create att code').text
    correct_str_new3 = 'Create attendance code'
    
    if self.assertEquals(chech_text_new3, correct_str_new3) is None:
      print('Attendance Code wrong subject test passed: ', self.assertEquals(chech_text_new3, correct_str_new3) is None)
      time.sleep(1.5)
      logout = driver.find_element_by_id("logout")
      logout.send_keys(Keys.RETURN)
      time.sleep(1.5)

    driver.close()

if __name__ == '__main__':
      unittest.main()