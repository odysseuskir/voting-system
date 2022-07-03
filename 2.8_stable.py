'''
Author: Odysseus-Abraham Kirikopoulos
(CC) Attribution-NonCommercial 4.0 International - SOME RIGHTS RESERVED - ODYSSEUS ABRAHAM KIRIKOPOULOS - 2022
Version: 2.8 Stable
WARRNING: The following programm was created for educational purpuses
'''

#Variables

party_a = 0
party_b = 0
party_c = 0
ttl_votes = 0
option = 'null'
authentic_copy = False
correct_votes = False

#Startup
print("Lanching...\n")
print("Author: Odysseus-Abraham Kirikopoulos")
print("(CC) Attribution-NonCommercial 4.0 International - SOME RIGHTS RESERVED - ODYSSEUS ABRAHAM KIRIKOPOULOS - 2022")
print("Build Version: 2.8 Stable\n")

#Greet & List
print("Welcome to the Voting System.\n")
while(authentic_copy == False):
    authetication = input("\nPlease enter the election center authetication code: ")
    if(authetication == 'demo'):
        print('\nYou have successfuly signed in.')
        authentic_copy = True
    else:
        print('\nFailed to autheticate. Try again.')

print("\nParty list:\n\nParty A (Code: 1)\nParty B (Code: 2)\nParty C (Code: 3)\n\nTo exit submitions type /d\n")

while(option != '/d'):
    
    #Vote

    option = input("Enter vote: ")

    #Counting Votes

    if(option == "1"):
        party_a += 1
        ttl_votes += 1
        print("\nYour vote has been registered\n")
    elif(option == "2"):
        party_b += 1
        ttl_votes += 1
        print("\nYour vote has been registered\n")
    elif(option == "3"):
        party_c += 1
        ttl_votes += 1
        print("\nYour vote has been registered\n")
    elif(option == '/d'):
        break
    else:
        print("Error: Unknown party")

#Percentage calculation

if(ttl_votes > 1):
    party_a_percentage = (party_a / ttl_votes) * 100
    party_b_percentage = (party_b / ttl_votes) * 100
    party_c_percentage = (party_c / ttl_votes) * 100
else:
    party_a_percentage = 0
    party_b_percentage = 0
    party_c_percentage = 0

#Vote counter

print(f"\nParty A has: {party_a} votes and {party_a_percentage}%\n")
print(f"Party B has: {party_b} votes and {party_b_percentage}%\n")
print(f"Party C has: {party_c} votes and {party_c_percentage}%\n")
if(party_a > party_b and party_c):
    print("\nParty A has the most votes")
elif(party_b > party_a and party_c):
    print("\nParty B has the most votes")
elif(party_c > party_b and party_a):
    print("\nParty C has the most votes")
elif(party_a == party_b == party_c):
    print("\nAll parties have equal votes")

input('\n\nPress any key to exit\n')