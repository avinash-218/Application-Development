#display.py

def welcome():		#welcome note
 print('-'*190)
 print('\n     \t\t\t\t\t\t\t\t\t\tWelcome to Black Jack\n')
 print('-'*190)

def intro():		#everything about black jack game
 about_game=open('About_black_jack.txt','r')
 print(about_game.read())

def match_draw():	#when match is draw due to equal total
 print('You and Dealer have same total')
 print('Match is Draw!')
 print('You neither won nor lost')
 print('Your bet money will be deposited in your account')

def pause():		#to pause
 input('\nPress Enter to continue\n')
