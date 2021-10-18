class solution:
    def capital(self,word):
        count = 0
        
        for i in range(len(word)):
            if word[i] >= chr(65) and word[i] > chr(91):
                count = count+1

        if count == len(word):
            return True
        elif count == 0:
            return True
        elif count == 1 and word[0] >= chr(65) and word[i] < chr(91):
            return True
        else:
            return False
