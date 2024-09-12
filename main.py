# Imports simulation python files
import motion
import Space
# Asks and determines which program to run
x = 0
guesses = []
while True:
    i = input("1 or 2\ndo you want run the projectile motion simulator or the secret simulator?:\n")
    print()
    print()
    if i == "1":
        print()
        print()
        print()
        print()
        print()
        print()
        motion.projectile()
        break
    elif i == "2":
        # Password program to hide the secret program
        Password = "space"
        hint = 0
        while True:
            print("Guesses =", guesses)
            p = input("What is the password?:\n")
            print()
            print()
            # Stops it from being below or above five characters
            if len(p) < 5 or len(p) > 5:
                print("Must be 5 letters")
            if p != Password:
                # Once correct, it runs Space.space
                print("Incorrect")
                print()
                hint += 1
                guesses.insert(0, p)
            elif p == Password:
                print("Correct...")
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                Space.space()
                x = 1
                break
            if hint >= 4:
                # Prints a hint after too many incorrect guesses
                print("an empty room has a lot of...")
    else:
        print("Incorrect input")
        print("\n\n")
    if x == 1:
        break
w = "Willem Dennis Vanderploeg"
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Credits\n______________________________________________________________________________________________________")
print("\tConcept:", w)
print("\tResearch:", w)
print("\tLead:", w)
print("\tProgramming", w)
print("Book used to derive space.py: Vaughan, L. (2021). Real-world python a hacker's guide to solving problems with\n "
      "\tcode. No Starch Press, Inc. ")
