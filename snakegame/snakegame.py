from snake import Snake, Direction
from food import Food
import tkinter
import tkinter.ttk

X_GRID_SIZE = 15
Y_GRID_SIZE = 15
BLOCK_SIZE = 20
OUTLINE_WIDTH = 1
INSIDE_FILL_WIDTH = BLOCK_SIZE - (2 * OUTLINE_WIDTH)
X_CANVAS_SIZE = X_GRID_SIZE * BLOCK_SIZE
Y_CANVAS_SIZE = Y_GRID_SIZE * BLOCK_SIZE
SNAKE_STARTING_SIZE = 3
SNAKE_COLOR = "#135513"
SNAKE_COLOR_OUTLINE = "#06AE06"
FOOD_COLOR = "#2C0383"
FOOD_COLOR_OUTLINE = "#A78FDA"
BACKGROUND_COLOR = "#A9A9A9"


def game_loop():

    #print("I'm in the game loop")
    global snake

    global is_stop_game
    if is_stop_game:
        root_window.after(600, game_loop)
        return

    def collision_detected(value=""):
        if value == "food":
            snake.add_part()
            food.set_random_position(snake.body_parts_positions)

            global score_number
            score_number = len(snake.body_parts_positions)
            game_score_new= "Score: "
            score_number_str= str(score_number)
            label_text_new = game_score_new + score_number_str
            lbl_score.config(text=label_text_new)

        else: 
            global is_stop_game
            is_stop_game = True
            die_snake()
        print("collision", value)


    def die_snake():
        game_over_window = tkinter.Toplevel()
        lbl_game_over = tkinter.Label(game_over_window, text="GAME OVER!", fg='#D30E0E')
        lbl_game_over.grid(column=0, row=0)
        game_over_window.title(" ")

        def play_again_btn_pressed(unused_argument):
            canvas.delete("objects")
            global snake
            global food
            global is_stop_game
            global last_button_pressed
            global score_number

            snake = Snake()
            last_button_pressed = Direction.RIGHT
            food = Food(X_GRID_SIZE, Y_GRID_SIZE)
            game_over_window.withdraw()
            is_stop_game = False

            score_number = len(snake.body_parts_positions)
            game_score_new= "Score: "
            score_number_str= str(score_number)
            label_text_new = game_score_new + score_number_str
            lbl_score.config(text=label_text_new)
            print("Im running!")

        btn_play_again = tkinter.ttk.Button(game_over_window, text="Play Again")
        btn_play_again.grid(column=0, row=1)
        btn_play_again.bind("<ButtonPress>", play_again_btn_pressed)




    # delete snake section
    canvas.delete("objects")

    # move snake 
    global last_button_pressed
    snake.move(last_button_pressed)


    # collision detection

    # Snake head is beyond perimeter of the grid
    x_position_of_head = snake.body_parts_positions[0][0]
    y_position_of_head = snake.body_parts_positions[0][1]

    if x_position_of_head < 0 or x_position_of_head > X_GRID_SIZE-1:
        collision_detected("wall")
    if y_position_of_head < 0 or y_position_of_head > Y_GRID_SIZE-1:
        collision_detected("wall")


    # Snake head shares a position with a body part
    tail_position = len(snake.body_parts_positions)-1
    head_position = snake.body_parts_positions[0]
    for body_part_number in range(1, tail_position+1):
        if snake.body_parts_positions[body_part_number] == head_position:
            collision_detected("snake")

    # Snake collides with food
    head_position = snake.body_parts_positions[0]
    food_position = food.food_position
    if head_position == food_position:
        collision_detected("food")


  

    # draw snake section

    def draw_rectangle(x_in_pixels, y_in_pixels, fill_color, outline_color):
        canvas.create_rectangle(
                                x_in_pixels + OUTLINE_WIDTH,
                                y_in_pixels + OUTLINE_WIDTH,
                                x_in_pixels + INSIDE_FILL_WIDTH,
                                y_in_pixels + INSIDE_FILL_WIDTH,
                                fill=fill_color,
                                outline=outline_color,
                                width=2,
                                tags="objects"
        )
    
    
    for body_part_number in range(len(snake.body_parts_positions)):
        x_position_of_body_part = snake.body_parts_positions[body_part_number][0]*BLOCK_SIZE
        y_position_of_body_part = snake.body_parts_positions[body_part_number][1]*BLOCK_SIZE
        draw_rectangle(x_position_of_body_part, y_position_of_body_part, SNAKE_COLOR, SNAKE_COLOR_OUTLINE)


    # Draw food
    #food.set_random_position()
    x_food_position = food.food_position[0]*BLOCK_SIZE
    y_food_position = food.food_position[1]*BLOCK_SIZE
    draw_rectangle(x_food_position, y_food_position, FOOD_COLOR, FOOD_COLOR_OUTLINE)


    root_window.after(600, game_loop)


def up_pressed(event):
    global last_button_pressed
    last_button_pressed = Direction.UP
def down_pressed(event):
    global last_button_pressed
    last_button_pressed = Direction.DOWN
def right_pressed(event):
    global last_button_pressed
    last_button_pressed = Direction.RIGHT
def left_pressed(event):
    global last_button_pressed
    last_button_pressed = Direction.LEFT
def space_pressed(event):
    snake.add_part()


is_stop_game = False

last_button_pressed = Direction.RIGHT

snake = Snake()
root_window = tkinter.Tk()
root_window.title("Snake Game")
root_window.bind("<Up>", up_pressed)
root_window.bind("<Down>", down_pressed)
root_window.bind("<Left>", left_pressed)
root_window.bind("<Right>", right_pressed)
root_window.bind("<Key-space>", space_pressed)

food = Food(X_GRID_SIZE, Y_GRID_SIZE)



canvas = tkinter.Canvas(root_window)
canvas.config(width=X_CANVAS_SIZE, height=Y_CANVAS_SIZE, borderwidth=0, highlightthickness=0)
canvas.grid(column=0, row=1)

lbl_score = tkinter.Label(root_window, text="hi")
lbl_score.grid(column=0, row=0)
score_number = len(snake.body_parts_positions)
a= "Score: "
b= str(score_number)
c= a+b
lbl_score.config(text=c)

root_window.after(1000, game_loop)

root_window.mainloop()


'''
rectangle = canvas.create_rectangle(
    x, upper left corner
    y,
    x, lower right corner
    y,
    fill=,
    outline=,
    width=,
    tags=
)
'''