# Making a Compound Interest Calculator Using Only Python

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principal amount (greater than 0): "))
    if principle <= 0:
        print("Principal amount must be greater than 0. Please try again.")

while rate <= 0:
    rate = float(input("Enter the interest rate (greater than 0): "))
    if rate <= 0:
        print("Interest rate must be greater than 0. Please try again.")

while time <= 0:
    time = int(input("Enter the time in years (greater than 0): "))
    if time <= 0:
        print("Time must be greater than 0. Please try again.")

# Calculate compound interest
total_amount = principle * (1 + rate / 100) ** time
print(f"The total amount after {time} year/s: ${total_amount:.2f}")
