import unnitest
from credential import credential

class TestCredential(unnitest.TestCase):
  """
  Test class that defines test cases for  the credential class behaviours
  Args:
      unittest.TestCase:TestCase class that helps in creating test cases
  """
  def setUp(self):
      """ 
      this setUp method will be run after each test cases.
      """
      self.new_credential=Credential("Anitha987","anithaumuhire@gmail.com","kigali555","twitter")