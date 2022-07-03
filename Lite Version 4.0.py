#(CC) Attribution-NonCommercial 4.0 International SOME RIGHTS RESERVED ODYSSEUS ABRAHAM KIRIKOPOULOS 2022
print("Party A (1) | Party B (2) | Party C (3)\n")
party_a = 0
party_b = 0
party_c = 0
option = ''
while(option != '/d'):
	option = input("Vote: ")
	if(option == '1'):
		party_a += 1
		print("\nRegistered\n")
	if(option == '2'):
		party_b += 1
		print("\nRegistered\n")
	if(option == '3'):
		party_c += 1
		print("\nRegistered\n")
print(f"\nParty A: {party_a} | Party B: {party_b} | Party C: {party_c}")
input()
