# CS61002: Algorithms and Programming 1
# Name: Matt Gates
# Date: 7/1/17
# Lab5.py

# Fun colors to print in terminal with
class c:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

errorMessage = "You haven't chosen a valid selection."
allowedCharacters = set("atcg")
inputChoices = ["a", "d", "s", "q"]
question = """What do you want to do:
        {}] add indel
        {}] delete indel
        {}] score
        {}] quit
""".format(inputChoices[0], inputChoices[1], inputChoices[2], inputChoices[3])

def askForChoice():
    while True:
        choice = input(question)
        if choice not in inputChoices or len(choice) < 1:
            print ("\n" + c.FAIL + "Error: " + c.ENDC + errorMessage + "\n")
        else :
            return choice

def askForString(nth):
    while True:
        inputString = input("Enter the {} string: ".format(nth)).lower()
        if not set(inputString) <= allowedCharacters or len(inputString) < 1:
            print ("")
            print (c.FAIL + "Error: " + c.ENDC + "Please only use characters a, t, c, or g")
            print ("")
        else:
            return inputString

def selectString() :
    while True:
        string = input("String 1 or String 2? ")
        if string not in ["1", "2"]:
            print ("")
            print (c.FAIL + "Error: " + c.ENDC + errorMessage)
            print ("")
        else:
            return int(string) - 1

def selectIndex(isDelete, string) :
    message = "Delete the indel at which index? " if isDelete else "Add the indel before which index? "
    while True:
        index = input(message)
        if not index.isdigit() or int(index) < 0 or (int(index)) > len(strings[string]) :
            print ("\n" + c.FAIL + "Error: " + c.ENDC + errorMessage + "\n")
        else :
            # Check that the index has an indel for deletes only
            if isDelete and strings[string][int(index)] != "-":
                print ("\n" + c.FAIL + "Error: " + c.ENDC + "Selected index is not an indel." + "\n")
                return False
            return int(index)

print ("")
print ("")
print (c.OKBLUE + "+++++++++++++++++++Exercise 1+++++++++++++++++++" + c.ENDC)
print ("")
print ("")

strings = [askForString("first"), askForString("second")]

print ("")
print ("[String 1] {}".format(strings[0]))
print ("[String 2] {}".format(strings[1]))
print ("")

# Perpetual loop until a valid choice is given
while True:
    choice = askForChoice()

    # Quit
    if choice == inputChoices[3]:
        print("\nTerminating program...")
        exit()

    # Add
    elif choice == inputChoices[0]:
        string = selectString()
        index = selectIndex(False, string)
        print(index)

        if type(index) != bool:
            strings[string] = strings[string][:index] + '-' + strings[string][index:]
            print("\n" + strings[string] + "\n")

    # Delete
    elif choice == inputChoices[1]:
        string = selectString()
        index = selectIndex(True, string)

        if type(index) != bool:
            strings[string] = strings[string][:index] + strings[string][index + 1:]
            print("\n" + strings[string] + "\n")

    # Score
    elif choice == inputChoices[2]:
        print ("SCORE")
