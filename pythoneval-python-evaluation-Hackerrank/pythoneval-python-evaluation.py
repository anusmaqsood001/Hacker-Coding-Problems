if __name__ == '__main__':
    N = int(input())
    lst = []
    
    for _ in range(N):
        args = input().split()
        command = args[0]
        
        if command == "insert":
            lst.insert(int(args[1]), int(args[2]))
        elif command == "print":
            print(lst)
        elif command == "remove":
            lst.remove(int(args[1]))
        elif command == "append":
            lst.append(int(args[1]))
        elif command == "sort":
            lst.sort()
        elif command == "pop":
            lst.pop()
        elif command == "reverse":
            lst.reverse()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna