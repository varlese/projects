Hi there!

My Rock, Paper, Scissors game has five different player options.

- Player: which creates a player who plays only "rock"

- Random Player: which creates a play who selects from rock, paper, or scissors at random

- Human Player: which creates a player that requests input to play the game

- Cycle Player: which creates a player that automatically cycles through rock, paper, and scissors

- Refelct Player: which creates a player that automatically mimics the last move played by the game's other player


To play:

1. Start the Python processor in your Terminal.

2. Import rps.py

3. Create two new players, i.e. "Erica = rps.HumanPlayer()"

4. Create a new game and pass it the player names as two parameters, i.e. "New = rps.Game(Erica, Cycle)"

5. Play a new game, i.e. "New.play_game()"


To change the types of player options available, adjust the players included on line 125 in the program. By default, the game is set up to play with a human player and a random player. 
