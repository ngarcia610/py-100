import tkinter
import random


def load_images(card_images):
    suits = ["heart", "club", "diamond", "spade"]
    picture_cards = ["jack", "queen", "king"]
    extension = "png"

    # for each suit, retrieve the image for the cards from cards directory
    for suit in suits:
        # non picture cards
        for card in range(1, 11):
            name = f"cards/{str(card)}_{suit}.{extension}"
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))

        # picture cards
        for card in picture_cards:
            name = f"cards/{str(card)}_{suit}.{extension}"
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


def _deal_card(frame):
    next_card = deck.pop(0)
    deck.append(next_card)
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side="left")
    return next_card


def score_hand(hand):
    # calculate total score of all cards in the list
    # only one ace can have value 11, reducing to 1 if the hand would otherwise bust
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value
        if score > 21 and ace:
            score -= 10
            ace = False
    return score


def deal_dealer():
    global player_games
    global dealer_games
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(_deal_card(dealer_card_frame))    
        dealer_score = score_hand(dealer_hand)

    dealer_score_label.set(dealer_score)
    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins!")
        dealer_games += 1
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
        player_games += 1
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
        dealer_games += 1
    else:
        result_text.set("Draw!")
    dealer_score_tally.set(dealer_games)
    player_score_tally.set(player_games)
    dealer_button["state"] = "disabled"
    player_button["state"] = "disabled"


def deal_player():
    global dealer_games
    if score_hand(player_hand) < 21:
        player_hand.append(_deal_card(player_card_frame))
        player_score = score_hand(player_hand)

        player_score_label.set(player_score)
        if player_score > 21:
            result_text.set("Dealer Wins!")
            dealer_games += 1
            dealer_score_tally.set(dealer_games)


def new_game():
    global dealer_card_frame
    global player_card_frame

    result_text.set("")
    dealer_card_frame.destroy()
    player_card_frame.destroy()
    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)
    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)
    dealer_hand.clear()
    player_hand.clear()
    deal_player()
    dealer_hand.append(_deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()
    dealer_button["state"] = "normal"
    player_button["state"] = "normal"


def shuffle():
    random.shuffle(deck)
    result_text.set("Deck shuffled!")


def play():
    mainWindow.mainloop()


mainWindow = tkinter.Tk()
mainWindow.title("Blackjack")
mainWindow.geometry("640x480")
mainWindow.configure(background="green")

player_score_tally = tkinter.IntVar()
dealer_score_tally = tkinter.IntVar()
player_score_label = tkinter.Label(mainWindow, textvariable=player_score_tally, background="green", fg="white")
player_score_label.grid(row=2, column=4)
dealer_score_label = tkinter.Label(mainWindow, textvariable=dealer_score_tally, background="green", fg="white")
dealer_score_label.grid(row=1, column=4)
player_games = 0
dealer_games = 0
player_score_tally.set(player_games)
dealer_score_tally.set(dealer_games)

result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text, background="green", fg="white", font="calibri 12 bold")
result.grid(row=0, column=0, columnspan=3)

card_frame = tkinter.Frame(mainWindow, relief="sunken", borderwidth=1, background="green")
card_frame.grid(row=1, column=0, sticky="ew", columnspan=3, rowspan=2)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)

# embed frame to hold card images - dealer
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, sticky="ew", rowspan=2)

player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)

# embed frame to hold card images - player
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

# button frame
button_frame = tkinter.Frame(mainWindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")

# the command parameter defines what happens when the button is pushed
# calling a function without parentheses returns a reference to the function without actually executing it
# the function needs to be executed when the button is pressed by the user, not when the button is created
dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)
player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)
new_game_button = tkinter.Button(button_frame, text="New Game", command=new_game)
new_game_button.grid(row=0, column=2)
shuffle_button = tkinter.Button(button_frame, text="Shuffle", command=shuffle)
shuffle_button.grid(row=0, column=3)

# load cards
cards = []
load_images(cards)  # tuple of values and images


# create a new deck of cards and shuffle them
deck = list(cards)
random.shuffle(deck)

# create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

deal_player()
dealer_hand.append(_deal_card(dealer_card_frame))
dealer_score_label.set(score_hand(dealer_hand))
deal_player()

if __name__ == "__main__":
    mainWindow.mainloop()
