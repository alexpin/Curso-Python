def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()
    return string == string[::-1]
    # string va a ser igual a string al reve.., retorna true or false


def run():
    print(is_palindrome(1000))


if __name__ == '__main__':
    run()

