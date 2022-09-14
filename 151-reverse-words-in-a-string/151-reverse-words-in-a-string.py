class Solution:
    def revword(self, word):
        revword = ""
        for j in range(len(word)-1, -1, -1):
            revword += word[j]
        return revword
            
    def reverseWords(self, s: str) -> str:
        ans = ""
        word = ""
        for i in range(len(s)-1, -1, -1): #14, -1, -1
            if s[i] == " " and len(word) > 0:
                cword = "" #eulb #si #yks
                cword = self.revword(word) #blue #is #sky
                if len(ans) != 0: #
                    ans += " " #blue 
                ans += cword #blue is sky
                word = "" #"" "" ""
            elif s[i] == " " and len(word) == 0:
                continue
            else:
                word += s[i] #si yks eht
      
        if len(word) > 0:
            cword = ""
            cword = self.revword(word)
            if len(ans) != 0: #
                ans += " " #blue 
            ans += cword 
        return ans
                
            
            
            
        
        
        
        
        