import argparse
from Agent import *
from Maze import *

parser = argparse.ArgumentParser(description=(
        "Load a maze "
        "and let an agent navigate inside")
                                     )
parser.add_argument('-f', type=str,
                    help='the path for the maze')
parser.add_argument('--search', type=str,
                    help='the type of the search simple, a_star')

args = parser.parse_args()

maze_file = args.f
a_star = True
if (args.search):
    a_star = args.search == "a_star"

maze = Maze(maze_file)
agent = Agent(maze)
if (a_star):
    agent.a_star_search()
else:
    agent.breadth_first_search()
