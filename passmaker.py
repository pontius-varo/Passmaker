import library, random

class Passmaker:

    #Constructor converts the string given by the user into a list.
    def __init__(self, word):
        self._pass = list(word)
        self.char_add()

    #This method assigns random characters and numbers to the list
    def char_add(self):

        z = 0
        #A while loop to do the following 4 times.(as the number of characters & numbers should not exceed 8 in total)
        while z < 2:
            u = random.randrange(len(library.numbers))
            self._pass.append(library.numbers[u])
            e = random.randrange(len(library.specialchar))
            self._pass.append(library.specialchar[e])
            z += 1

    def scram(self):
        #This method scrambles the userlist (called _pass) and adds it to a new string.
        random.shuffle(self._pass)
        newpass = " "
        return self.remove(newpass.join(self._pass))

    #This method removes the spaces in the newly created string.
    def remove(self, string):
        return string.replace(" ","")

#This function handles the userinput and the object generated from the Passmaker class.
def displayer():
    active = True
    print(library.title[0])
    while active:
        word = input(">> ")
        if (len(word) > 6):
            print(library.other[0])
        else:
            active = False
            myPass = Passmaker(word)
            print(library.other[1], myPass.scram())

displayer()
