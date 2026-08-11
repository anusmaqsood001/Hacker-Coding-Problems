# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == '__main__':
    # Read K (number of lists) and M (modulo value)
    k, m = map(int, input().split())
    
    # Read each list (ignoring the first element N_i which specifies length)
    lists = []
    for _ in range(k):
        elements = list(map(int, input().split()))[1:]
        lists.append(elements)
    
    # Generate all Cartesian products, compute (sum of squares) % M, and find max
    max_s = max(sum(x**2 for x in combination) % m for combination in product(*lists))
    
    print(max_s)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna