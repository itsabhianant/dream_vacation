def ask(content: str, choices: list, not_enter_content=None) -> str:
    """Ask a question

    If it asks the question stored in the content argument and the answer is other than the choices argument, print the not_enter_content argument and ask the question again
    """
    answer = input(content)

    if answer in choices:
        return answer
    elif not_enter_content:
        print(not_enter_content)
    return ask(content, choices, not_enter_content)


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
    