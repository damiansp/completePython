import random


DECK = 4 * [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


def main():
    deck = DECK[:]
    random.shuffle(deck)
    d_cards = deal_cards('dealer', deck)
    p_cards = deal_cards('player', deck)
    print_welcome()


def print_welcome():
    print('       ---------------------------------------------       ')
    print('            Welcome the game Casino Black Jack!            ')
    print('       ---------------------------------------------       ')


def deal_cards(recipient, deck):
    cards = []
    for _ in range(2):
        cards.append(deck.pop())
    if sum(cards) > 21:
        print(
            f'{recipient} busted. '
            f'You {"win" if recipient == "dealer" else "lose"}!')
        exit()
    if sum(cards == 21):
        print(
            f'{recipient} got BLACK JACK! '
            f'You {"win" if recipient == "player" else "lose"}!')
        exit()
    if recipient == 'dealer':
        print(f'Dealer\'s cards: [{cards[0]}, ??]')
    else:
        print(f'Your cards: {cards}')
        
