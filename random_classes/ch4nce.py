import random

class ch4nce:
    def __init__(self):
        return
    
    @staticmethod
    def randomize(winchance):
        if winchance >= 100:
            print('Winchance must be a value under 100')
            exit

        winchance += 1
        value = random.randrange(1, 100)
        
        if value < winchance:
            return True
        elif value > winchance:
            return False

    @staticmethod
    def flip(*args):

        value = random.randrange(1, 100)
        
        if value < 51:
            return True
        elif value > 51:
            return False
