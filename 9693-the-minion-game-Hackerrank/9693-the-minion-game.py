def minion_game(string):
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    n = len(string)
    
    for i in range(n):
        # A character at index i can form (n - i) substrings starting from index i
        if string[i] in vowels:
            kevin_score += (n - i)
        else:
            stuart_score += (n - i)
            
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna