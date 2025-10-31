countries = input().split(", ")
capitals = input().split(", ")

dict = dict(zip(countries, capitals))

for country, capital in dict.items():
    print(f"{country} -> {capital}")