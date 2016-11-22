from Maze import *
from sets import Set
from Point import *
import heapq


class Agent:

    def __init__(self, maze):
        self.__maze = maze
        self.__starting_point = maze.get_starting_point()
        self.__starting_point.cost = 0
        self.__ending_point = maze.get_ending_point()
        self.__current_position = self.__starting_point
        self.__visited_points = Set()  # Used to save the visited nodes
        print("Agent initiated. "
              "Starting position: {0}. "
              "Ending position: {1}. "
              "Current position: {2} "
              .format(
                    self.__starting_point, self.__ending_point,
                    self.__current_position
                )
              )

    def determine_possible_moves(self):
        """
        (None) -> None
        This method should no be used
        with me current logic the algorith is implemented.
        It was implemented for debugging reasons
        """
        north = False
        east = False
        south = False
        west = False
        # Try to move west
        if ((self.__current_position.x - 1) >= 0):
            if (not maze.is_wall(Point(
                [
                    self.__current_position.x - 1,
                    self.__current_position.y
                ]
            ))):
                west = True
        # Try to move east
        if ((self.__current_position.x + 1) <= maze.get_maze_x_size()):
            if (not maze.is_wall(Point(
                [
                    self.__current_position.x + 1,
                    self.__current_position.y]
            ))):
                east = True
        # Try to move north
        if ((self.__current_position.y - 1) >= 0):
            if (not maze.is_wall(Point(
                [
                    self.__current_position.x,
                    self.__current_position.y - 1
                ]
            ))):
                north = True
        # Try to move south
        if ((self.__current_position.y + 1) <= maze.get_maze_y_size()):
            if (not maze.is_wall(Point(
                [
                    self.__current_position.x,
                    self.__current_position.y + 1
                ]
            ))):
                south = True
        print(
            "Possible moves: "
            "North: {0}, "
            "East: {1}, "
            "South: {2}, "
            "West: {3}"
            .format(north, east, south, west)
            )

    def set_current_position(self, point):
        """
        (Point) -> None
        It should not be used under normal circumstances.
        The method is implemented for debugging purposes
        """
        self.__current_position = point

    def __search(self, point):
        """
        (Point) -> None

        A breadth-first search that is efficient enough
        to find the solution.
        The agent searches the neighbours of its current point
        until it finds the goal point
        """
        if point == self.__ending_point:
            print "Found ending point at ({0}, {1})".format(point.x, point.y)
            return True
        elif self.__maze.is_wall(point):
            print "Wall at ({0}, {1})".format(point.x, point.y)
            return False
        elif len(self.__visited_points) and point in self.__visited_points:
            print "Visited at ({0}, {1})".format(point.x, point.y)
            return False
        print "Visiting ({0}, {1})".format(point.x, point.y)
        # mark as visited
        self.__visited_points.add(point)
        # explore neighbours
        for neighbour in self.__find_neighbours(point):
            if self.__search(neighbour):
                return True
        return False

    def __find_neighbours(self, point):
        neighbours = []
        if (
            point.x + 1 <= self.__maze.get_maze_x_size() and
            not self.__maze.is_wall(Point([point.x + 1, point.y]))
        ):
            neighbours.append(Point([point.x + 1, point.y]))
        if (
            point.x - 1 >= 0 and
            not self.__maze.is_wall(Point([point.x - 1, point.y]))
        ):
            neighbours.append(Point([point.x - 1, point.y]))
        if (
            point.y + 1 <= self.__maze.get_maze_y_size() and
            not self.__maze.is_wall(Point([point.x, point.y + 1]))
        ):
            neighbours.append(Point([point.x, point.y + 1]))
        if (
            point.y - 1 >= 0 and
            not self.__maze.is_wall(Point([point.x, point.y - 1]))
        ):
            neighbours.append(Point([point.x, point.y - 1]))
        return neighbours

    def breadth_first_search(self):
        self.__search(self.__current_position)

    def a_star_search(self):
        """
        (None) ->None

        An implementation of A* algorithm.
        We calculate the cost for all points
        from the starting point and keep
        the neighbour of the goal point
        with the lowest cost.
        We make the assumption that the heuristic function h(n)
        is always zero and the cost is the movement
        from one point to another.
        """

        points = []
        heapq.heappush(points, (self.__starting_point, 0))

        # Dictionary containing the parent of each node.
        # The parent is the path from the starting point
        # to this point with the lowest cost
        parent = {}

        # Dictionary containing the cost
        # to each point from the starting point
        cost_so_far = {}
        parent[self.__starting_point] = None
        cost_so_far[self.__starting_point] = 0

        while len(points) > 0:
            current = heapq.heappop(points)[0]
            if current == self.__ending_point:
                break

            for next in self.__find_neighbours(current):
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost
                    heapq.heappush(points, (next, priority))
                    parent[next] = current

        path = self.__reconstruct_path(parent, cost_so_far)

        print "--Lowest cost path--"
        for point in path:
            print point

    def __reconstruct_path(self, parent, cost):
        # Append the ending point to the path
        path = [self.__ending_point]

        # The maximum cost is if we need to walk through the whole maze
        # to find the ending point
        lowest_cost = (
            self.__maze.get_maze_y_size() *
            self.__maze.get_maze_x_size()
            )
        # Find the neighbour of the ending point
        # with the lowest cost
        ending_point_neighbours = (
            self.__find_neighbours(self.__ending_point)
            )
        for neighbour in ending_point_neighbours:
            try:
                if lowest_cost > cost[neighbour]:
                    lowest_cost = cost[neighbour]
                    point = neighbour

                path.append(point)
            except KeyError:
                continue

        # Reconstruct the path
        # by each point's parent
        while parent[point] is not None:
            point = parent[point]
            path.append(point)

        # Reverse the list to start
        # from the starting point
        path.reverse()
        return path

# if __name__ == "__main__":
#    agent = Agent(maze1)
#    agent.a_star_search()
