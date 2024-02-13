import random


def randMassive(length):
    massive_person = []

    for i in range(int(length)):
        rand = random.uniform(65.0, 70.0)
        massive_person.append(round(rand, 2))

    return massive_person


def sumElements(massive):
    return round(sum(massive) / len(massive), 2)


def rand():
    person = input("Enter number of days: ")
    massive_one = randMassive(int(person))
    massive_two = randMassive(int(person))
    massive_three = randMassive(int(person))
    massive_sum = []

    massive_sum.append(sumElements(massive_one))
    massive_sum.append(sumElements(massive_two))
    massive_sum.append(sumElements(massive_three))

    print(f"Generated prices:\nExchange 1: {massive_one}\nExchange 2: {massive_two}\nExchange 3: {massive_three}\n")
    return print(f"Average price: {round(sum(massive_sum) / len(massive_sum), 5)}")


rand()