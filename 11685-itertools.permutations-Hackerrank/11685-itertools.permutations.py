# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

if __name__ == '__main__':
    s, k = input().split()
    k = int(k)
    
    # Sort the string first so permutations are generated in lexicographic order
    for p in permutations(sorted(s), k):
        print("".join(p))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna