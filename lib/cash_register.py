#!/usr/bin/env python3
#creating cash register class
class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total=0
    self.items = []
    self.previous_transaction = []

  pass
