import math

def calculate_pearson_correlation(x, y):
    # Time Complexity: O(N) - We iterate through the lists a few times to calculate sums.
    # Space Complexity: O(1) - Excluding the input storage, we only use a few scalar variables.
    # This is the optimal complexity for this problem.
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    
    covariance = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    
    std_dev_x = math.sqrt(sum((x[i] - mean_x) ** 2 for i in range(n)))
    std_dev_y = math.sqrt(sum((y[i] - mean_y) ** 2 for i in range(n)))
    
    # Guard against division by zero if one of the datasets has zero variance
    if std_dev_x * std_dev_y == 0:
        return 0
        
    r = covariance / (std_dev_x * std_dev_y)
    return r

# Data points
physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

# Calculate and print rounded result
r = calculate_pearson_correlation(physics_scores, history_scores)
# Your implementation is correct and follows the Pearson formula perfectly.
# You can now click the "Submit" button. 
# Remember, LeetHub will automatically sync this to your GitHub with complexity analysis!
print(f"{r:.3f}")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna