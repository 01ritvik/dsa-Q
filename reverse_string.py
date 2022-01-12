class solution:
    def rev_str(self,word):
        left = 0
        right = len(word) - 1

        
        while left < right:
            word[left],word[right] = word[right],word[left]
            left = left+1
            right = right -1
