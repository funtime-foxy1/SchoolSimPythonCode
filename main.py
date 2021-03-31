import time

print('You start walking to school')
time.sleep(1)
print('You forget what class number you go in. You know it has to be one of these: 142, 147, 165')
ForgetNumber = int(input('type a number visable: '))
if ForgetNumber == 142:
  print('You walk in and dont recognise your teacher.')
  exit()
if ForgetNumber == 147:
  print('Yes! The correct class. You sit at your seat.')
  continue1 = int(input('type 1 to continue: '))
  if continue1 == 1:
    time.sleep(2)
    print('Ding dong! Wow, that was quick! Time to go home!')
    time.sleep(1)
    print('Hello! it me funtime foxy. so, this was a short game i did in school for recess. Hope you liked this little game! This game will not end intil you end it. :) bye!')
if ForgetNumber == 165:
  print('You walk in and dont recognise your teacher.')
  exit()
