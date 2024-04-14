#!/bin/user/pyhton

import curses
import time

# Initializing curses
stdscr = curses.initscr()

# Setting the cursor to invisible by inserting 0 as argument
curses.curs_set(0)

Theme='⣾⣽⣻⢿⡿⣟⣯⣷'

for j in range(10):
  for i in Theme:
    print (" ", i," Processing ... ",end="\r")
    time.sleep(0.1)

# Restoring original state
curses.endwin()
