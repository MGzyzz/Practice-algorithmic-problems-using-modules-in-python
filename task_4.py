def product():
    items = ['Milk', 'Bread', 'Cheese', 'Chocolate', 'Water']

    prices = [10, 5, 20.5, 7.15, 2.99]

    dictionary = []
    print(f"{'Name':<20}{'Price':>6}")
    for i, j in zip(items, prices):
        print(f"{i:<20}{'{:.2f}'.format(j):>6}")


product()


