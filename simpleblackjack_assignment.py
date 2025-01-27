import tkinter as tk
from tkinter import PhotoImage
import random

IMAGE_FOLDER = "PNG-cards/"
scale_factor = 3 

root = tk.Tk()
root.title("Blackjack with Card Images")

deck = []
player_hand = []
dealer_hand = []

card_photo_images = {}

def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    return [(rank, suit) for rank in ranks for suit in suits]

def shuffle_deck():
    global deck
    deck = create_deck()
    random.shuffle(deck)

def deal_card(hand):
    card = deck.pop()
    hand.append(card)
    return card

def get_card_image(card):
    rank, suit = card
    file_path = f"{IMAGE_FOLDER}{rank.lower()}_of_{suit.lower()}.png"
    if card not in card_photo_images:
        original_image = PhotoImage(file=file_path)
        resized_image = original_image.subsample(scale_factor, scale_factor)
        card_photo_images[card] = resized_image
    return card_photo_images[card]

def hand_value(hand):
    value = 0
    aces = 0
    for card, suit in hand:
        if card in 'JQK':
            value += 10
        elif card == 'A':
            value += 11
            aces += 1
        else:
            value += int(card)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def start_new_game():
    global player_hand, dealer_hand
    shuffle_deck()
    player_hand = []
    dealer_hand = []
    deal_card(player_hand)
    deal_card(player_hand)
    deal_card(dealer_hand)
    deal_card(dealer_hand)
    update_display(show_dealer=False)
    result_label.config(text="")

def hit():
    deal_card(player_hand)
    if hand_value(player_hand) > 21:
        result_label.config(text="You bust! Dealer wins.")
        update_display(show_dealer=True)
    else:
        update_display(show_dealer=False)

def stand():
    while hand_value(dealer_hand) < 17:
        deal_card(dealer_hand)
    update_display(show_dealer=True)
    player_score = hand_value(player_hand)
    dealer_score = hand_value(dealer_hand)
    if dealer_score > 21 or player_score > dealer_score:
        result_label.config(text="You win!")
    elif player_score == dealer_score:
        result_label.config(text="It's a tie!")
    else:
        result_label.config(text="Dealer wins!")

def update_display(show_dealer=False):
    for widget in player_hand_frame.winfo_children():
        widget.destroy()
    for widget in dealer_hand_frame.winfo_children():
        widget.destroy()

    player_score_label.config(text=f"Your Score: {hand_value(player_hand)}")
    for card in player_hand:
        card_img = get_card_image(card)
        card_rank = card[0]  
        if card_img:
            frame = tk.Frame(player_hand_frame)  
            frame.pack(side="left", padx=5)
            img_label = tk.Label(frame, image=card_img)
            img_label.pack()  
            text_label = tk.Label(frame, text=card_rank)  
            text_label.pack()  

    if show_dealer:
        dealer_score_label.config(text=f"Dealer's Score: {hand_value(dealer_hand)}")
        for card in dealer_hand:
            card_img = get_card_image(card)
            if card_img:
                label = tk.Label(dealer_hand_frame, image=card_img)
                label.pack(side="left")
    else:
        dealer_score_label.config(text="Dealer's Score: ??")
        if dealer_hand:
            card_img = get_card_image(dealer_hand[0])
            if card_img:
                label = tk.Label(dealer_hand_frame, image=card_img)
                label.pack(side="left")
            hidden_label = tk.Label(dealer_hand_frame, text="[Hidden]")
            hidden_label.pack(side="left")

player_frame = tk.Frame(root)
dealer_frame = tk.Frame(root)
control_frame = tk.Frame(root)

player_frame.pack(pady=10)
dealer_frame.pack(pady=10)
control_frame.pack(pady=10)

player_hand_frame = tk.Frame(player_frame)
dealer_hand_frame = tk.Frame(dealer_frame)
player_hand_frame.pack()
dealer_hand_frame.pack()

tk.Label(player_frame, text="Player's Hand").pack()
player_score_label = tk.Label(player_frame, text="Your Score: ")
player_score_label.pack()
tk.Label(dealer_frame, text="Dealer's Hand").pack()
dealer_score_label = tk.Label(dealer_frame, text="Dealer's Score: ??")
dealer_score_label.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack()
tk.Button(control_frame, text="Hit", command=hit).grid(row=0, column=0)
tk.Button(control_frame, text="Stand", command=stand).grid(row=0, column=1)
tk.Button(control_frame, text="New Game", command=start_new_game).grid(row=0, column=2)

start_new_game()
root.mainloop()
