#!/usr/local/bin/python3

import random
import sys

NONE = '-'
BLUE = 'B'
RED = 'R'
ASSASSIN = 'X'

def colorize(color, word):
    if color == BLUE:
        x = 34
    elif color == RED:
        x = 31
    elif color == ASSASSIN:
        x = 45
    else:
        return '{:10s}'.format(word)
    return '\033[{}m{:10s}\033[0m'.format(x, word)

def get_words(filenames):
    all_words = set()
    for filename in filenames:
        with open(filename, 'r') as f:
            all_words = all_words.union([w.rstrip() for w in list(f)])
    words = list(random.sample(all_words, 25))
    random.shuffle(words)
    return words

class Board:
    def __init__(self, words):
        self.firstTeam = random.choice([RED, BLUE])
        second_team = RED if self.firstTeam == BLUE else BLUE

        self.grid = []
        for i in range(7):
            self.grid.append(NONE)
        for i in range(9):
            self.grid.append(self.firstTeam)
        for i in range(8):
            self.grid.append(second_team)
        self.grid.append(ASSASSIN)

        self.words = words
        random.shuffle(self.grid)

    def __str__(self):
        s = "The {} team is first to play.\n".format('red' if self.firstTeam == RED else 'blue')
        s += ''.join(['-' for i in range(21)])
        s += "\n"
        for row in range(5):
            for col in range(5):
                s += '| {} '.format(colorize(self.grid[row*5 + col], self.words[row*5 + col]))
            s += "|\n"
        s += ''.join(['-' for i in range(21)])
        return s

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: {} <dict1.txt> <dict2.txt> ...'.format(sys.argv[0]))
        sys.exit(2)

    words = get_words(sys.argv[1:])
    print(Board(words))
