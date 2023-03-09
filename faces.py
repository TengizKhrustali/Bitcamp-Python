# This program converts emoticons to emojis
def main():
    x = str(input("Please input emoticon: "))
    x = convert(x)
    print(x)


def convert(x):
    x=x.replace(":)", "🙂")
    x=x.replace(":(", "🙁")
    return x


main()
