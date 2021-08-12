import checkBox

#creating a diary-file
try:
    quit_f = "not"
    f = open("diary.txt", "r")
    print(f.read())

    while quit_f != "poka":
        f = open("diary.txt", "a")
        quit_f = input()
        f.write(quit_f)
        f.write("\n")

    if (checkBox.isAlone("diary.txt")):
        print("Do you need help?")

except:
    print("It seems that you do not possess a required diary-file. Please reload the program in order to read/write data")
    f = open("diary.txt", "w")
    f.write("Please, type 'poka' in order to exit the file  ")
    f.write("\n")
    f. close()

#TODO: how to work with spreadshit
