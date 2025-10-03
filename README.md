# 🎰 Blackjack Game - Python Edition

A visually stunning Blackjack card game built with Python and Tkinter, featuring realistic card graphics, smooth gameplay, and an intuitive user interface. Experience the thrill of 21 right on your desktop!

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-FF6F61?style=for-the-badge&logo=python&logoColor=white)

## 🎮 Game Overview

Challenge the dealer in this classic casino card game! Get as close to 21 as possible without going over, and beat the dealer's hand to win. Perfect for both casual players and those looking to practice their Blackjack strategy.

## ✨ Features

### 🃏 Gameplay Features
- **Authentic Blackjack Rules**: Standard casino rules including dealer stands on 17
- **Visual Card Display**: High-quality PNG card images for immersive gameplay
- **Smart Ace Handling**: Automatic ace value adjustment (11 or 1) to prevent busting
- **Dealer AI**: Realistic dealer behavior following traditional house rules
- **Hidden Card Mechanic**: Dealer's second card remains hidden until the showdown

### 🎨 Visual Features
- **Stunning Card Graphics**: Professional card images for all 52 cards in the deck
- **Real-time Score Display**: Live score tracking for both player and dealer
- **Responsive Layout**: Clean, organized interface with separate frames for each hand
- **Card Rank Labels**: Easy identification of card values
- **Dynamic Updates**: Smooth transitions as cards are dealt and revealed

### 🎯 Game Mechanics
- **Full 52-Card Deck**: Complete standard deck with all suits (Hearts, Diamonds, Clubs, Spades)
- **Proper Shuffling**: Randomized deck shuffle at the start of each game
- **Instant Win Detection**: Automatic detection of busts, wins, and ties
- **Easy Controls**: Simple three-button interface (Hit, Stand, New Game)

## 🚀 Getting Started

### Prerequisites
- Python 3.6 or higher
- Tkinter (usually comes pre-installed with Python)
- Card image assets in PNG format

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/NeonWest/BlackJack-Game.git
   cd BlackJack-Game
   ```

2. **Ensure you have the card images**
   - Create a folder named `PNG-cards/`
   - Place all 52 card images in this folder
   - Images should be named: `{rank}_of_{suit}.png`
   - Example: `ace_of_hearts.png`, `10_of_spades.png`

3. **Run the game**
   ```bash
   python blackjack.py
   ```

## 🎲 How to Play

### Game Rules
1. **Objective**: Get closer to 21 than the dealer without going over
2. **Card Values**:
   - Number cards (2-10): Face value
   - Face cards (J, Q, K): Worth 10 points
   - Aces: Worth 11 points (automatically becomes 1 if needed to prevent bust)

### Controls
- **Hit**: Draw another card to increase your hand value
- **Stand**: Keep your current hand and let the dealer play
- **New Game**: Start a fresh round with a newly shuffled deck

### Gameplay Flow
1. Game starts with both you and the dealer receiving 2 cards
2. Dealer's second card is hidden
3. Choose to **Hit** (draw more cards) or **Stand** (end your turn)
4. If you bust (go over 21), you lose immediately
5. When you stand, the dealer reveals their hidden card
6. Dealer must hit until reaching 17 or higher
7. Winner is determined by who has the higher hand without busting

### Winning Conditions
- ✅ **You Win**: Your score is higher than dealer's (without busting) OR dealer busts
- ❌ **You Lose**: You bust OR dealer's score is higher than yours
- 🤝 **Tie**: Both you and dealer have the same score

## 💻 Technical Implementation

### Architecture Highlights

**Object-Oriented Card System**
```python
# Deck representation using tuples
deck = [(rank, suit) for rank in ranks for suit in suits]

# Smart hand value calculation with ace handling
def hand_value(hand):
    # Automatically adjusts ace values to prevent busting
    while value > 21 and aces:
        value -= 10
        aces -= 1
```

**Image Caching System**
```python
# Efficient image loading and caching
card_photo_images = {}  # Prevents redundant image loading
resized_image = original_image.subsample(scale_factor, scale_factor)
```

**Dynamic UI Updates**
- Frames are rebuilt on each update for clean state management
- Conditional rendering for hidden dealer card
- Real-time score calculations

### File Structure
```
📁 BlackJack-Game/
├── 📄 blackjack.py           # Main game logic and GUI
├── 📁 PNG-cards/             # Card image assets
│   ├── 2_of_hearts.png
│   ├── ace_of_spades.png
│   └── ... (all 52 cards)
└── 📄 README.md              # This file
```

## 🎨 Customization

### Adjusting Card Size
Modify the `scale_factor` variable to change card dimensions:
```python
scale_factor = 3  # Higher = smaller cards, Lower = larger cards
```

### Changing Card Images
Simply replace the PNG files in the `PNG-cards/` folder while maintaining the naming convention:
```
{rank}_of_{suit}.png
```

## 🔧 Code Features

- **Clean Separation of Concerns**: Logic, UI, and game state are well-organized
- **Global State Management**: Efficient handling of deck and hand states
- **Event-Driven Architecture**: Button callbacks control game flow
- **Resource Management**: Smart image caching prevents memory bloat
- **Error Handling**: Graceful handling of missing images and edge cases

## 🎯 Future Enhancements

Potential features for future versions:
- 💰 Betting system with chip management
- 📊 Win/loss statistics tracking
- 🎵 Sound effects for card dealing and wins
- 🏆 Achievement system
- 👥 Multiplayer support
- 💾 Save/load game state
- 🎨 Multiple card deck themes

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional card deck designs
- Enhanced UI/UX features
- Game rule variations (Spanish 21, Double Exposure, etc.)
- Performance optimizations
- Bug fixes and improvements

## 📝 License

This project is open source and available for educational and personal use.

## 👤 Author

**Omar Atakishiyev**
- GitHub: [@NeonWest](https://github.com/NeonWest)

## 🙏 Acknowledgments

- Built with Python's Tkinter for cross-platform compatibility
- Implements authentic casino Blackjack rules
- Designed for both beginners learning Python and card game enthusiasts

## 📚 Learning Outcomes

This project demonstrates:
- ✅ Python GUI development with Tkinter
- ✅ Event-driven programming
- ✅ State management in games
- ✅ Image handling and optimization
- ✅ Game logic implementation
- ✅ Object-oriented programming principles

---

🎰 **Ready to play?** Clone the repo and try your luck at 21!

⭐ **Enjoyed the game?** Give it a star on GitHub!
