from pyexpat import model
from django.db import models

class toEnglish(models.Model):
    def brailleToEnglish(braille):
        alphaBraille = ['⠁', '⠃', '⠉', '⠙', '⠑', '⠋', '⠛', '⠓', '⠊', '⠚', '⠅', '⠇',
        '⠍', '⠝', '⠕', '⠏', '⠟', '⠗', '⠎', '⠞', '⠥', '⠧', '⠺', '⠭', '⠽', '⠵', ' ']
        numBraille = ['⠼⠁', '⠼⠃', '⠼⠉', '⠼⠙', '⠼⠑', '⠼⠋', '⠼⠛', '⠼⠓', '⠼⠊', '⠼⠚']
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        puntuation = [',',';',':','.','?','!', ';','(',')', '/', '-']
        puntuationBraille = ['⠂','⠆','⠒','⠲','⠦','⠖','⠐⠣','⠐⠜','⠸⠌','⠤']
        character = ['&','*','@','©','®','™','°',]
        characterBraille = ['⠈⠯','⠐⠔','⠈⠁','⠘⠉','⠘⠗','⠘⠞','⠘⠚',]

        inputString = ' '

        if len(braille) > 0:
            for n in braille:
                if n in alphaBraille:
                    inputString += alphabet[alphaBraille.index(n)]
                elif n in numBraille:
                    inputString += nums[numBraille.index(n)]
                elif n in puntuationBraille :
                    inputString += puntuation[puntuationBraille.index(n)]
                elif n in characterBraille:
                    inputString += character[characterBraille.index(n)]

            print(inputString)
            return

class brailleTo(models.Model):
    input = models.CharField(max_length = 200)
    
    def __str__(self):
        return toEnglish.brailleToEnglish(self.input)