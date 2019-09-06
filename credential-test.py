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
if __name__ == '__main__':
    unittest.main()

         