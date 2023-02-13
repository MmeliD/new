my_number = 42
your_geuss = 0
while (your_geuss != my_number):
    your_input = input("Geuss my number: ")
    your_geuss = int(your_input)
    if your_geuss < my_number:
        print("guess higher")
    elif your_geuss>my_number:
        print("geuss lower")
    else:
        print("You got it!")
