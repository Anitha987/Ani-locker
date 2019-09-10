import address
import pyperclip
class Credential:
  """
  create a class credential  to hold our user accounts
  """
  credential_list=[]
  def __init__(self,username,email,password,account):
    """
    _init_method will help us by the time  we want to use initialise all our objects 
    Args:
    """
    self.username=username
    self.email=email
    self.password =password
    self.account=account
  def save_credential(self):
      '''
      save credential method will help us to save credential objects into credential-list
      '''
      Credential.credential_list.append(self)
  def delete_credential(self):
      '''
      delete_credential method deletes a saved credential in case we want to remove one from our credential_list
      '''
      Credential.credential_list.remove(self)
  @classmethod
  def find_by_email(cls,email):
    '''
    method that takes in an email and returns a credential that matches that email.

    Args:
      email:email to search for
    Returns: 
      address of person that  matches the email
    '''
    for credential in cls.credential_list:
      if credential.email==email:
        return credential         
  @classmethod
  def credential_exist(cls,email):
    '''
    Method that checks if our entered email exists from the  credential list.
    Args:
        email:email to search if it exists
    Returns:
      Boolean:True or false depending if the credential provided exists
    '''
    for credential in cls.credential_list:
      if credential.email==email:
        return True
    return False  
  @classmethod
  def display_credential(cls):
    '''
    method that returns our credential list
    '''
    return cls.credential_list
  @classmethod
  def copy_email(cls,email):
    email_found=Credential.find_by_email(email)
    pyperclip.copy(email_found.email)
  @classmethod  
  def check(cls,username,password):
    current=''

    for credential in Credential.credential_list:    
      if (credential.username == log_username and credential.password == log_pass):
        current=credential.username
    return current
                