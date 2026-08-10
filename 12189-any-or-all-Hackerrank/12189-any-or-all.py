# Enter your code here. Read input from STDIN. Print output to STDOUT

n, numbers = input(), input().split()
print(all(int(x) > 0 for x in numbers) and any(x == x[::-1] for x in numbers))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna