from Point import Point


class Maze:

    def __init__(self, file_path):
        self.__maze_structure = self.__load_maze(file_path)
        self.__starting_point = self.__find_starting_point()
        self.__ending_point = self.__find_ending_point()
        # We subtract 1 for better support of the comparison
        # in case the agent tries to move out of bounds
        self.__maze_y_size = len(self.__maze_structure) - 1
        self.__maze_x_size = len(self.__maze_structure[-1]) - 1
        print "Starting point: {0}".format(self.__starting_point)
        print "Ending point: {0}".format(self.__ending_point)
        print "Maze size: {0}, {1}".format(
            self.__maze_x_size,
            self.__maze_y_size
            )

    def __load_maze(self, file_path):
        maze_structure = []
        with open(file_path) as file:
            for line in file:
                maze_line = []
                # We use strip to clean the string
                # from the return character (\n)
                for point in line.strip():
                    maze_line.append(point)
                maze_structure.append(maze_line)
        print "Maze structure successfully loaded"
        return maze_structure

    def __find_starting_point(self):
        for maze_line in self.__maze_structure:
            for maze_point in maze_line:
                if maze_point == 'S':
                    # We pass first the column (x coordinate)
                    # and then the line (y coordinate)
                    return Point(
                        [
                            maze_line.index(maze_point),
                            self.__maze_structure.index(maze_line)
                        ]
                    )

    def __find_ending_point(self):
        for maze_line in self.__maze_structure:
            for maze_point in maze_line:
                if maze_point == 'G':
                    # We pass first the column (x coordinate)
                    # and then the line (y coordinate)
                    return Point(
                        [
                            maze_line.index(maze_point),
                            self.__maze_structure.index(maze_line)
                        ]
                    )

    def get_starting_point(self):
        return self.__starting_point

    def get_ending_point(self):
        return self.__ending_point

    def is_wall(self, point):
        return self.__maze_structure[point.y][point.x] == 'X'

    def get_maze_x_size(self):
        return self.__maze_x_size

    def get_maze_y_size(self):
        return self.__maze_y_size

# maze1 = Maze("mazes/maze")
