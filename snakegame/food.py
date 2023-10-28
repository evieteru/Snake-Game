import random

class Food:
    def __init__(self, x_grid_size, y_grid_size):
        self.x_grid_size = x_grid_size
        self.y_grid_size = y_grid_size
        self.food_position = [7,7]
        
    def set_random_position(self, snake_body_parts_positions):
        is_food_position_bad = True
        while is_food_position_bad:
            new_x = int(random.random() * self.x_grid_size)
            new_y = int(random.random() * self.y_grid_size)
            self.food_position = [new_x, new_y]
            for body_part_number in range(0, (len(snake_body_parts_positions)-1)):
                if snake_body_parts_positions[body_part_number] == self.food_position:
                    is_food_position_bad = True
                else:
                    is_food_position_bad = False
                    print("bad food position")
                    #redo above code

