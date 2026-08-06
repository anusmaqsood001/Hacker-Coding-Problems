# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
from sklearn.linear_model import LinearRegression

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # Read F (number of features) and N (number of training rows)
    F = int(input_data[0])
    N = int(input_data[1])
    
    idx = 2
    
    # Read training data
    X_train = []
    y_train = []
    for _ in range(N):
        row = [float(x) for x in input_data[idx : idx + F]]
        price = float(input_data[idx + F])
        X_train.append(row)
        y_train.append(price)
        idx += F + 1
        
    # Read T (number of test queries)
    T = int(input_data[idx])
    idx += 1
    
    # Read test features
    X_test = []
    for _ in range(T):
        row = [float(x) for x in input_data[idx : idx + F]]
        X_test.append(row)
        idx += F
        
    # Fit Ordinary Least Squares Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Predict test targets
    predictions = model.predict(X_test)
    
    # Output predictions rounded to 2 decimal places
    for pred in predictions:
        print(f"{pred:.2f}")

if __name__ == '__main__':
    main()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna