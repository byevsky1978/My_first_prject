cities = ["Lod", "Holon", "Rome", "London", "Paris", "Barcelona", "Moscow"]
max = 0
for city in cities:
    print(city)
    l = len(city)
    if l > max:
        max = l
        index = cities.index(city)
print(max)
print(cities[index])

cities.append("Madrid") # add Madrid t cities
cities.insert(3, "Petach Tikva")


