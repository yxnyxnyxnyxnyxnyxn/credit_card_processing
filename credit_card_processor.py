import sys 
from credit_card import CreditCard 

class CreditCardProcessor: 
  def __init__(self,input):
    self.credit_cards = {} 
    for line in input:
      line = line.split(' ')
      action = line[0]
      if action ==  "Add":
         self.add(line)
      if action == "Charge":
         self.charge(line)
      if action ==  "Credit":
         self.credit(line)
  
  def add(self, line):
    [action, name, card_number, amount] = line
    self.credit_cards[name] = CreditCard(card_number, int(amount[1:])) 
     
  def charge(self,line):
    action, name,amount = line
    cc = self.credit_cards[name]
    amount = int(amount[1:])
    if cc.isValid and cc.balance + int(amount) < cc.limit:
        self.credit_cards[name].balance  += int(amount) 
    

  def credit(self,line):
    [action, name,amount] = line 
    cc = self.credit_cards[name]
    if cc.isValid:
      cc.balance -= int(amount[1:])
  
  def output(self):
    output = ""
    sorted_credit_cards = dict(sorted((self.credit_cards.items)(), key=lambda x: x[0]))
    for k,v in sorted_credit_cards.items():
      if v.isValid: 
        output += f"{k}:${v.balance}\n"
      else:
        output += f"{k}:error\n"
    sys.stdout.write(output)

def main():
  if len(sys.argv) == 1:
     credit_card_processor = CreditCardProcessor(sys.stdin)
     credit_card_processor.output()
  elif len(sys.argv) == 2:
     file_path = sys.argv[1]
     file = open(file_path,"r+")
     credit_card_processor = CreditCardProcessor(file.readlines())
     credit_card_processor.output()
 
if __name__ == '__main__':
  main() 
   	
	
