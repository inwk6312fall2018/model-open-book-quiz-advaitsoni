import pyCardDeck as p
def deck():
	#generate card deck
	card_type=['Heart','Club','Black','Spade']
	card_no={'K':'King','Q':'Queen','J':'Jack',10:'ten',9:'nine',8:'eight'
	,7:'seven',6:'six',5:'five',4:'four',3:'three',2:'two','A':'Ace'}
	cards=[]
	for i in card_type:
		for k,v in card_no.items():
			cards.append(v+' '+'of'+' '+i)
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
