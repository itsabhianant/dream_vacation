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


def ask_share_friend() -> str:
    question_content = "\nWould you like to share this with your friend/friends? (y/n): "
    not_enter_content = "You have to enter either yes or no."

    yes_choices = ["y"]
    no_choices = ["n"]

    choices = yes_choices + no_choices

    answer = ask(question_content, choices, not_enter_content)

    if answer in yes_choices:
        return True
    else:
        return False


dream_vacations = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    vacation = input("\nWhere would you like to go for your vacation? ")
     
    dream_vacations[name] = vacation

    repeat = ask_share_friend()
    if not repeat:
        polling_active = False

print("---Poll Results---")
for name, vacation in dream_vacations.items():
    print(name.title() + " would like to go " + vacation.title() + " for vacation.")
    