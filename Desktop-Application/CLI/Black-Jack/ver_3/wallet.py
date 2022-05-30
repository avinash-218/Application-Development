#wallet

#this is casino wallet account
class Wallet:

 def open_account(self):		#get name and money to deposit into casino wallet
  self.name=''
  while not self.name.isalpha():
   self.name=input('Enter your first name\n').upper()
  self.balance=''
  while not self.balance.isdigit():
   self.balance=input('\nEnter money to deposit into your casino wallet\n')
  self.balance=eval(self.balance)
  
 def display(self):		#display wallet details(name,balance)
  print(f"\n{self.name}'s Details:")
  print('-'*15)
  print(f"Name\t\t:{self.name}\nBalance\t\t:{self.balance}\n")

 def deposit(self,deposit):		#to deposit money into wallet
  print('Deposit Accepted',deposit)
  self.balance+=deposit

 def withdraw(self,withdraw):		#to withdraw amount from wallet
  print('Withdraw Accepted',withdraw)
  self.balance-=withdraw

