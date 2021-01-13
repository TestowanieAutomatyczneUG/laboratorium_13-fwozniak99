class Mirrored:
    def game(self, word1, word2):
        if type(word1) is str and type(word2) is str:
            if len(word1) == len(word2):
                mirrored = word1[::-1]
                if word2 == mirrored:
                    return True
                else:
                    return False
            else:
                return "Words aren't the same length"
        elif type(word1) is int or type(word2) is int:
            return "Cannot be an integer"
        else:
            return "Must be a string"
