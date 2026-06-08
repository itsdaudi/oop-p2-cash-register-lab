#!/usr/bin/env python3
#creating cash register class
class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total=0
    self.items = []
    self.previous_transactions = []

#property discount
  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, value):
    if isinstance(value, int) and 0 <= value <= 100:
      self._discount = value
    else:
      print("Not valid discount")
      self._discount = 0

#method1 add_item      
def add_item(self, item, price, quantity=1):
    self.total += price * quantity
    self.items.append(item)
    self.previous_transactions.append({
      "item": item,
      "price": price,
      "quantity": quantity
    })
#method2 apply_discount
def apply_discount(self):
    if len(self.previous_transactions) == 0:
      print("There is no discount to apply.")
    else:
      discount_amount = self.discount / 100 * self.total
      self.total -= discount_amount
      print(f"Discount applied! New total: ${self.total:.2f}")

#method3 void_last_transaction
def void_last_transaction(self):
    if len(self.previous_transactions) == 0:
      print(" No transaction to void.")
    else:
        last=self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        self.items.remove(last["item"])           
  pass
