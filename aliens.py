dream_vacations = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    vacation = input("\nWhere would you like to go for your vacation? ")
     
    dream_vacations[name] = vacation

    repeat = input("\nWould you like to share this with your friend/friends? (yes/no): ")
    if repeat == 'no':
        polling_active = False

print("---Poll Results---")
for name, vacation in dream_vacations.items():
    print(name.title() + " would like to go " + vacation.title() + " for vacation.")
    