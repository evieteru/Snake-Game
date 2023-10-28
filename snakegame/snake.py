import enum
from tkinter import Y
from turtle import down

class Direction(enum.Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

class Snake:
    def __init__(self):
        self.body_parts_positions = []
        self.body_parts_positions.append([0,0]) #head
        self.body_parts_positions.append([0,1])
        self.body_parts_positions.append([0,2])
       
       
    def move(self,  direction):
        '''
        Representation of a five part snake below as a list:
        Positions of each body part are in a list called self.body_parts_positions
          Head      body_part    body_part   body_part     tail
        [ [x, y]    [x, y]       [x, y]      [x, y]        [x,y] ]
        '''

        # we are going to move the entire snake, 
        # by changing the positions of each part one at a time, starting at the tail

        length_of_snake = len(self.body_parts_positions)

        for body_part_number in range(length_of_snake - 1, 0, -1):
            position_of_body_part_ahead= self.body_parts_positions[body_part_number - 1]
            self.body_parts_positions[body_part_number] = position_of_body_part_ahead

        # change the position of the head
        
        if direction == Direction.DOWN:
            head_position = self.body_parts_positions[0]
            y_value_of_head_position = head_position[1] + 1
            x_value_of_head_position = head_position[0]
            new_head_position = [x_value_of_head_position, y_value_of_head_position]
            self.body_parts_positions[0] = new_head_position
        elif direction == Direction.UP:
            head_position = self.body_parts_positions[0]
            y_value_of_head_position = head_position[1] - 1
            x_value_of_head_position = head_position[0]
            new_head_position = [x_value_of_head_position, y_value_of_head_position]
            self.body_parts_positions[0] = new_head_position
        elif direction == Direction.RIGHT:
            head_position = self.body_parts_positions[0]
            y_value_of_head_position = head_position[1] 
            x_value_of_head_position = head_position[0] + 1
            new_head_position = [x_value_of_head_position, y_value_of_head_position]
            self.body_parts_positions[0] = new_head_position
        else:
            head_position = self.body_parts_positions[0]
            y_value_of_head_position = head_position[1] 
            x_value_of_head_position = head_position[0] - 1
            new_head_position = [x_value_of_head_position, y_value_of_head_position]
            self.body_parts_positions[0] = new_head_position

    def add_part(self):
        tail_position = self.body_parts_positions[-1]
        self.body_parts_positions.append(tail_position)

snake = Snake()


print(snake.body_parts_positions)
snake.add_part()
print(snake.body_parts_positions)
snake.move(Direction.DOWN)
snake.move(Direction.DOWN)
snake.move(Direction.DOWN)

print(snake.body_parts_positions)
