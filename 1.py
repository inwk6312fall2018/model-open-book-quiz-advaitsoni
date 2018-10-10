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

def replace_card(player_name,cards_to_replace):
	"""to replace cards with new one"""
	burn_card()	#remove 1st card from deck
	for i in range(len(cards_to_replace)):	
		if cards_to_replace[i] in player_name:
			player_name.remove(cards_to_replace[i])
			player_name.append(my_deck.draw())
	return player_list

def hand_rankings(a):
	"""to check ranking of hands"""
	for i in range(len(a)):
		b=sorted(a[i])
		if b[0][1]==b[1][1]==b[2][1]==b[3][1]==b[4][1] and b[0][0]==1 and b[1][0]==10 and b[2][0]==11 and b[3][0]==12 and b[4][0]==13:
			print('royal_flush')
		elif b[0][1]==b[1][1]==b[2][1]==b[3][1]==b[4][1] and b[1][0]==b[0][0]+1 and b[2][0]==b[0][0]+2 and b[3][0]==b[0][0]+3 and b[4][0]==b[0][0]+4:
			print('straight_flush')
		elif b[0][0]==b[1][0]==b[2][0]==b[3][0] or b[1][0]==b[2][0]==b[3][0]==b[4][0]:
			print('four_of_a_kind')
		elif (b[0][0]==b[1][0]==b[2][0] and b[3][0]==b[4][0]) or (b[0][0]==b[1][0] and b[2][0]==b[3][0]==b[4][0]):
			print('full house')
		elif b[0][1]==b[1][1]==b[2][1]==b[3][1]==b[4][1] and b[1][0]!=b[0][0]+1 and b[2][0]!=b[1][0]+1 and b[3][0]!=b[2][0]+1 and b[4][0]!=b[3][0]+1:
			print('flush')
		elif b[1][0]==b[0][0]+1 and b[2][0]==b[0][0]+2 and b[3][0]==b[0][0]+3 and b[4][0]==b[0][0]+4 and (b[0][1]!=b[1][1] or b[1][1]!=b[2][1] or b[2][1]!=b[3][1] or b[3][1]!=b[4][1] or b[4][1]!=b[0][1]):
			print('Straight')
		elif b[0][0]==b[1][0]==b[2][0] or b[1][0]==b[2][0]==b[3][0] or b[2][0]==b[3][0]==b[4][0]:
			print('three_of_a_kind')
		elif (b[0][0]==b[1][0] and b[2][0]==b[3][0]) or (b[1][0]==b[2][0] and b[3][0]==b[4][0]) or (b[0][0]==b[1][0] and b[3][0]==b[4][0]):
			print('two_pair')
		elif b[0][0]==b[1][0] or b[1][0]==b[2][0] or b[2][0]==b[3][0] or b[3][0]==b[4][0] or b[0][0]==b[4][0]:
			print('Pair')
		else:
			print('high_card')


my_deck=p.Deck(deck())
player1=[]
player2=[]
player_list=[player1,player2]   #list of players

for card in range(5):
        for player in player_list:
                my_deck.shuffle()
                player.append(my_deck.draw())
print(player_list)      #card list of each player

hand_rankings(player_list) 
