# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from ast import If
word= str(input("please enter the first word: "))
anagram= str(input("please enter the second word: "))

def find_anagram(word, anagram):
    # [assignment] Add your code here
    
    str1=word.lower()
    str2= anagram.lower()
    sort_str1 = sorted(str1)
    sort_str2 = sorted(str2)
    if len(str1)==len(str2):
        
        if sort_str1==sort_str2:
            print("This is an anagram")
        else:
            print("This is an not anagram")
    else:
        print("This is an not anagram")
find_anagram(word, anagram)

