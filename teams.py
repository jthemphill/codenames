#!/usr/local/bin/python3

import random
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python {} leaders.txt players.txt'.format(sys.argv[0]))
        exit(2)

    leaders_txt = sys.argv[1]
    players_txt = sys.argv[2]

    with open(leaders_txt, 'r') as f:
        leaders = [x.rstrip() for x in f]

    red_leader, blue_leader = random.sample(leaders, 2)

    with open(players_txt, 'r') as f:
        players = [x.rstrip() for x in f]

    players = [x for x in players if x != red_leader and x != blue_leader]

    if len(players) < 2:
        print('You need at least two non-leaders in order to play Codenames.')
        exit(2)

    random.shuffle(players)
    blue_players = players[:len(players) / 2]
    red_players = players[len(players) / 2:]

    print('Blue leader: {}'.format(blue_leader))
    print('Blue team: {}'.format(blue_players))
    print()
    print('Red leader: {}'.format(red_leader))
    print('Red team: {}'.format(red_players))
