#display.py

def welcome():		#welcome note
 print('-'*190)
 print('\n     \t\t\t\t\t\t\t\t\t\tWelcome to Black Jack\n')
 print('-'*190)

def intro():		#everything about black jack game
 about_game=open('About_black_jack.txt','r')
 print(about_game.read())

def black_jack_tie():	#to display when the player ties with the dealer due to 'natural'
 print('Dealer too has Natural BLACK JACK!!!')
 print('Match is a natural Tie for you')

def bust_player():	#to display when the player is busted
 print('You are busted')

def bust_dealer():	#to display when the player is busted after force hit(s)
 print('The Dealer is busted')
 print('You have won the original bet!!!')

def player_win():	#when player wins by maintaining more total than dealer's
 print('Congrajulation!!! You Win')
 print('You have won the original bet')

def player_lose():	#when player loses by maintaining lesser total than dealer's
 print('You Lose')
 print('You lost your original bet')

def match_draw():	#when match is draw due to equal total
 print('You and Dealer have same total')
 print('Match is Draw!')
 print('You neither won nor lost')
 print('Your bet money will be deposited in your account')

def pause():		#to pause
 input('\nPress Enter to continue\n')
