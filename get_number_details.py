import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

user_numbers=input("enter your number:")

number=phonenumbers.parse(user_numbers)

user_carrier=carrier.name_for_number(number, "en")

user_geo = geocoder.description_for_number(number,"en")

print(f"your carrier is {user_carrier} and location is : {user_geo}")