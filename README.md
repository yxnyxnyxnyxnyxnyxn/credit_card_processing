# credit_card_processing


Input: 
- fileinput as command line 
- STDIN input read 




Add: 
create a new credit card (name, card number, limit) 
- card number validation Luhn10 
- start with 0 balance 


Charge: 
Increase balance for a card number with amount  
- charges over limit -> declined 
- Charge against invalid card are ignored 



Credit: 
Decrease balance 
- can be negative balance
- ignore invalid card 
