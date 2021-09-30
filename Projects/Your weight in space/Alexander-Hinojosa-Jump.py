# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
# g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

# print("Caculator of weight in diferent planets")

# myweight = int(input("What is your weight in pounds?"))
# myplanet = input(f"Select the planet you want to calculate the weight: {planets}")

# def calculateWeight(planet, Mass):
#     print(f"Earth mass in pounds is: {Mass}")

#     w_kg = Mass / 2.2046
#     print(f"Mass in kg: {w_kg}") 

#     n_lb = 4.45

#     planet_index = planets.index(planet)
#     print(f"weight in {planets[planet_index]} is {(w_kg * g_ms2[planet_index]) / n_lb} lb")

# calculateWeight(myplanet, myweight)

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
rel_gravity = [2.65, 1.11, 1, 2.64, 0.40, 0.94, 1.13, 0.88]

print("Jumping on other planets")

myjump=float(input("What is the distance of your jump in Earth [meters]?"))
myplanet=input(f"Select the planet you want to calculate the jump:{planets}")

def calculatejump(planet, distance):
    print(f"Earth gravity in meters is: {distance}")

    planet_index = planets.index(planet)
    print(f"jump in {planets[planet_index]} is {(myjump * rel_gravity[planet_index])} m")

calculatejump(myplanet, myjump)





