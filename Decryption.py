# Programmed by: Lee Anne Y. Angeles

while True:
    # Input statement
    string = input("\nEnter a string to decrypt: ")

    # Used replace() method to change character '*' to 'a'
    str1 = string.replace('*', 'a')
    # Used replace() method to change character '&' to 'e'
    str2 = str1.replace('&', 'e')
    # Used replace() method to change character '#' to 'e'
    str3 = str2.replace('#', 'i')
    # Used replace() method to change character '+' to 'o
    str4 = str3.replace('+', 'o')
    # Used replace() method to change character '!' to 'u
    str5 = str4.replace('!', 'u')

    # Output statement
    print("The Plain Text:", str5.capitalize())

    try_again = input("\nWould you like to try again? [ y / n ] : ").lower()
    if try_again.lower() == 'y':
        continue
    else:
        print("\nThank you for using this program!\nGoodbye!")
        break


