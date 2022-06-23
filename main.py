import random

def userChoice():
  user = input('Press [r] for a randomly generated password or [p] for a customized password : ')
  if user == 'r' or user == 'R':
    randomPasswordGenerator()
  elif user == 'p' or user == 'P':
    customizedPassword()
  else:
    print('Bruhh! why?')

def randomPasswordGenerator():
  x = 'abcdefghijtuvw567890!@#$xyzABCDEFGHIJKLMklmnopqrsNOPQRSTUVWXYZ1234%^&*'
  characters = list(x)
  res = random.choices(characters, k=9)
  print(''.join(res)) 

def customizedPassword():
  user_sma = int(input('How many small letters do you want in your password ? '))
  user_cap = int(input('How many capital letters do you want in your password ? '))
  user_num = int(input('How many numbers do you want in your password (1-9 only) ? '))
  user_spec = int(input('How many special characters do you want in your password ? '))
  sma = list('abcdefghijklmnopqrstuvwxyz')
  cap = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
  num = list('123456789')
  spe_cha = list('!@#$%^&*(){}[]?/><\|')
  res = random.choices(sma, k=user_sma)
  res_2 = random.choices(cap, k=user_cap)
  res_3 = random.choices(num, k=user_num)
  res_4 = random.choices(spe_cha, k=user_spec)
  final_pass = ''.join(res) + ''.join(res_2) + ''.join(res_3) + ''.join(res_4) 
  print('Your Password is : ')
  print(''.join(random.sample(final_pass, len(final_pass))))
   
userChoice()
