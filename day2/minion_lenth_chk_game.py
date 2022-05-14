def minion_game(string):
    # your code goes here
    vovels = "AEIOU"
    stuart = 0
    kevin = 0
    for i in range(len(s)):
     if s[i] in vovels:
        kevin += (len(s)-i)
     else:
        stuart += (len(s)-i)
    
    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif kevin < stuart:
        print(f"Stuart {stuart}")
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)