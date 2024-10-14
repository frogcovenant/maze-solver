from TreeNode import TreeNode
import os


FOLDER_PATH = 'mazes'
START_CHAR = 'A'
GOAL_CHAR = 'B'
WALL_CHAR = '0'


def getMazeMatrixFromFile(filePath):
    maze = []
    start = None
    goal = None

    f = open(filePath)
    next(f) # skip first line with maze size

    for line_pos, line in enumerate(f):
        maze.append([])
        for character_pos, character in enumerate(line[:-1]): # skip the newline character
            maze[line_pos].append(character)
            if character == START_CHAR:
                start = (line_pos, character_pos) # (row, column)
            elif character == GOAL_CHAR:
                goal = (line_pos, character_pos) # (row, column)

    return maze, start, goal


def getValidChildren(maze, coordinates):
    rows = len(maze)
    cols = len(maze[0])
    x, y = coordinates
    valid_children = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy

        # Check if the new coordinates are within the maze bounds
        if 0 <= new_x < rows and 0 <= new_y < cols:
            # Optionally, check if the cell is passable (1 represents a valid path)
            if maze[new_x][new_y] != WALL_CHAR:  # Assuming 1 represents open space and 0 is a wall
                valid_children.append((new_x, new_y))

    return valid_children


def buildMazeTree(currentNode, position):
    global maze, addedToTree, goal, goalFound
    # Get valid children from the current position
    currentChildren = getValidChildren(maze, position)
    
    # Recursively add each child to the current node
    for child in currentChildren:
        # Create a new tree node for each child
        childNode = TreeNode(child)
        # Add this child node to the current node's children
        if child not in addedToTree:
            currentNode.add_child(childNode)
            addedToTree.add(child)
        else: continue
        # stop condition
        if goal == child or goalFound: 
            goalFound = True
            return
        # Recursively build the tree from the child node
        buildMazeTree(childNode, child)


if __name__ == '__main__':
    for filePath in os.listdir(FOLDER_PATH):
        maze, start, goal = getMazeMatrixFromFile(f"{FOLDER_PATH}\{filePath}")
        addedToTree = set() # keep track of added nodes to not add them twice to the tree
        goalFound = False # keep track if we found the goal to now make the tree bigger than we need

        print('CURRENT MAZE:')
        for line in maze: print(line)
        print(f'\nStart: {start}')
        print(f'Goal:  {goal}\n')
        
        mazeTree = TreeNode(start)
        buildMazeTree(mazeTree, start)
        print('NODE TREE FOR MAZE:')
        print(mazeTree)

        print(f'PATH: {mazeTree.solve(goal)}\n\n')
