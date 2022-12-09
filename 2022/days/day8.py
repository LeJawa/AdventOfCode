from argument_parser import get_config_from_individual_day
import os

from day import Day
DAY = 8
PRINT_OUTPUT_MANUAL_OVERRIDE = True

class Forest:
    def __init__(self, lines: list[str]) -> None:
        
        trees: list[list[int]] = []
        
        for line in lines:
            line = line.strip()
            trees.append([])
            for c in line:
                trees[-1].append(int(c))
        
        self.trees = trees
        
    def calculate_inside_visibility(self) -> None:
        max_score = 0
        self.scenic_score: list[list[int]] = []
        
        for i in range(len(self.trees)):
            self.scenic_score.append([])
            for j in range(len(self.trees[i])):
                self.scenic_score[i].append(self.scenic_score_along_row(i, j) * self.scenic_score_along_column(i, j))
                if self.scenic_score[i][j] > max_score:
                    max_score = self.scenic_score[i][j]
                    best_tree = (i, j)
        
        self.best_tree = best_tree
                
    def scenic_score_along_column(self, x: int, y: int) -> int:
        trees_to_top = 0
        trees_to_bottom = 0
        tree_height = self.trees[x][y]
        for i in range(1, len(self.trees[0])):
            if x+i >= len(self.trees):
                break
            
            trees_to_bottom += 1
            if self.trees[x+i][y] >= tree_height:
                break
            
        
        for i in range(1, len(self.trees[0])):
            if x-i < 0:
                break
            
            trees_to_top += 1
            if self.trees[x-i][y] >= tree_height:
                break
        
        return trees_to_bottom * trees_to_top
                
    def scenic_score_along_row(self, x: int, y: int) -> int:
        trees_to_left = 0
        trees_to_right = 0
        tree_height = self.trees[x][y]
        
        for i in range(1, len(self.trees[0])):
            if y+i >= len(self.trees[0]):
                break
            
            trees_to_right += 1
            if self.trees[x][y+i] >= tree_height:
                break
            
        
        for i in range(1, len(self.trees[0])):
            if y-i < 0:
                break
            
            trees_to_left += 1
            if self.trees[x][y-i] >= tree_height:
                break
                    
        return trees_to_left * trees_to_right
    
    def calculate_outside_visibility(self) -> None:
        visible_from_left: list[list[bool]] = []
        visible_from_right: list[list[bool]] = []
        visible_from_top: list[list[bool]] = []
        visible_from_bottom: list[list[bool]] = []
        
        for i in range(len(self.trees)):
            visible_from_left.append([])
            visible_from_right.append([])
            visible_from_top.append([])
            visible_from_bottom.append([])
            
            highest_from_left = -1
            highest_from_right = -1
            highest_from_top = -1
            highest_from_bottom = -1
            
            for j in range(len(self.trees[i])):
                visible_from_left[i].append(self.trees[i][j] > highest_from_left)
                if visible_from_left[i][-1]:
                    highest_from_left = self.trees[i][j]
                    
                visible_from_right[i].append(self.trees[i][-1-j] > highest_from_right)
                if visible_from_right[i][-1]:
                    highest_from_right = self.trees[i][-1-j]
                    
                visible_from_top[i].append(self.trees[j][i] > highest_from_top)
                if visible_from_top[i][-1]:
                    highest_from_top = self.trees[j][i]
                    
                visible_from_bottom[i].append(self.trees[-1-j][i] > highest_from_bottom)
                if visible_from_bottom[i][-1]:
                    highest_from_bottom = self.trees[-1-j][i]
        
        visible_from_right = mirror(visible_from_right)
        visible_from_bottom = rotate_left(visible_from_bottom)
        visible_from_top = rotate_left(mirror(visible_from_top))
        
        self.visibility_grid: list[list[bool]] = []
        self.visible_count = 0
        
        for i in range(len(self.trees)):
            self.visibility_grid.append([])
            for j in range(len(self.trees[i])):
                visible = visible_from_left[i][j] or visible_from_right[i][j] or visible_from_top[i][j] or visible_from_bottom[i][j]
                self.visibility_grid[i].append(visible)
                if visible:
                    self.visible_count += 1
    
def mirror(matrix:list[list]) -> list[list]:
    new_matrix:list[list] = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            new_matrix[i].append(matrix[i][-j-1])
    
    return new_matrix

def rotate_left(matrix:list[list]) -> list[list]:
    new_matrix:list[list] = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            new_matrix[i].append(matrix[j][-i-1])
    
    return new_matrix
        
def run_day(day: Day) -> Day:
    lines = day.input
    # lines = day.sample
    
    forest = Forest(lines)
    forest.calculate_outside_visibility()
    forest.calculate_inside_visibility()
    
    # print(forest.visible_count)
    # print(forest.best_tree, forest.scenic_score[forest.best_tree[0]][forest.best_tree[1]])
        
    day.set_description(f"The elves want to build a tree house at the best location in the forest.")
    day.set_result(f"From the outside, there are {forest.visible_count} trees visible.\n" + \
        f"The tree with the best scenic score is the tree situated at {forest.best_tree} with a scenic score of {forest.scenic_score[forest.best_tree[0]][forest.best_tree[1]]}.\n" + \
            f"This tree is {'not ' if not forest.visibility_grid[forest.best_tree[0]][forest.best_tree[1]] else ''}visible from the outside.")
            
    return day


if __name__ == "__main__":
    
    PATH = os.path.dirname(__file__)
    
    config = get_config_from_individual_day()

    PRINT_OUTPUT = not config['no_output']
        
    day = Day(DAY)
    day.set_input(f"{PATH}/../input/")
    day = run_day(day)
    day.append_to_output(PATH)
    
    if PRINT_OUTPUT and PRINT_OUTPUT_MANUAL_OVERRIDE:
        print(day)