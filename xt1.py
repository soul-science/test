import math

def ishui():
    n = int(input("input the n to hui:"))
    i = 2
    ok = []
    while i <= 16:
        flag = 1
        middle = n
        result = []
        yu = []
        if(int(middle/i >= 1)):
            while int(middle/i) >= 1:
                if middle%i != 0:
                    yu.append(int(middle%i))
                else:
                    yu.append(0)
                middle = (middle - middle%i)/i
            result.append(1*middle)
            while yu != []:
                result.append(int(yu.pop()))
        else:
            result.append(n)
        if len(result) == 1:
            flag = 0
        for j in range(0,int(len(result)/2)):
                if result[j] != result[len(result)-j-1]:
                    flag = 0
                    break;
        if flag == 1:
            ok.append(i)
        i = i + 1
    print(ok)
if __name__ == "__main__":
    ishui()
                
            
        
