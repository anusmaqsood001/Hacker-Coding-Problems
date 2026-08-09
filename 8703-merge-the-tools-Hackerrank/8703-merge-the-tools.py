def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        # Slice substring of length k
        t_i = string[i:i + k]
        
        # dict.fromkeys preserves insertion order in Python 3.7+ while removing duplicates
        u_i = "".join(dict.fromkeys(t_i))
        print(u_i)




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna