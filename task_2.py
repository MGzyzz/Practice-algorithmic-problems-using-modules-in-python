def pyramid():
    person = input("Input pyramid height:\n")

    for i in range(1, int(person)+1):
        spaces = (int(person) - i) * ' '
        result = '*' * i + (i-1) * '*'
        print(f"{spaces}{result}")

def rhombus():
    person = input("Input rhombus height:\n")

    for i in range(1, int(person)+1):
        spaces = (int(person) - i) * ' '
        result = '*' * i + (i-1) * '*'
        print(f"{spaces}{result}")

    for i in reversed(range(1,int(person))):
        spaces = (int(person) - i ) * ' '
        result = '*' * i + (i-1) * "*"
        print(f"{spaces}{result}")


def main_menu():
    choose = input("What do you want to generate? The selection is made using the indices below:\n[1] Pyramid \n[2] Rhombus\n")
    match choose:
        case "1":
            pyramid()
        case "2":
            rhombus()
        case _:
            print("Invalid command. Please try again")


main_menu()

