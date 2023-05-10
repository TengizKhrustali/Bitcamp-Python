def main():
    x = input("please input fruit name: ").lower()
    fruits_and_calories = { "apple":130, "avocado":50, "banana": 110, "cantaloupe":50,"grapefruit":60, 
    "grapes":90, "kiwifruit":90, "lemon":15, "lime":20, "nectarine":60,
    "orange":80, "peach":60, "pear":100, "pineapple":50,"plums":70, 
    "sweet cherries" :100, "strawberries":50, "tangerine":50, "watermelon":8}

    if x in fruits_and_calories:
        print("Calories: " + str(fruits_and_calories[x]))


if __name__ == "__main__":
    main()
