def continet(name):
    country=["USA","France","Italy","Germany","Nigeria","SA"]
    with open("countries.text","a") as file:
        if name not in country:
            file.write(name)
            return(f"this is {name}")

print(continet("brazil"))