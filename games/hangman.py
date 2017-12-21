from random import *
from pprint import pprint
class Hangman:
    def __init__(self, wordList):
        self.health = 8;
        self.word = wordList[randint(0, len(wordList)-1)];
        self.hidden = self.genHidden();
        self.guesses = [];
    def genHidden(self):
        length = len(self.word);
        hiddenChars = [];
        wordChars = list(self.word);
        for x in range(0, length):
            if(wordChars[x] == " "):
                hiddenChars += "  ";
            else:
                hiddenChars += "_ ";
        hiddenChars = hiddenChars[:-1];
        return ''.join(hiddenChars);
    def guess(self, letter):
        length = len(self.word);
        hiddenChars = list(self.hidden);
        wordChars = list(self.word);
        found = False;
        for x in range(0, length):
            if(wordChars[x] == letter):
                hiddenChars[(2*(x))] = letter;
                found = True;
        self.hidden = ''.join(hiddenChars);
        if(not found):
            self.health -= 1;
            self.guesses.append(letter);
        return found;
    def isDead(self):
        return self.health == 0;
    def checkWin(self):
        return "_" not in self.hidden;
    def gui(self):
        while(not self.checkWin() and not self.isDead()):
            print("Lives: " + str(self.health));
            print(self.hidden);
            pprint(self.guesses);
            g = input("Guess: ");
            if(self.guess(g)):
                print("Nice Job!");
            else:
                print("Oops!");
            print("-----------------------------------");
        print("--- Game Over ---");
        print("The word was: " + self.word);
        if(self.checkWin()):
            print("You have won!");
        else:
            print("You have lost!");
