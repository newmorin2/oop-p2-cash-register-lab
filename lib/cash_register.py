#!/usr/bin/env python3

class CashRegister:
  def __init__(self,discount=0):
      self._discount = discount
      self.total = 0
      self.items = []
      self.previous_transactions = []

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

  def add_item(self, item, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
          self.items.append(item)

        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

  def apply_discount(self):
        if len(self.previous_transactions) == 0:
            print("There is no discount to apply.")
            return

        discount_amount = (self.discount / 100) * self.total
        self.total -= discount_amount

        last_transaction = self.previous_transactions.pop()

        if last_transaction["item"] in self.items:
            self.items.remove(last_transaction["item"])

  def void_last_transaction(self):
        if len(self.previous_transactions) == 0:
            print("No transactions to void.")
            return

        last = self.previous_transactions.pop()

        self.total -= last["price"] * last["quantity"]

        if last["item"] in self.items:
            self.items.remove(last["item"])