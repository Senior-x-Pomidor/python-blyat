import random
import re
import time
from games_and_tools import googol

last_update = "27.06.2025"

def clear_terminal():
    # \033[H setzt den Cursor oben links, \033[J löscht bis zum Ende
    print("\033[H\033[J", end="")
def farbig(text, farbcode):
    return f"\033[{farbcode}m{text}\033[0m"
def big_text(text):
    money = str(googol.display_money_value())



    if text == "blackjack":
        print("\033[1;31m    ____  __           __     _            __  \033[0m")
        print("\033[1;31m   / __ )/ /___ ______/ /__  (_)___ ______/ /__\033[0m")
        print("\033[1;33m  / __  / / __ `/ ___/ //_/ / / __ `/ ___/ //_/\033[0m")
        print("\033[1;32m / /_/ / / /_/ / /__/ ,<   / / /_/ / /__/ ,<   \033[0m")
        print("\033[1;34m/_____/_/\\__,_/\\___/_/|_|_/ /\\__,_/\\___/_/|_|  \033[0m")
        print("\033[1;34m                       /___/                   \033[0m")
        print("by dani (Senior-x-Pomidor) "+last_update)
        print("Kontostand: "+money)
        print(" \n \n \n \n \n")
ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

warning_txt = warning_text = """
\033[1;31mGlücksspiel kann süchtig machen.\033[0m
Bitte spielen Sie verantwortungsbewusst und nur mit Geld, das Sie entbehren können.
Achten Sie auf Ihre Spielzeiten und Gewohnheiten – setzen Sie sich im Zweifel ein Limit.
Sollten Sie erste Anzeichen von problematischem Spielverhalten bei sich oder Angehörigen bemerken
(z.B. Kontrollverlust, zunehmende finanzielle Sorgen, soziale Isolation),
wenden Sie sich frühzeitig an professionelle Unterstützung:

– Bundeszentrale für gesundheitliche Aufklärung (BZgA)
  Telefon: 0800 1 372 700 (kostenfrei, vertraulich)
  https://www.bzga.de

– TelefonSeelsorge
  Telefon: 0800 111 0 111 oder 0800 111 0 222 (kostenfrei, rund um die Uhr)
  https://www.telefonseelsorge.de

Hilfe zu suchen ist kein Zeichen von Schwäche, sondern ein wichtiger Schritt,
um Ihre Lebensqualität zu schützen.
"""
#######################################################################


covered_card = f"""\
┌─────────┐
│\ / | \ /│
│ |-----| │
│/ \ | / \│    
││ │---│ ││
│\ / | \ /│
│ |-----| │
│/ \ | / \│
└─────────┘"""

def generate_cards_list():

    global cards_list
    global suit_list

    suit_list = ["♥","♦","♣","♠"]

    cards_list = []

    for suit in range(len(suit_list)):

        cards_list.append([])

        for card in range(1,14):

            if    card == 1: card =  "A" 
            elif  card == 11: card = "J"
            elif  card == 12: card = "Q"
            elif  card == 13: card = "K"
            else: card = str(card)

            if suit <= 1:
                card = farbig(card, "1;31")
                suit_list[suit] = farbig(suit_list[suit], "1;31")
            else:
                card = farbig(card, "1;37")#37--> to make black
                suit_list[suit] = farbig(suit_list[suit], "1;37")#37--> to make black
            
            cards_list[suit].append((card, suit_list[suit]))

def generate_deck_of_cards():

    global deck_of_cards
    deck_of_cards = []

    for suit in range(len(cards_list)):
        for card in range(len(cards_list[suit])):
            new_card = (cards_list[suit][card][0] + cards_list[suit][card][1])
            deck_of_cards.append(new_card)
    random.shuffle(deck_of_cards)

def pull_card():

    global pulled_card

    pulled_card = deck_of_cards.pop()

def generate_hand(person): 

    if person == "dealer":
        for i in range(2):
            pull_card()
            hand_dealer.append(pulled_card)

    if person == "player_1":
        for i in range(2):
            pull_card()
            hand_player_1.append(pulled_card)

    if person == "player_2":
        for i in range(2):
            pull_card()
            hand_player_2.append(pulled_card)
    
def update_hand(person):

    if person == "dealer":

            pull_card()
            hand_dealer.append(pulled_card)
            print("Dealer zieht Karte!")
            time.sleep(2)
            return
    
    choice = input("Wie entscheidest du dich?\n" \
    "Hit = H, Stand = S\n").lower()



    if choice == "h":
        

        if person == "player_1":

            pull_card()
            hand_player_1.append(pulled_card)
        if person == "player_2":

            pull_card()
            hand_player_2.append(pulled_card)
    else:
        return choice

def generate_card_image(card_number, person):

    if person == "dealer":
        hand = hand_dealer
    elif person == "player_1":
        hand = hand_player_1
    elif person == "player_2":
        hand = hand_player_2
    else:
        raise ValueError("Unknown person: " + str(person))

    card = hand[card_number]

    for suit_cards in cards_list:
        for value, suit in suit_cards:
            if (value + suit) == card:
                break
        else:
            continue
        break


    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    clean_value = ansi_escape.sub('', value)
    big_space   = 9 - len(clean_value)
    small_space = 4

    card_image = f"""\
┌─────────┐
│{value}{" " * big_space}│
│         │
│         │
│{" " * small_space}{suit}{" " * small_space}│
│         │
│         │
│{" " * big_space}{value}│
└─────────┘"""
    return card_image
    
def display_hand(card_number, person):
    card_images = [generate_card_image(i, person).splitlines() for i in range(card_number)]

    if card_number == 2 and person == "dealer" and turn == 1:

        # Replace the first card with the covered card
        card_images = [generate_card_image(0, person).splitlines()]+[covered_card.splitlines()] 

    # Jede Zeile aller Karten nebeneinander ausgeben
    for lines in zip(*card_images):
        print("  ".join(lines))
        
def extract_card_value(value: str) -> str:
    """
    1) ANSI-Codes weg.
    2) Match: am Stringanfang eine mehrstellige Zahl ODER genau A, K, Q, J.
    3) Rückgabe des gefundenen Substrings oder ''.
    """
    clean = ansi_escape.sub('', value)
    m = re.match(r'^(?:\d+|A|K|Q|J)', clean)
    return m.group(0) if m else ''

def count_best_hand(person):
    def replace_if_K_Q_J(x):
        return 10 if x in ("K", "Q", "J") else x

    if person == "dealer":
        hand = hand_dealer
    elif person == "player_1":
        hand = hand_player_1
    elif person == "player_2":
        hand = hand_player_2
    else:
        raise ValueError("Unknown person: " + str(person))

    cleaned = [extract_card_value(s) for s in hand]
    no_faces = list(map(replace_if_K_Q_J, cleaned))

    coerced = []
    for x in no_faces:
        try:
            coerced.append(int(x))
        except ValueError:
            coerced.append(x)

    value_no_A = sum(x for x in coerced if isinstance(x, int))
    ace_count = sum(1 for x in coerced if x == "A")

    # Alle Asse als 11 zählen, außer das würde das Ergebnis noch weiter erhöhen
    # Also: total = value_no_A + ace_count*11
    # Aber: jedes Ass kann auch nur 1 zählen, falls das besser ist
    # Wir nehmen die beste (höchste) mögliche Wertung, auch wenn sie >21 ist

    # Alle Asse als 11
    total = value_no_A + ace_count * 11

    # Solange total > 21 und es gibt noch Asse als 11, rechne ein Ass zu 1 um
    aces_as_eleven = ace_count
    while total > 21 and aces_as_eleven > 0:
        total -= 10  # Ein Ass zählt jetzt nur noch 1 statt 11
        aces_as_eleven -= 1

    return total

def display_game():

    clear_terminal()
    big_text("blackjack")
    print("Dealer:")
    display_hand(len(hand_dealer), "dealer")
    print()
    print("Spieler 1:")
    display_hand(len(hand_player_1), "player_1")
    print()
#    print("Spieler 2:")
#    display_hand(len(hand_player_2), "player_2")

def update_bet():
    global bet
    clear_terminal()
    big_text("blackjack")
    print("Standard Wetteinsatz: 25€")
    print("Zum ändern eingeben sondst Enter drücken")
    while True:
        try:
            bet_input = input("Wetteinsatz Eingeben:")
            if bet_input.strip() == "":
                bet = 25 # Default bet value
                break
            bet = int(bet_input)
            break
        except ValueError:
            print("Bitte eine gültige ganze Zahl eingeben!")
    return bet

def update_money_value():
    global bet
    if blackjack_player ==True:
        bet = round(bet*1.2)

    googol.update_value_file(result, bet)
    
#######################################################################

def main_blackjack_classic():

    global hand_dealer, hand_player_1, hand_player_2, deck_of_cards
    global turn, result, blackjack_player, bet
    turn = 1
    result = ""
    hand_dealer = []
    hand_player_1 = []
    hand_player_2 = []
    deck_of_cards = []
    blackjack_player = False
    blackjack_dealer = False
    generate_cards_list()
    generate_deck_of_cards()
    generate_hand("dealer")
    generate_hand("player_1")
    display_game()

    if count_best_hand("player_1") == 21 and len(hand_player_1) == 2:
        blackjack_player = True
    if count_best_hand("dealer") == 21 and len(hand_dealer) == 2:
        blackjack_dealer = True

    if blackjack_player and blackjack_dealer:
        display_game()
        print("Beide haben Blackjack! Unentschieden!")
        input("Enter...")
        return
    elif blackjack_player:
        result = "+"
        update_money_value()
        display_game()
        print("Blackjack! Du gewinnst!")
        input("Enter...")
        return
    elif blackjack_dealer:
        result = "-"
        update_money_value()
        display_game()
        print("Dealer hat Blackjack! Du verlierst!")
        input("Enter...")
        return

    # Player's turn
    choice = ""
    while choice != "s":
        display_game()
        if count_best_hand("player_1") == 21:
            print("21!")
            break
        choice = update_hand("player_1")
        if count_best_hand("player_1") > 21:
            result = "-"
            update_money_value()
            display_game()
            print("Bust! Du hast verloren!")
            input("Enter...")
            return

    # Dealer's turn (only if player didn't bust)
    turn = 2
    while count_best_hand("dealer") < 17:
        display_game()
        update_hand("dealer")

    # Final comparison
    dealer_score = count_best_hand("dealer")
    player_score = count_best_hand("player_1")
    
    display_game()
    
    if dealer_score > 21:
        result = "+"
        update_money_value()
        display_game()
        print("Dealer bust! Du gewinnst!")
    elif dealer_score > player_score:
        result = "-"
        update_money_value()
        display_game()
        print("Dealer gewinnt!")
    elif player_score > dealer_score:
        result = "+"
        update_money_value()
        display_game()
        print("Du gewinnst!")
    else:
        display_game()
        result = ""  # Tie, no money change
        print("Unentschieden!")
    
        
    
    input("Enter...")


def blackjack_loop():
    global bet
    big_text("blackjack")
    print(warning_text)
    input("\nEnter...")
    update_bet()

    while True:
        main_blackjack_classic()
        again = ""
        while True:
            if again == "w":
                update_bet()
                again = "j"
            if again in ("j", "n"):
                break
            again = input("Nochmal spielen? (j/n, w für Wetteinsatz ändern):\n ").strip().lower()
            if again not in ("j", "n", "w"):
                print("Ungültige Eingabe!")
        if again != "j":
            break
    return

if __name__ == "__main__":
    blackjack_loop()
