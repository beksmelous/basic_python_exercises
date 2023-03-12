print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
people_to_split = input("How many people to split the bill? ")

percentage = int(tip) / 100
tip_amount = percentage * int(total_bill)
total_amount = tip_amount + int(total_bill)
each_person_schould_pay = total_amount / int(people_to_split)
each_person_schould_pay_rounded = round(each_person_schould_pay, 2)
print(f"Each person schould pay ${each_person_schould_pay_rounded}")
