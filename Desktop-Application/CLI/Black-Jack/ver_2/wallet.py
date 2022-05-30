#wallet

#this is casino wallet account
class Wallet:
 
 def get_details(self):		#get name and money to deposit into casino wallet
  self.name=''
  while not self.name.isalpha():
   self.name=input('Enter your name\n')
  self.balance=''
  while not self.balance.isdigit():
   self.balance=input('Enter money to deposit into your casino wallet\n')
  self.balance=eval(self.balance)
  self.display()
  
 def display(self):		#display wallet details(name,balance)
  print('\nWallet Details:')
  print('-'*21)
  print(f"Name\t\t:{self.name}\nBalance\t\t:{self.balance}\n")

 def deposit(self):		#to deposit money into wallet
  deposit=''
  while not deposit.isdigit():
   deposit=input('Enter amount to deposit in your wallet in numbers\n')
  print('Deposit Accepted',deposit)
  deposit=eval(deposit)
  self.balance+=deposit
  print('Now,your wallet details are updated to:')
  self.display()

 def withdraw(self):		#to withdraw amount from wallet
  withdraw=''
  while not(withdraw.isdigit() and eval(withdraw)<=self.balance):
   self.display()						#print wallet details
   withdraw=input('Enter correct value to withdraw from your wallet\n')
  print('Withdraw Accepted',withdraw)
  withdraw=eval(withdraw)
  self.balance-=withdraw
  print('Now,your wallet details are updated to:')
  self.display()



