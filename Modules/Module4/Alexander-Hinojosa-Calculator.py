# print("Hello World")
# print(input("What is your name?"))
# Myname=input()
# print("It is good to meet you", Myname)
# print("What is your age?")
# myAge=input()
# print("you would be" +str(myAge)+5)+"in 5 years"

print("Volume of a rectangular prism")
print ("""
  _________________________
  I     I           I     I
  I     I           I     I
  I_____I___________I_____I

""")
length=int(input("What is the length of the rectangular prism?"))
widht=int(input("What is the widht of the rectangular prism?"))
height=int(input("What is the height of the rectangular prism?"))
print("The volume of the rectangular prims is:",length*widht*height)

def volumeofrectangularprism(length, widht, height):
    print(f"Volume of the rectangular prism {int(length)*int(widht)*int(height)}") 
    print("length is 32cm")
    print("widht is 25cm")
    print("height is 15cm")
    volumeofrectangularprism(32, 25, 15)