# Ian Fife

def rollDice(die1, die2, die3, die4, die5, word):
    def get_variations(word):
        if len(word) == 1:
            return [word]
        result=[]
        for i,v in enumerate(word):
            for p in get_variations(word[:i] + word[i+1:]):
                result += [v+p]
        return result
    
    for char1 in die1:
        for char2 in die2:
            for char3 in die3:
                for char4 in die4:
                    for char5 in die5:
                        variation_list = get_variations(char1 + char2 + char3 + char4 + char5)
                        if word in variation_list:
                            return True
    return False

print(rollDice("ABGRTY", "EGKOWX", "ABVCXA", "POYEAT", "EITYTJ", "GREAT"))

print(rollDice("ABGRTY", "EGKOWX", "ABVCXA", "POYEAT", "EITYTJ", "TIGER"))
