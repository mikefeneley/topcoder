class CardCount:
    
    def dealHands(self, numPlayers, deck):
        
        num_cards = len(deck) % numPlayers
        deck = deck[0:len(deck) - num_cards]
        hands = [] 
       
        for i in range(0,  numPlayers):
            hands.append('')

        for idx, card in enumerate(deck):
            hands[idx % numPlayers] += card

        hands = tuple(hands)
        return hands
