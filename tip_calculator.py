

print('Welcome to tip calculator')

total_bill = float(input('What is the total bill?\n'))

tip_percentage = int(input('What percentage tip would you like to give? 5, 10, 12 or 15?\n'))

tip_perc = 1+(tip_percentage / 100)

new_total_bill = total_bill * tip_perc

num_cust = int(input('How many persons will contribute for the payment?\n'))

amount_per_person = round(new_total_bill / num_cust, 2)

print(f'Your original bill was {total_bill},\n The new bill including {tip_percentage}% is {new_total_bill}.\n Each person will pay the sum of {amount_per_person}')