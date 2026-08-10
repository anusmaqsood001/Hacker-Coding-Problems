# Enter your code here. Read input from STDIN. Print output to STDOUT
def sort_key(c):
    if c.islower():
        # Lowercase letters come first, sorted alphabetically
        return (0, c)
    elif c.isupper():
        # Uppercase letters come second, sorted alphabetically
        return (1, c)
    elif c.isdigit():
        # Odd digits come third, even digits come fourth
        if int(c) % 2 != 0:
            return (2, c)
        else:
            return (3, c)

if __name__ == '__main__':
    s = input()
    print("".join(sorted(s, key=sort_key)))


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna