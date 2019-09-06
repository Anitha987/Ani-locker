import pyperclip
import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
  """
  Test class that defines test cases for  the credential class behaviours
  Args:
      unittest.TestCase:TestCase class that helps in creating test cases
  """
  def setUp(self):
    """ 
    this setUp method will be run after each test cases.
    """
    self.new_credential= Credential("Anitha987","anithaumuhire@gmail.com","kigali555","twitter")
  def test_init (self):
    """
    test_init testcase to test if the objects are initialised properly
    """
    self.assertEqual(self.new_credential.username,"Anitha987")
    self.assertEqual(self.new_credential.email,"anithaumuhire@gmail.com")
    self.assertEqual(self.new_credential.password,"kigali555")
    self.assertEqual(self.new_credential.account,"twitter")
  def test_save_credential(self):
      '''
      test_save_credential test case to test if the credential act object is saved into the credential_list
      '''
      self.new_credential.save_credential()
      self.assertEqual(len(Credential.credential_list),1) 
  def tearDown(self):
      '''tearDown method will help us to clean up once  each test has been run
      '''
      Credential.credential_list=[]   
  def test_save_multiple_credential(self):
    '''
    test_save_multiple_credential to check if we can save multiple credential objects to our credential_list
    '''
    self.new_credential.save_credential()   
    test_credential=Credential("Ronah","ronah@gmail.com","ronah123","instagram")
    test_credential.save_credential()
    self.assertEqual(len(Credential.credential_list),2) 
  def test_find_credential(self):
      '''
      test_find_address help to testif we want to search one of our information
      '''
      self.new_credential.save_credential()
      test_credential=Credential("Ronah","ronah@gmail.com","ronah123","instagram")
      test_credential.save_credential()
      found_credential = Credential.find_by_email("ronah@gmail.com")
      self.assertEqual(found_credential.email,test_credential.email) 
  def test_credential_exists(self):
    '''
    test and see bty the time our address is not found to return a boolean.
    '''
    self.new_credential.save_credential
    test_credential=Credential("Ronah","ronah@gmail.com","ronah123","instagram")
    test_credential.save_credential()
    credential_exists=Credential.credential_exist("ronah@gmail.com")
    self.assertTrue(credential_exists) 
  def test_copy_email(self):
    '''
    Test to confirm that we are copying the email address  from a found address  
    '''
    self.new_credential.save_credential()
    Credential.copy_email("anithaumuhire@gmail.com")
    self.assertEqual(self.new_credential.email,pyperclip.paste())   

if __name__ == '__main__':
    unittest.main()

         