print("====================")
print(" Area calculator 📐")
print("====================")

print("1)Triangle")
print("2)Rectangle")
print("3)Square")
print("4)Circle")
print("5)Quit")
num= int(input("which shape: "))

if num==1:
  height= int(input("height: "))
  base= int(input("base: "))
  area1=((height)*(base))/2
  print("the area is: ", area1)

elif num==2:
  length= int(input("length: "))
  width= int(input("width: "))
  area2=length*width
  print("the area is: ", area2)

elif num==3:
  side= int(input("side: "))
  area3=side**2
  print("the area is: ", area3)

elif num==4:
  radius= int(input("radius: "))
  area4=3.14159*(radius**2) # Changed π to 3.14159
  print("the area is: ", area4)

else:
  print("goodbye")

