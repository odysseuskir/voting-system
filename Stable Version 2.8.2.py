'''
Author: Odysseus-Abraham Kirikopoulos
License: GNU General Public License v3.0
Version: 2.8.2 Stable
WARNING: The following programm was created for educational purpuses
'''

startup = """
  Lanching...
  Author: Odysseus-Abraham Kirikopoulos
  License: GNU General Public License v3.0
  Build Version: 2.8.2 Stable

  Welcome to the Voting System.
"""
#Variables
parties = [0, 0, 0];
ttl_votes = 0
option = 'null'
authentic_copy = False

#Startup
print(startup)

while(!authentic_copy):
    authetication = input("\nPlease enter the election center authetication code: ")
    if(authetication == 'demo'):
        print('\nYou have successfuly signed in.')
        authentic_copy = True
    else:
        print('\nFailed to autheticate. Try again.')

print("\nParty list:\n\nParty A (Code: 1)\nParty B (Code: 2)\nParty C (Code: 3)\n\nTo exit submitions type /d\n")

while(True):
    #Vote
    option = input("Enter vote: ")
    if(option == '/d'):
        break

    #Counting Votes
    if(option in ['1', '2', '3']):
        parties[int(option) - 1] += 1;
        ttl_votes += 1
        print("\nYour vote has been registered\n")
    else:
        print("Error: Unknown party")

party_a_percentage = 0
party_b_percentage = 0
party_c_percentage = 0
#Percentage calculation
if(ttl_votes > 1):
    party_a_percentage = (parties[0] / ttl_votes) * 100
    party_b_percentage = (parties[1] / ttl_votes) * 100
    party_c_percentage = (parties[2] / ttl_votes) * 100

#Vote counter
print(f"\nParty A has: {parties[0]} votes and {party_a_percentage}%\n")
print(f"Party B has: {parties[1]} votes and {party_b_percentage}%\n")
print(f"Party C has: {parties[2]} votes and {party_c_percentage}%\n")
if(parties[0] == parties[1] and parties[1] == parties[2]):
    print("\nAll parties have equal votes")
else:
    most_votes_index = parties.index(max(parties))
    print(f"\nParty {'ABC'[most_votes_index]} has the most votes")

input('\n\nPress any key to exit\n')
