import sys
import unittest
from unittest import TestCase

import sys
from credit_card_processor import CreditCardProcessor
from credit_card import CreditCard

class credit_card_processor_tests(TestCase):
  
  #card validation test
  def test_valid_card1(self):
   card_number = "5454545454545454"
   cc = CreditCard(card_number, 10000)
   self.assertEqual(cc.isValid, True)

  def test_valid_card2(self):
   card_number = "4111111111111111"
   cc = CreditCard(card_number, 10000)
   self.assertEqual(cc.isValid, True)
  
  def test_invalid_card(self):
   card_number = "1234567890123456"
   cc = CreditCard(card_number, 10000)
   self.assertEqual(cc.isValid, False)

  def test_overcharge(self):
    input = ["Add Tom 4111111111111111 $1000","Charge Tom $1200"]
    ccs = CreditCardProcessor(input)
    cc = ccs.credit_cards["Tom"] 
    self.assertEqual(cc.balance, 0)

  def happy_path_test(self):
    input = ["Add Tom 4111111111111111 $1000","Charge Tom $800", "Credit Tom $200"]
    ccs = CreditCardProcessor(input)
    cc = ccs.credit_cards["Tom"] 
    self.assertEqual(cc.balance, 600)

if __name__ == '__main__':
  unittest.main()
