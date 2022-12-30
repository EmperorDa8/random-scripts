def continet(name):
    country = ["USA", "France", "Italy", "Germany", "Nigeria", "SA"]
    with open("countries.text", "a") as file:
        if name not in country:
            file.write(name)
            return f" {name} is not part of listed countries"
        else:
            return f" {name} is part of listed countries"


#print(continet("brazil"))
