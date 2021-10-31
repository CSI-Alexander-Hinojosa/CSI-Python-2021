import math
# gun= "AS VAL"
# caliber= "9x39mm"
# ammunition= "9x39mm SSP gs"
# velocity_ms= 310

# Building= "Ocean Tower"
# BuildingHeight= 243

# gravity_Ms = 9.81

print("Welcome to the proyectile motion analisis. On this file, it would calculate the motion of the proyectile from a weapon. The weapom selected is the AS VAL, with an ammunition of 9x39mm SSP gs with a velocity of 310. The proyectile is going to be expelled from the Ocean Tower from a height of 243ft.")

def ProyectileFunction(gun:str, caliber:str, ammunition:str, velocity_ms:int, Building:str, BuildingHeight:str, gravity_Ms:int):
    time_s= math.sqrt(2*BuildingHeight/gravity_Ms)
    distance= (velocity_ms*gravity_Ms)
    print(f"The gun selected for the experiment is {gun}. The caliber of {gun} is {caliber} ")

ProyectileFunction("AS VAL", "9x39mm", "9x39mm SSP gs", 310, "Ocean Tower", 243, 9.81)
