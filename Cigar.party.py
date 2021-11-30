def cigar_party(cigars, is_weekend):

    if is_weekend:
        print(40-60, True)
    else:
        print(cigar>60,False)

cigar:float = float(input("What is the amount of cigars:"))

def cigar_party(cigar, is_week):
    if (cigar<40):
        print(False)
    elif (cigar>=40):
        print(True)
    elif (cigar>60):
        print(False)

# # ground shipping
# if (weight == 2 or weight < 2 ):
#     cost_ground = weight * 1.75 + 20
#     print("Ground shipping: $", float(cost_ground))
# elif (weight > 2 or weight <= 6 ):
#     cost_ground=weight*3.50+20
#     print("Ground shipping: $", float(cost_ground))
# elif (weight > 6 or weight<= 10):
#     cost_ground=weight*4.50+20
#     print("Ground shipping: $", float(cost_ground))
# else: 
#     cost_ground=weight*5.25+20
#     print("Ground shipping: $", float(cost_ground))