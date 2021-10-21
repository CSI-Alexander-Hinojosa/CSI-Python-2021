print("Welcome to the simpson's shipping program")

weight:float = float(input("What is the weight of your packege:"))

# ground shipping
if (weight == 2 or weight < 2 ):
    cost_ground = weight * 1.75 + 20
    print("Ground shipping: $", float(cost_ground))
elif (weight > 2 or weight <= 6 ):
    cost_ground=weight*3.50+20
    print("Ground shipping: $", float(cost_ground))
elif (weight > 6 or weight<= 10):
    cost_ground=weight*4.50+20
    print("Ground shipping: $", float(cost_ground))
else: 
    cost_ground=weight*5.25+20
    print("Ground shipping: $", float(cost_ground))

# Courier shipping
if (weight==2 or weight < 2 ):
    cost_courier = weight*3.50+5
    print("Courier shipping: $", float(cost_courier))
elif (weight > 2 or weight<= 6):
    cost_courier=weight*7.00+8
    print("Courier shipping: $", float(cost_courier))
elif (weight > 6 or weight<= 10):
    cost_courier=weight*9.00+12
    print("Courier shipping: $", float(cost_courier))
else:
    (weight > 10 )
    cost_courier=weight*10.50+15
    print("Courier shipping: $", float(cost_courier))


# Drone shipping
if (weight==2 or weight < 2 ):
    cost_drone = weight*5.25+0.00
    print("Drone shipping: $", float(cost_drone))
elif (weight > 2 or weight<= 6):
    cost_drone=weight*10.50+0.00
    print("Drone shipping: $", float(cost_drone))
elif (weight > 6 or weight<= 10):
    cost_drone=weight*13.50+0.00
    print("Drone shipping: $", float(cost_drone))
else:
    (weight > 10 )
    cost_drone=weight*15.75+0.00
    print("Drone shipping: $", float(cost_drone))

print("Ground premiun charge=$150")