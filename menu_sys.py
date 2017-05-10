"""."""


def menu():
    """."""
    correct_input = False
    while not correct_input:
        print("1. Name of mentors")
        print("2. Nickname of Miskolc mentors")
        print("3. Carol's full name and phone number (applicant)")
        print("4. Full name and phone number of applicant, who went to Adipiscingenimmi University")
        print("5. New applicant: Markus Schaffarzyk")
        print("6. Chage phone number of Jemima Foreman (applicant)")
        print("7. Delete applicants who got funded (from existence, for an eternity MUWHAHAHAHA!)")
        print("0. Exit program\n")
        user_input = input("Please select a querry: ")
        if user_input not in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            print("Incorrect input!\n")
            continue
        print()
        correct_input = True
    if user_input == "0":
        return False
    return user_input
