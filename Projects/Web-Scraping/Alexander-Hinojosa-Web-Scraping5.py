import requests
import bs4
# Chicago Heights, Illinois

website = requests.get("https://forecast.weather.gov/MapClick.php?lat=41.50730000000004&lon=-87.63386499999996#.Yks1OSjMLIV")
forecast = bs4.BeautifulSoup(website.content, "html.parser")
sevenDay = forecast.find(id="seven-day-forecast")
forecast_items= sevenDay.find_all (class_="tombstone-container")
tonight = forecast_items[1]
# print(tonight.prettify())

period= tonight.find(class_="period-name").get_text()
print(period)

short_des= tonight.find(class_="short-desc").get_text()
print(short_des)

temp= tonight.find(class_="temp temp-low").get_text()
print(temp)