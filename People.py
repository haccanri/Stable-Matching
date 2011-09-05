class Person:
  """A person object"""

  def __init__(self, name):
    self.name = name
    self.partner = None
    self.partner_preferences = None

  def __repr__(self):
    return self.name

  def get_partner_preferences(self):
    if self.partner_preferences == None :
      raise Exception("No preferences have been assigned yet")    
    return self._partner_preferences

  def set_partner_preferences(self, value):
    self._partner_preferences = value

class Man(Person):
  """A man object maintains an zerobased indexindex n of specifying he is on
  his nth choice fiance"""
  def __init__(self, name):
    Person.__init__(self, name)
    self.preference_index = 0

class Woman(Person):
  """A woman object has a reverse lookup dictionary of the 
  partner_preferences"""
  def __init__(self, name):
      Person.__init__(self, name)
      self.ranking = {}

  def assign_rankings(self):
    for rank in range(len(self.partner_preferences)):
      self.ranking[self.partner_preferences[rank]] = rank
