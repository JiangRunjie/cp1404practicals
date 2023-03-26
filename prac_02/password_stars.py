PASSWORD_LENGTH = 8


def main():
    password = get_password()
    print("Password:", len(password) * "*")


def get_password():
    prompt = input(str("Password:"))
    while len(prompt) < PASSWORD_LENGTH:
        print("At least 8 characters.")
        prompt = input(str("Password:"))
    else:
        return prompt


main()
