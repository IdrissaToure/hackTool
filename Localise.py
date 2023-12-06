import phonenumbers
from phonenumbers import gecoder

#Trouver le pays numéro
num ="+22377849399"
monNum = phonenumbers.parse(num)
localisation= gecoder.description_for_number(monNum,"ml")
print(Localisation)
