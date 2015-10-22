Very quick and dirty way to set up a game of Codenames. Codenames was
made by Vlaada Chvatil, not me, you should totally buy Codenames when
it comes out / is no longer sold out, etc.

Usage:
======

You'll need a laptop (this might only work on Mac or Linux) with
Python, a pad of paper, and black / red / blue writing implements.

Choose codemasters and teams however you want. If you want to choose
randomly, write the people who would like to be leaders down in
`leaders.txt`, write the players' names down in a file like
`players.txt` and run

    python teams.py leaders.txt players.txt

if all the players are willing to be leaders, you can just run:

    python teams.py players.txt players.txt

Then give the laptop to the two codemasters and run

    python grid.py good-words/*

Which will use all the words defined in the good-words folder. The
laptop will be your key for the game, so only the codemasters should
be able to see it. Now have the codemasters write the words on the pad
of paper, and you're good to go!

Easy ways to help
=================

This is nowhere near complete, and probably not even useful to you -
it was just the minimal amount of code I had to write to start playing
games with my friends. Here are some ways you can improve this:

* I don't have the official words. Every game I've played with the
  words in good-words.txt has been fun, but feel free to pull request
  if you encounter an unfun word, if you have some good word ideas, or
  if you have the official dictionary.
* I use a mac, so I'm not sure what the experience is for
  non-programmers or Windows users. Maybe the colors are bad? Open an
  issue if there's something wrong.
* I think a web interface could be nice. If you want to be able to use
  this on a tablet or windows computer, open an issue or comment on
  the issue to motivate me. Or just write it yourself, whatever you
  feel like doing really.
