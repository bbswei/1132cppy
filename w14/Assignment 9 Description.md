# UNO Simulator
Description
In this assignment, you’ll build a simplified UNO simulator that plays out a game step-by-step based on clear and consistent rules.

The game uses number cards, action cards (Skip, Reverse, Draw Two), and wild cards (Wild, Wild Draw Four). Players take turns playing a card that matches the color or value of the top card on the pile — or drops a Wild when things get tricky.

Card Type	     	   Effect
Skip	         	   The next player is skipped.
Reverse	         	   The playing order is reversed.
Draw Two (+2)	 	   The next player draws 2 cards.
Wild	         	   Can be played on any card. The player must choose a new color.
Wild Draw Four (+4)	   Can be played on any card. The player must choose a new color. The next player draws 4 cards.

Your job is to manage the players, turns, card effects, and decision-making — and make sure everything runs smoothly until someone wins!

### 🎮 Game Rules
- Game Setup
There are exactly 5 players (Player 0 to Player 4) in every game. Each player is dealt 5 cards at the beginning in round-robin order (starting from Player 0, in ascending order).
The first card from the remaining deck is flipped and placed on the discard pile as the initial top_card after dealing cards for all players.
No effect is triggered by the starting card, even if it is a special card (Skip, Draw Two, Reverse, Wild, or Draw Four). However, its color and value still determine which cards Player 0 is allowed to play.
If the initial top_card is a Wild or Draw Four (which normally has no color), treat it as Red for the purpose of determining valid plays.
The game starts with Player 0, and proceeds in ascending order of player IDs.

- Turn Sequence
On a player's turn, they must play one card (according to the following selection rule) that matches the current top_card in color or value/type, or play a Wild card.
If no playable card is available, the player draws one card from the top of the draw pile:
If the drawn card is playable, it must be played immediately. Otherwise, the player keeps the card and skips the turn.
If the drawn pile is empty, skip drawing.

- Selection Rule
Card Selection Rule
When a player has multiple playable cards, they must choose one to play according to the following priority:

- Number cards
Skip
Reverse
Draw Two
Wild
Wild Draw Four
If multiple cards have the same priority, choose the first one according to hand order (FIFO).

- Wild Color Selection Rule
When a player plays a Wild or Wild Draw Four, they must choose a new color:

Choose the color that appears most frequently in the player’s remaining hand.
If tied, use fixed order: Red > Yellow > Green > Blue
If no colored cards remain, choose Red by default.

🛑 Game End
The game ends immediately when any player has no cards left, then that player is declared the winner.
You can assume that all test cases are guaranteed to eventually produce a winner.


