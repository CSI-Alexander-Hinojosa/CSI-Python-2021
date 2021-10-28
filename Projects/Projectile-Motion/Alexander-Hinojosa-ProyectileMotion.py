import math
# gun= "AS VAL"
# caliber= "9x39mm"
# ammunition= "9x39mm SSP gs"
# velocity_ms= 310

# Building= "Ocean Tower"
# BuildingHeight= 243

# gravity_Ms = 9.81

def ProyectileFunction(gun:str, caliber:str, ammunition:str, velocity_ms:int, Building:str, BuildingHeight:str, gravity_Ms:int):
    time_s= math.sqrt(2*BuildingHeight/gravity_Ms)
    distance= (velocity_ms*gravity_Ms)
    print(f"The gun selected for the experiment is {gun}. The caliber of {gun} is {caliber} ")

ProyectileFunction("AS VAL", "9x39mm", "9x39mm SSP gs", 310, "Ocean Tower", 243, 9.81)