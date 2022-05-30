#myapp.py

import mylib as lib

def main():
 print('\n')
 print('-'*190)
 print("\t\t\t\t\t\t\t\t\t\t\t\t\tTic Tac Toe")
 print('-'*190)
 while True:
  print()
  x_or_o=lib.choose_symbol()
  entries=[ ['1','2','3'] , ['4','5','6'] , ['7','8','9']]
  lib.display_table(entries)
  entries=[ [' ',' ',' '],[' ',' ',' '],[' ',' ',' '] ]
  print('\nPlayer should enter the number as displayed in the table to mark the position with his/her symbol')
  print('\n\n\t\t\t\t\t\t\t\t\t\t\t\t\tGame Begins!!!\n')
  lib.getinput(entries,x_or_o)
  print("\nDo You Want To Play Again ?")
  play_again=''
  while play_again != 'yes' and play_again != 'no':
   play_again=input("\n\tYes Or No?\n")
  if play_again.lower()=='no':
   print("\n\t\t\t\t\tCome Back Again...Bye!")
   break
  elif play_again.lower()=='yes':
   pass

main()
