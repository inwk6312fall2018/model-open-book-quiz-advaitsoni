import pyCardDeck as p
def deck():
	card_type=['Heart','Club','Black','Spade']
	card_no={'K':'King','Q':'Queen','J':'Jack',10:'ten',9:'nine',8:'eight'
	,7:'seven',6:'six',5:'five',4:'four',3:'three',2:'two','A':'Ace'}
	cards=[]
	for i in card_type:
		for k,v in card_no.items():
			cards.append(v+' '+'of'+' '+i)
	return cards

my_deck=p.Deck(deck())
my_deck.shuffle()
card=my_deck.draw()
print(card)
