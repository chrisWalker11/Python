#defines function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) #calls function and feeds it variables 20 and 30


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50 
#calls cheese_and_crackers function feeds amount_of_cheese & amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6) #calls cheese_and_crackers and does math and result is the variable


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #calls function does math with the variables
