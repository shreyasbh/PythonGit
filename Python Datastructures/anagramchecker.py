def anagramCheck(s1, s2):
    s1 = sanitizeString(s1)
    s2 = sanitizeString(s2)
    if sorted(s1) == sorted(s2):
        return True
    return False
    
    
def sanitizeString(s):
    slower = s.lower()
    ss = ""
    for i in slower:
        if i != " ":
            ss += i
    return ss

print(anagramCheck("clint eastwood", " old west action"))

def anagram2(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    return sorted(s1) == sorted(s2)

def anagram3(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    
    if len(s1) != len(s2):
        return False
    
    count = {}
    
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
                 
    for k in count:
        if count[k] != 0:
            return False
        
        return True

print(anagram3("clint eastwood", " old west action"))



    
    
