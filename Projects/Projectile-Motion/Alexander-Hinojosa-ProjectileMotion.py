import math
from ExperimentalData import ExperimentalData 
import os
from pathlib import Path 
import json

# defining ProyectileFunction
def ProyectileFunction(experimentalData:ExperimentalData):

# experimentalData object was made from the variables of the experiment. 
# experimentalData= {

#  "gun": "AS VAL",
# "caliber": "9x39mm",
# "ammunition": "9x39mm SS5 gs",
# "velocity_ms": 900,

# "Building": "Ocean Tower",
# "BuildingHeight": 243,

# "gravity_Ms": 9.81
# Planets and gravities
# }

# planet with gravities list
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    g_ms = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

    planet= planets.index(experimentalData.planet)

# time and distance calculation
    time_s = math.sqrt ((2*experimentalData.BuildingHeight) / g_ms[planet])
    distance_m= (experimentalData.velocity_ms*time_s)
    #  distance= (experimentalData[velocity_ms]*gravity_Ms)

    # Descriptive Paragraph
    print(f"The gun selected for the experiment is {experimentalData.gun}. The caliber of {experimentalData.caliber}. With an ammunition {experimentalData.ammunition}, with the velocity of {experimentalData.velocity_ms}. The building that the proyectile is being fired from is {experimentalData.Building}, with an altitude of {experimentalData.BuildingHeight}, and would have a duration of {time_s}. The projectile would go through a velocity of {distance_m}. The shoot would be fired in {experimentalData.planet}, possessing a gravity of {g_ms[planet]}.")


# Original Variable
# experimentalData=ExperimentalData("AS VAL", "9x39mm", "9x39mm SS5 gs", 310, "Ocean Tower", 243, 9.81)

# My variations
myDataSet= [
ExperimentalData("AS VAL", "9x39mm", "9x39mm SS5 gs", 900, "Ocean Tower", 243, "Earth"),
ExperimentalData("AS VAL", "9x39mm", "9x39mm SS5 gs", 900, "Nacional plaza", 238, "Mars"),
ExperimentalData("MP5", "9x19mm", "9x19mm Parabellum", 800, "Ocean Tower", 243, "Earth"),
ExperimentalData("MP5", "9x19mm", "9x19mm Parabellum", 800, "Nacional plaza", 238, "Mars")

]

# for data in myDataSet:

#     print("\n----------------------------------------------------------------------\n")
#     ProyectileFunction(data)

# Dataset
for data in myDataSet:
    print("\n----------------------------------------------------------------------\n")
    ProyectileFunction(data)


# Serialization
myOutputPath= Path(__file__).parents[0]
myOutputFilePath= os.path.join(myOutputPath, "Projectile-Motion.json")

print(myOutputPath)

with open(myOutputPath,'w') as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)

# Deserialization
deserialize=open(myOutputPath)
experimentJson= json.load(deserialize)

for e in experimentJson:
    print("\n-------------------------------------------------\n")
    ProyectileFunction(ExperimentalData(**e))

# for e in experimentJson:
#     ExperimentalData(**e).run()

    # json.dump(myDataSet[0].__dict__, outfile)
# ProyectileFunction(experimentalData)

