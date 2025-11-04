import random as rd 
print("====================")
print(" rock paper scissors")
print("====================")

print("1 for rock")
print("2 for paper")
print("3 for scissors")
player= int(input("pick a number: "))
computer= rd.randint(1,3)

print("you chose: ",player)
print("cpu chose: ",computer)

if player==1 and computer==3:
  print("you win")
elif player==2 and computer==1:
  print("you win")
elif player==3 and computer==2:
  print("you win")
elif player==computer:
  print("tie")
else:
  print("you lose")