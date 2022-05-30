#bank_account

class Account:
 owner='Avinash'
 balance=1000
 
 def display():
  print('Bank Account Details:')
  print('-'*21)
  print(f"Account Owner\t:{Account.owner}\nAccount Balance\t:{Account.balance}\n")

 def deposit(deposit):
  print('Deposit Accepted',deposit)
  Account.balance+=deposit

 def withdraw(withdraw):
  if Account.balance>withdraw:
   print('Withdraw Accepted',withdraw)
   Account.balance-=withdraw
  else:
   print('Funds Unavailable')

