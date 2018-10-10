import pyCardDeck as p
def deck():
	#generate card deck
	card_type=['Heart','Club','Black','Spade']
	card_no={13:'King',12:'Queen',11:'Jack',10:'ten',9:'nine',8:'eight'
	,7:'seven',6:'six',5:'five',4:'four',3:'three',2:'two',1:'Ace'}
	cards=[]
	for i in card_type:
		for k,v in card_no.items():
			cards.append((k,i))
	return cards

def burn_card():
	"""to burn i.e remove 1st card of deck"""
	global my_deck
	burn=my_deck.draw()
	my_deck.discard(burn)
	return my_deck

def replace_card(player_name,cards_to_replace):		#player_name= card list of player; cards_to_list= list of cards, player wants to replace
	"""to replace cards with new one"""
	burn_card()	#remove 1st card from deck
	for i in range(len(cards_to_replace)):	
		if cards_to_replace[i] in player_name:
			player_name.remove(cards_to_replace[i])
			player_name.append(my_deck.draw())
	return player_name

def hand_rankings(b):		#b= card list of player
	#to check ranking of hands"""
	if b[0][1]==b[1][1]==b[2][1]==b[3][1]==b[4][1] and b[0][0]==1 and b[1][0]==10 and b[2][0]==11 and b[3][0]==12 and b[4][0]==13:
		return ('royal_flush')
	elif b[0][1]==b[1][1]==b[2][1]==b[3][1]==b[4][1] and b[1][0]==b[0][0]+1 and b[2][0]==b[0][0]+2 and b[3][0]==b[0][0]+3 and b[4][0]==b[0][0]+4:
		return ('straight_flush')
	elif b[0][0]==b[1][0]==b[2][0]==b[3][0] or b[1][0]==b[2][0]==b[3][0]==b[4][0]:
		return ('four_of_a_kind')
	elif (b[0][0]==b[1][0]==b[2][0] and b[3][0]==b[4][0]) or (b[0][0]==b[1][0] and b[2][0]==b[3][0]==b[4][0]):
		return ('full house')
	elif b[0][1]==b[1][1]==b[2][1]==b[3][1]==b[4][1] and b[1][0]!=b[0][0]+1 and b[2][0]!=b[1][0]+1 and b[3][0]!=b[2][0]+1 and b[4][0]!=b[3][0]+1:
		return ('flush')
	elif b[1][0]==b[0][0]+1 and b[2][0]==b[0][0]+2 and b[3][0]==b[0][0]+3 and b[4][0]==b[0][0]+4 and (b[0][1]!=b[1][1] or b[1][1]!=b[2][1] or b[2][1]!=b[3][1] or b[3][1]!=b[4][1] or b[4][1]!=b[0][1]):
		return ('Straight')
	elif b[0][0]==b[1][0]==b[2][0] or b[1][0]==b[2][0]==b[3][0] or b[2][0]==b[3][0]==b[4][0]:
		return ('three_of_a_kind')
	elif (b[0][0]==b[1][0] and b[2][0]==b[3][0]) or (b[1][0]==b[2][0] and b[3][0]==b[4][0]) or (b[0][0]==b[1][0] and b[3][0]==b[4][0]):
		return ('two_pair')
	elif b[0][0]==b[1][0] or b[1][0]==b[2][0] or b[2][0]==b[3][0] or b[3][0]==b[4][0] or b[0][0]==b[4][0]:
		return ('Pair')
	else:
		return ('high_card')

def change_cards(list_of_player):	#list_of_player= list of cards, of all players
	"""if player wants to replace cards"""
	lst=[]
	card=[]
	while len(my_deck)>=3:		#to check if the remaining cards are more than 3 in deck 
		for i in range(4):
			ask=input("do you want to replace any card/s player %d [y/n]:" %i)
			if ask=='y':
				print("how many card/s you want to replace (valid upto 3) ?")
				cards_to_replace=int(input())
				if cards_to_replace<=3:			#if user enters upto 3 cards then proceed further
					print("enter card/s you want to replace")
					for j in range(cards_to_replace):
						print("please enter card number:")
						num=int(input())
						print("please enter card type i.e 'Black','Spade' etc.:")
						card_type=input()
						card.append((num,card_type))
					list_of_player[i]=replace_card( list_of_player[i], card)	#calling replace_card function
					print("updated card list of player %d" %i,list_of_player[i])
				else:
					print("at a time, you can replace upto 3 cards only! ")
			else:
				lst.append('n')
		if len(lst)>=4:
			break
	return print_cards(list_of_player)

def print_cards(list_var):
	"""to print each players card seperately"""
	for i in range(len(list_var)):
		print("player %d cards are" %i,list_var[i])

my_deck=p.Deck(deck())
player1=[]
player2=[]
player3=[]
player4=[]
player_list=[player1,player2,player3,player4]   #list of players

for card in range(5):		#to create list of cards for each player
        for player in player_list:
                my_deck.shuffle()
                player.append(my_deck.draw())

print_cards(player_list) 

print(change_cards(player_list))

for i in range(len(player_list)):	#to print hand ranks of each player
	print("player %d hand rank is:" %i,hand_rankings(player_list[i]))


