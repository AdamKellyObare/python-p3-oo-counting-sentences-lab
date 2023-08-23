#!/usr/bin/env python3

class MyString:
  pass
  def __init__(self, value=''):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")
      self.value = ""
      
  def is_sentence(self):
    return self.value.endswith('.')
  
  def is_question(self):
    return self.value.endswith('?')
  
  def is_exclamation(self):
    return self.value.endswith('!')
  
  def count_sentences(self):
        sentences = re.split(r'[.!?]+', self._value)
        # Exclude empty strings from the count
        return len([sentence for sentence in sentences if sentence])  



