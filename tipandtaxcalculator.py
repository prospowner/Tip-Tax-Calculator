#getting input

bill = float(input('What was the total bill?'))
tax_rate = float(input('What is the tax rate in percentage?'))
no_of_people = int(input("How many people to split the bill between?"))
tip = float(input('How much percentage you want to tip?'))
#calculation setup

tax_amount = (bill * (tax_rate / 100))
tip_amount = tip_amount = bill * (tip / 100)
grand_total = grand_total = bill + tax_amount + tip_amount
share = (grand_total / no_of_people)
#getting output

print(f'The total bill with tax and tip is: {grand_total}')
print(f'Each person should pay: {share}')