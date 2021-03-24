class Solution:
    def solve(self, words, s):
        dct = {}
        # def check(words,s):
        #     t = ""
        #     x = False
        #     for word in words:
        #         if(len(s) == 0):
        #             return True
        #         if(word in s):
        #             t = s[:s.index(word)] + s[s.index(word)+len(word):]

        #             if(len(t) == 0):
        #                 return True
        #             if(t in dct):
        #                 x = dct[t]
        #             else:
        #                 x = check(words,t)
        #                 dct[t] = x

        #     if(x == True):
        #         return True
        #     return False


        def check(s):
            if(s in dct):
                return dct[s]
            if(len(s) == 0):
                return True
            for word in words:
                if(s.startswith(word) ):
                    dct[s] = check(s[len(word):])
                    if(dct[s] == True):
                        return True
            return False


        return check(s)
                
        