class UI:
    def displayMenu(self):
        print("""
    Choose an option
1.Add a number. The number is read from the console.
2.Display the list of numbers.
3.Filter the list so that it contains only the numbers between two indices.
4.Undo 
5.Exit""")

    def inputMenuOption(self):
        INVALID_OPTION = -1
        try:
            option = int(input("> "))
            if option < 1 or option > 5:
                print("Select a valid option")
                return INVALID_OPTION
            return option
        except ValueError:
            print("Select a valid option")
            return INVALID_OPTION


    def inputComplexNumber(self):
        option = input("Insert complex number (a+bi): ")
        return option

    def displayMessage(self, message):
        print(message)


