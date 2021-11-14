# Mobile Number Information Finder
# __by Akash
import phonenumbers
from phonenumbers import carrier, geocoder , timezone

mobilenumber = input("Enter Mobile number using Country code: ")
mobilenumber = phonenumbers.parse(mobilenumber)

print(timezone.time_zones_for_number(mobilenumber))

print(carrier.name_for_number(mobilenumber ,"en"))

print(geocoder.description_for_number(mobilenumber,"en"))

print("Valid Mobile Number",phonenumbers.is_valid_number(mobilenumber))

print("Checking possibility of Number: ", phonenumbers.is_possible_number(mobilenumber))


