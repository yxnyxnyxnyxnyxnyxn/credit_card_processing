# credit_card_processing

###### Overview
A program that will add new credit card accounts and process the charge and credits against them, and display information. 

CreditCardProcessor:
Processes input file and organzie all the new credit cards into credit_card map using credit card holder's name as key. (Assumption: we dont need to handle or check multiple "Add" for tha same name)  
Take action on the credit card.

CreditCard: 
Store credit card metadata for each card holder. 
IsValid: boolean. Indicate if credit card holder has valid credit card. 
Balance: int. Store balance of valid credit cards. 
Limit: int. Store credit card limit for valid credit cards.

###### Programming Language 
Python
I choose python for this project for the following reason: 
1. More readable for reviewers  
2. Easier to implement (I'm more familiar with Python)

###### Run code 
- Run code: 
```
python3 credit_card_processor.py {input_path}

python3 credit_card_processor.py <{input_path}
```

- Run tests:
```
python3 credit_card_processor_test.py   
```





