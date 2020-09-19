class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5 = c10 = 0
        for i in bills:
            if i == 5: c5+=1
            elif i == 10 :
                c10 +=1
                if c5 >= 1: 
                    c5 -= 1
                else : 
                    return False
            elif i == 20:
                if c10>=1 and c5>=1:
                    c10 -=1
                    c5 -=1
                elif c5>=3:
                    c5-=3
                else: return False
        return True