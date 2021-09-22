# length=int(input("What is the length of the rectangular prism?"))
# widht=int(input("What is the widht of the rectangular prism?"))
# height=int(input("What is the height of the rectangular prism?"))
# print("The volume of the rectangular prims is:",length*widht*height)

# def volumeofrectangularprism(length, widht, height):
#     print(f"Volume of the rectangular prism {int(length)*int(widht)*int(height)}") 
#     print("length is 32cm")
#     print("widht is 25cm")
#     print("height is 15cm")
#     volumeofrectangularprism(32, 25, 15)

print("Welcome to In The Heights")
print("The cost of the each seat is as follow: Arena: $75.00, Nivel Principal: $40.00, Club seat: $40.00")

Arena=int(input("How many tickets would you buy for Arena seats?"))
NivelPrincipal=int(input("How many tickets would you buy for Nivel Principal seats?"))
Clubseat=int(input("How many tickets would you buy for Club seats?"))
print("The total amounth of tickets is:",Arena+NivelPrincipal+Clubseat)

def totalcostoftickets(Arena,NivelPrincipal,Clubseat):
    print(f"The cost for Arena tickets is:{int(Arena)*75}")
    print(f"The cost for NivelPrincipal tickets is:{int(NivelPrincipal)*75}")
    print(f"The cost for Clubseat tickets is:{int(Clubseat)*75}")
print()
Sectionsales=(Arena, NivelPrincipal, Clubseat)
Sales_An=Arena*75
Sales_NP=NivelPrincipal*40
Sales_CS=Clubseat*40
def totalcostoftickets(Sales_An, Sales_NP, SalesCS):
    print(f"The total cost of the tickets is: ${int(Sales_An)+ int(Sales_NP)+ int(Sales_CS)}") 
print() 
totalcostoftickets(Sales_An, Sales_NP, Sales_CS)