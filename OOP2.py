class Smartphone:
    def __init__(self, company, model, size, colour, os):
        self.company = company
        self.model = model
        self.size = size
        self.colour = colour
        self.os = os

    def __str__(self):
         return f"this smartphone of {self.model} was made by {self.company} of {self.size} ,{self.colour} and {self.os}"


iphone = Smartphone("apple", "11", "6_inches", "ash", "mac-os")

nokia = Smartphone("Nokia.inc", "2.4", "6_inches", "black", "andriod-one")
print(nokia)
print(iphone)