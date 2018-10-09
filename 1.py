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
