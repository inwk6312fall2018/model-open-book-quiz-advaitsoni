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

my_deck=p.Deck(deck())
#my_deck.shuffle()	#shuffle deck
#card=my_deck.draw()	#draw one card
#print(card)
player1=[]
player2=[]
player_list=[player1,player2]	#list of players

for card in range(5):
	for player in player_list:
		my_deck.shuffle()
		player.append(my_deck.draw())
print(player_list)	#card list of each player

def burn_card():
	"""to burn i.e remove 1st card of deck"""
	global my_deck
	burn=my_deck.draw()
	my_deck.discard(burn)
	return my_deck

def replace_card(player_name,cards_to_replace):
	"""to replace cards with new one"""
	burn_card()	#remove 1st card from deck
	for i in range(len(cards_to_replace)):	
		if cards_to_replace[i] in player_name:
			player_name.remove(cards_to_replace[i])
			player_name.append(my_deck.draw())
	return player_list

#a=[player2[1],player2[2]]
#print(replace_card(player2,a))

def hand_rankings(a):
	"""to check ranking of hands"""
	for i in range(len(a)):
		b=sorted(a[i])
		if a[i][0][1]==a[i][1][1]==a[i][2][1]==a[i][3][1]==a[i][4][1] and b[0][0]==1 and b[1][0]==10 and b[2][0]==11 and b[3][0]==12 and b[4][0]==13:
			print('royal_flush')
		elif a[i][0][1]==a[i][1][1]==a[i][2][1]==a[i][3][1]==a[i][4][1] and b[1][0]==b[0][0]+1 and b[2][0]==b[0][0]+2 and b[3][0]==b[0][0]+3 and b[4][0]==b[0][0]+4:
			print('straight_flush')
		elif b[0][0]==b[1][0]==b[2][0]==b[3][0] or b[1][0]==b[2][0]==b[3][0]==b[4][0]:
			print('four_of_a_kind')
		elif (b[0][0]==b[1][0]==b[2][0] and b[3][0]==b[4][0]) or (b[0][0]==b[1][0] and b[2][0]==b[3][0]==b[4][0]):
			print('full house')
		elif b[0][1]==b[1][1]==b[2][1]==b[3][1]==b[4][1] and b[1][0]!=b[0][0]+1 and b[2][0]!=b[1][0]+1 and b[3][0]!=b[2][0]+1 and b[4][0]!=b[3][0]+1:
			print('flush')
		else:
			print('none')

#to test hand_rankings func
aa=[[(1,'b'),(10,'b'),(11,'b'),(12,'b'),(13,'b')],[(9,'b'),(10,'b'),(11,'b'),(12,'b'),(13,'b')],[(9,'b'),(10,'b'),(9,'a'),(9,'f'),(9,'h')],[(9,'b'),(10,'b'),(9,'a'),(10,'f'),(9,'h')],[(7,'b'),(1,'b'),(3,'b'),(10,'b'),(9,'b')]]
print(len(aa))
print(sorted(aa[0]))
hand_rankings(aa) 

