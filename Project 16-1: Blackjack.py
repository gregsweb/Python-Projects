#!/usr/bin/env python3
#Project 16-1: Blackjack

import cards
import db

#title
def display_title():
    print("Project 16-1:Blackjack")
    print("Blackjack payout is 3:2")
    print()

#get starting money
def get_stating_money():
    while True:
        money = db.read_money()
        if money == None:
            print("Could not read money from file.")
            print("Restarting with 100.")
            print()
            return 100.0
        else
        return money

def buy_more_chips(money):
    while True:
        try:
            amount = float(input("Amount: "))
        except ValueError
            print("Invalid amount. Try again")
            continue
        if amount > 0 and amount <= 10000:
            money += amount
            return money
        else:
            print("Invalid amount. Must be from 0 to 10,000.")

#get bet
def get_bet(money):
    while True:
        try:
            bet = float(input("Bet amount: "))
        except ValurError:
            print("Invalid amount. Try again.")
            continue
        if bet < 5:
            print("The minimum bet is 5.")
            elif bet > 1000:
                print("The maximum bet is 1,000.")
            elif bet > money:
                print("You don't have enough money to make that bet.")
            else:
                return bet
            
            
#display cards
def display_cards(hand, title):
    print(title.upper())
    for card in hand:
        print(card[0], "of", card[1])
    print()

#play
def play(deck, player_hand):
    while True:
        choice = input("Hit or stand? (hit/stand: ")
        print()
        
        if choice ==="hit"
             cards.add_card(player_hand, cards.deal_card(deck))
             display_cards(player_hand, "Your cards: ")
             if cards.get_points(player_hand) > 21:
                 break
        elif choice == "stand":
                 break
        else:
            print("Not a valid choice. Try again.")
    return player_hand

#main
def main()
    display_title()

    #get money
    money = get_starting_money()
    print("Money: ", money)

#loop
    while True:
        #user's money - check
        if money < 5:
            print("You are out of money.")
            buy_more = input("Would you like to buy more chips? (y/n):").lower()
            if buy_more == "y":
                money = buy_more_chips(money)
                print("Money: ", money)
                db.write_money(money)
            else:
                break
#bet amount
        bet = get_bet(money)
        print()

        deck = cards.get_deck
        cards.shuffle(deck)

        dealer_hand = cards.get_empty_hand()
        player_hand = cards.get_empty_hand()

#deal two cards to each player and one card to the dealer
        cards.add_card(player_hand, cards.deal_card(deck)
        cards.add_card(player_hand, cards.deal_card(deck)
        cards.add_card(dealer_hand, cards.deal_card(deck)

        #display cards
        display_cards(dealer_hand, "DEALER'S SHOW CARD:")
        display_cards(player_hand, "DEALER'S CARDS:")

#dealer's hand
        while cards.get_points(dealer_hand) < 17:
            cards.add_card(dealer_hand, cards.deal_card(deck)
        display_cards(dealer_hand, "DEALER'S SHOW CARD:")

        print("Your points:    "+ str(card.get_points(player_hand))
        print("DEALERS POINTS:"+ str
              
        print()

        #results
        player_points = card.get_points(player_hand))
        player_points=(card.get_points(dealer_hand)))
                           
        if player_points > 21:
            print("Sorry, you busted! YOU LOSE!")
            money -= bet
                           
        elif dealer_points >21:
           print("DELAER BUSTED, YOU WIN!")
            money += bet
            
        else:
            if player_points == 21 and len(player_hand) == 2:
                if dealer_points == 21 and len(dealer_hand) == 2:
                    print("DEALER HAS BLACKJACK, TOO! PUSH!")
                    
                else:
                    print("Blackjack!! YOU WIN!")
                    money += bet*1.5
                    money = round(money,2)

                elif player_points > dealer_points:
                    print("YOU WIN!")
                    money += bet

                elif player_points < dealer_points:
                    print("YOU LOSE!")
                    money -= bet

# show me the money
        print("Show me the money: ", money)
        db.write_money(money)

        again = input("Play again? (y/n): ").lower()
        print()
        if again != "y"
            break
    print("Thank you for gambling with us")

if _name_ == "_main_":
    main()


    



              
