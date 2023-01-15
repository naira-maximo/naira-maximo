# E. palindrome
# Verifique se uma string é palíndrome
#   palindrome('asa') True
#   palindrome('casa') False 
def palindrome(s):
  if len(s) == 3:
    if s[0] == s[-1]:
      print(True)
    else:
      print(False)
  elif len(s) == 5:
    if s[0] == s[-1] and s[1] == s[-2]:
      print(True)
    else:
      print(False)
  elif len(s) == 7:
    if s[0] == s[-1] and s[1] == s[-2] and s[2] == s[-3]:
      print(True)
    else:
      print(False)
  elif len(s) == 9:
    if s[0] == s[-1] and s[1] == s[-2] and s[2] == s[-3] and s[3] == s[-4]:
      print(True)
    else:
      print(False)
  elif len(s) == 11:
    if s[0] == s[-1] and s[1] == s[-2] and s[2] == s[-3] and s[3] == s[-4] and s[4] == s[-5]:
      print(True)
    else:
      print(False)
  else:
    print(False)
  return print

palindrome('asa')
palindrome('omississimo')
palindrome('casa')
palindrome('galinha')
palindrome('carro')
