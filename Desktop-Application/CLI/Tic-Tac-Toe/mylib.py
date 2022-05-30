# mylib.py

#choose x or o for players

def choose_symbol():
 print("Players Choose your symbols")
 player1_symbol=input("Player 1:Enter X or O\n")
 while player1_symbol != 'x' and player1_symbol != 'o':
  player1_symbol=input("Player 1: Enter X or O\n")
 if player1_symbol=='x':
  x_or_o={'one':'X','two':'O'}
 else:
  x_or_o={'one':'O','two':'X'}
 print("\nPlayer 1:",x_or_o['one'],"\nPlayer 2:",x_or_o['two'])
 return x_or_o

#display table

def display_table(entries):
 print('\n\n','\t'*15,end='')
 print(entries[0][0],'|',entries[0][1],'|',entries[0][2])
 print('\t'*14,'      - - - - - -')
 print('\t'*15,end='')
 print(entries[1][0],'|',entries[1][1],'|',entries[1][2])
 print('\t'*14,'      - - - - - -')
 print('\t'*15,end='')
 print(entries[2][0],'|',entries[2][1],'|',entries[2][2])

# to get an input

def getinput(entries,x_or_o):
 player_flag=1
 cur_player='one'
 won_flag=False
 while not won_flag:
  print('Player',cur_player,',your turn now!')
  inp=input()
  entries=check_and_store_input(inp,entries,cur_player,x_or_o)
  print('\n'*60)
  display_table(entries)
  print('\n'*25)
  won_flag=check_end(entries,x_or_o[cur_player])
  if won_flag==-1:
   print("Match Is Draw!")
   return None
  player_flag+=1
  if player_flag%2==0:
   cur_player='two'
  else:
   cur_player='one'
 display_result(cur_player)

#to check if the given input is crt and not already taken

def check_and_store_input(inp,entries,cur_player,x_or_o):
 while True:
  while not inp.isdigit() or eval(inp) not in range(1,10):
   inp=input("Enter a number between 1 and 9 which has not been choosen already\n")
  inp=eval(inp)
  if inp%3!=0 and entries[inp//3][inp%3-1]==' ':
   entries[inp//3][inp%3-1]=x_or_o[cur_player]
   break
  elif entries[inp//3-1][2]==' ':
   entries[inp//3-1][2]=x_or_o[cur_player]
   break
  else:
   inp=input("Enter a number between 1 and 9 which has not been choosen already\n")
 return entries

#to display result

def display_result(other_player):
 if other_player=='one':
  print('Player 2 Has Won')
 else:
  print('Player 1 Has Won')

#to check if game has finished or not

def check_end(entries,symbol):
#vertical
 a,b,c=entries
 for i in range(3):
  if a[i]==b[i]==c[i]==symbol:
   return True

#horizontal
 for i in entries:
  if i.count(symbol)==3:
   return True		#won
 
#diag
 if entries[0][0]==entries[1][1]==entries[2][2]==symbol or entries[0][2]==entries[1][1]==entries[2][0]==symbol:
  return True 
 count=0

#draw
 for i in entries:
  if ' ' not in i:
   count+=1
 if count==3:
  return -1
