'''
HIGHER OR LOWER CARD GAME
It is a guessing game where the user guesses whether a card from a shuffled deck of cards has a higher or lower 
value than a previously chosen card. If the user guesses correctly, he scores a point. If he guesses wrong, he
loses a life. Life is initialized to 5. The user wins if all the cards in the deck are used up. From lowest to
highest value, the cards are ace,2,3,4,5,6,7,8,9,10,J,Q,K.

There are 2 groups of cards, cards_in_deck and cards_in_stack. Cards that have not yet been chosen are in
cards_in_deck. Cards that have already been chosen are in cards_in_stack. The curr_card is a card that is randomly 
chosen from cards_in_deck, and transfer it to the top of cards_in_stack. You then choose another card called 
rand_card from the cards_in_deck. The game is for the user to guess whether rand_card has a higher or lower value
than curr_card. If the user guesses correctly, curr_card becomes rand_card and is transferred to the top of the
cards_in_stack. A new rand_card is chosen from the cards_in_deck. If the user guesses incorrectly, the user
loses a life and then a new rand_card is chosen from the cards_in_deck and the user is asked to guess again. The
game continues until the user loses all his lives or the cards_in_deck is empty (in which case the user wins the 
game) '''

import random
life=5
cards_in_deck={'sa':1,'s2':2,'s3':3,'s4':4,'s5':5,'s6':6,'s7':7,'s8':8,'s9':9,'s10':10,'sj':11,'sq':12,'sk':13,
'ha':1,'h2':2,'h3':3,'h4':4,'h5':5,'h6':6,'h7':7,'h8':8,'h9':9,'h10':10,'hj':11,'hq':12,'hk':13,
'ca':1,'c2':2,'c3':3,'c4':4,'c5':5,'c6':6,'c7':7,'c8':8,'c9':9,'c10':10,'cj':11,'cq':12,'ck':13 ,
'da':1,'d2':2,'d3':3,'d4':4,'d5':5,'d6':6,'d7':7,'d8':8,'d9':9,'d10':10,'dj':11,'dq':12,'dk':13}
# Cards that have not yet been chosen
cards_in_stack={} #Cards that have already been chosen
curr_card=random.choice(list(cards_in_deck.keys())) # Randomly chooses a card from cards_in_deck
cards_in_stack.update({curr_card:cards_in_deck[curr_card]}) # Adds curr_card to the top of cards_in_stack
cards_in_deck.pop(curr_card) # Removes curr_card from the cards_in_deck
rand_card=''

# Game is contained within this loop. The game continues until either life==0 or cards_in_deck is empty
while cards_in_deck and life: 
    print('Cards in deck:',cards_in_deck)
    print('Cards that have been chosen',cards_in_stack)
    print('Life remaining:',life)
    print('Current card:',curr_card)
    choice=input('Enter h for higher or l for lower: ')
    rand_card=random.choice(list(cards_in_deck.keys()))
    if choice=='h' or choice=='H':
        if cards_in_stack[curr_card]<=cards_in_deck[rand_card]:
            print('You guessed correctly!')
        else:
            print('You guessed wrong! You lose a life. The card was',rand_card)
            life-=1
            print()
            continue
    elif choice=='l' or choice=='L':
        if cards_in_stack[curr_card]<cards_in_deck[rand_card]:
            print('You guessed wrong! You lose a life. The card was',rand_card)
            life-=1
            print()
            continue
        else:
            print('You guessed correctly!')
    print('The card was',rand_card)
    curr_card=rand_card # curr_card becomes rand_card
    cards_in_stack.update({curr_card:cards_in_deck[curr_card]}) # curr_card is added to cards_in_stack
    cards_in_deck.pop(curr_card) # remove curr_card (which was rand_card previously) from cards_in_deck
    print()

if life==0:
    print('Game over')
    print('Score:',len(cards_in_stack))
else:
    print('You win!')
