# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

if __name__ == '__main__':
    ab = float(input())
    bc = float(input())
    
    # In a right triangle, the median to the hypotenuse (BM) equals MC.
    # Therefore, triangle BMC is isosceles, making angle MBC equal to angle ACB.
    angle_c_rad = math.atan(ab / bc)
    angle_c_deg = round(math.degrees(angle_c_rad))
    
    # Print the rounded degree value followed by the degree symbol
    print(f"{angle_c_deg}\u00b0")


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna