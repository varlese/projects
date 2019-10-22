#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

# Player Classes


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        human_play = input("Rock, paper, scissors...shoot! ").lower()
        if human_play in moves:
            return human_play
        else:
            print("That's not in the game! Try again.")
            self.move()


class ReflectPlayer(Player):
    def __init__(self):
        self.my_move = ""
        self.their_move = moves[0]

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

    def move(self):
        return self.their_move


class CyclePlayer(Player):
    def __init__(self):
        self.cycle = -1

    def move(self):
        if self.cycle < 2:
            self.cycle += 1
        else:
            self.cycle = 0
        return moves[self.cycle]


# Evaluating scores
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Game classes
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.scores = []

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        player1_win = beats(move1, move2)
        player2_win = beats(move2, move1)
        winner = 0
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if player1_win:
            winner = 1
            print("You win!")
        elif player2_win:
            winner = 2
            print("The computer wins!")
        else:
            print("Tie!")
        return winner

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.scores.append(self.play_round())
        p1_score = self.scores.count(1)
        p2_score = self.scores.count(2)
        print(f"Your score is {p1_score} and the computer's score" +
              " is {p2_score}.")
        keep_playing = input("Would you like to keep playing? y/n ").lower()
        if keep_playing == "y":
            self.play_game()
        else:
            if p1_score > p2_score:
                print("You win! Game over :) ")
            elif p2_score < p1_score:
                print("Sorry, you lost! Game over :)")
            else:
                print("It's a tie! Game over :)")


# Remove comments to active different types of players. Options are:
# Player()
# HumanPlayer()
# RandomPlayer()
# CyclePlayer()
# ReflectPlayer()
if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
