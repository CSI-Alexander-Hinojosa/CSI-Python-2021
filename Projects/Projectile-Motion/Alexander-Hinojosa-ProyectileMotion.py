import math
from ExperimentalData import ExperimentalData 

from pathlib import Path 
import json
import os

# gun= "AS VAL"
# caliber= "9x39mm"
# ammunition= "9x39mm SS5 gs"
# velocity_ms= 900

# Building= "Ocean Tower"
# BuildingHeight= 243

# gravity_Ms = 9.81


def ProyectileFunction(experimentalData:ExperimentalData):
    time_s = math.sqrt ((2*experimentalData.BuildingHeight) / experimentalData.gravity_Ms)
    distance= (experimentalData.velocity_ms*time_s)
    #  distance= (experimentalData[velocity_ms]*gravity_Ms)

    print(f"The gun selected for the experiment is {experimentalData.gun}. The caliber of {experimentalData.caliber} is {experimentalData.caliber}. The building that the proyectile ")

print("Welcome to the proyectile motion analisis. On this file, it would calculate the motion of the proyectile from a weapon. The weapom selected is the {experimentalData.gun}, with an ammunition of {experimentalData.ammunition} with a velocity of {experimentalData.velocity.Ms}. The proyectile is going to be expelled from the Ocean Tower from a height of 243ft.")

# experimentalData object was made from the variables of the experiment. 
# experimentalData= {

#  "gun": "AS VAL",
# "caliber": "9x39mm",
# "ammunition": "9x39mm SS5 gs",
# "velocity_ms": 900,

# "Building": "Ocean Tower",
# "BuildingHeight": 243,

# "gravity_Ms": 9.81

# }
experimentalData=ExperimentalData("AS VAL", "9x39mm", "9x39mm SS5 gs", 310, "Ocean Tower", 243, 9.81)

myDataSet= [
ExperimentalData("AS VAL", "9x39mm", "9x39mm SS5 gs", 900, "Ocean Tower", 243, 9.81),
ExperimentalData("AS VAL", "9x39mm", "9x39mm SS5 gs", 900, "Nacional plaza", 238, 9.81),
ExperimentalData("MP5", "9x19mm", "9x19mm Parabellum", 800, "Ocean Tower", 243, 9.81),
ExperimentalData("MP5", "9x19mm", "9x19mm Parabellum", 800, "Nacional plaza", 238, 9.81)


]
for data in myDataSet:
    print("\n----------------------------------------------------------------------\n")
    ProyectileFunction(data)

# Serialization
myOutputPath= Path(__file__).parents[0]
myOutputFilePath= os.path.join(myOutputPath, "Projectile-Motion.json")

with open(myOutputPath,"W") as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)
    # json.dump(myDataSet[0].__dict__, outfile)
# ProyectileFunction(experimentalData)