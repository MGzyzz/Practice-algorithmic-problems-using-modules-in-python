
def find_words():
    enter_one = input("Enter 2 sentences:\n1) ").split()
    enter_two = input("2) ").split()
    list_one = []
    list_two = []

    for i in enter_one:
        if i.isalpha() or i.isspace():
            list_one.append(i.capitalize())
    for i in enter_two:
        if i.isalpha() or i.isspace():
            list_two.append(i.capitalize())

    list_one = set(' '.join(list_one).split())
    list_two = set(' '.join(list_two).split())
    result = (list_one.intersection(list_two))

    return print("Similar words are:", ", ".join(sorted(result, reverse=True)))


find_words()

