print("Welcome to the tip calculator 🤩🔥")
total_bill = int(input("What is the total bill ? $"))
tip_amount = int(input("How much tip you would like to give? 10,12 or 15 ?"))
people = int(input("How many people to split the bill ?"))

tip_as_percent = tip_amount/100
tips_calculating = (total_bill * tip_as_percent)+ total_bill
bill_per_person = tips_calculating/people
final_amount = round(bill_per_person,2)
print(f"The amount has to be paid by each person is ${final_amount}")