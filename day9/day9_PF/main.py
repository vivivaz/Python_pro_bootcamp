#HINT: You can call clear() to clear the output in the console.
import os
from art import logo

def clear():
    os.system( 'cls' )

print(logo)
print("Welcome!")
continius_leilao = True
participants_leilao = {}

while continius_leilao:
    nome = input("what is your name? ")
    bid = int(input("what is your bid? $"))
    participants_leilao[nome] = bid
    more_bidders = input("Are there any other bidders? Tipe 'yes' or 'no'.\n")
    clear()
    if more_bidders == "no":
        continius_leilao = False

biggest_bid = 0
key = "null"       
for participant in participants_leilao:
    if participants_leilao[participant] > biggest_bid:
        biggest_bid = participants_leilao[participant]
        key = participant

print(f"the winner is {key} with a bid of {biggest_bid}.")
