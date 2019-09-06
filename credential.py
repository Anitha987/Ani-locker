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
