def eat_lunch(lunchables):
    if not lunchables:
        print("My lunch is empty, and my parents are mean!")
    else:
        for index, food in enumerate(lunchables):
            if index == 0:
                print(f"First I eat {food}")
            elif index == len(lunchables) - 1:
                print(f"Finally I eat {food}")
            else:
                print(f"Next I eat {food}")

brownbag1 = ["a sandwich", "some takis", "some apple sauce", "a breath mint"]
brownbag2 = ["a pizza slice", "some dunkaroos", "some orange wedges"]
brownbag3 = []

print("brownbag 1:")
eat_lunch(brownbag1)

print("\nbrownbag 2:")
eat_lunch(brownbag2)

print("\nbrownbag 3:")
eat_lunch(brownbag3)
