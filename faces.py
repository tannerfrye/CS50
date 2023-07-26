

#create convert
def convert(x ="world :("):
    x = x.replace(":)", "\U0001F642")
    x = x.replace(":(", "\U0001F641")
    print(x)

#create main


main = input("What would you like to say? ")



#show main to user
convert(main)
