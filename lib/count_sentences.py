#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    # self.value = None
    self.value = value
  def get_value(self):
    return self._value
  def set_value(self, new_value):
    if type(new_value)==str:
      self._value = new_value
    else:
      print("The value must be a string.")
  value = property(get_value, set_value)
  def is_sentence(self):
        if self._value and self._value.endswith('.'):
            return True
        return False

  def is_question(self):
      if self._value and self._value.endswith('?'):
          return True
      return False

  def is_exclamation(self):
        if self._value and self._value.endswith('!'):
            return True
        return False
  def count_sentences(self):
   limiters=[".","!","?"]
   sentence=self._value.split(' ')
   return len([s for s in sentence if s and any(s.endswith(d)for d in limiters)])
    
pass
