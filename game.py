from tkinter import * 
import random 

class Snake():
    def __init__(self, grids):
        # The body should be a list of coordinates on the grid (0,0), ..., (size-1, size-1)
        self.size = grids
        self.body = [[0, self.size-2], [0, self.size-1]]

    def collision(self):
        # check collision of the head of the snake 
        x, y = self.body[0]
        if x < 0 or x > self.size-1: return True 
        if y < 0 or y > self.size-1: return True 
        if self.body.count(self.body[0]) > 1: return True 
        return False

class Board(Canvas): 
    def __init__(self, parent, point_var, size = 1, spd = 1): 
        Canvas.__init__(self, parent, highlightthickness=0,bg="black")
        self.game = True 
        self.parent = parent
        self.points = point_var

        # set the size of grid on the board and game speed 
        self.size = 20//size 
        self.grids = 500//self.size 
        self.spd = spd*100 # in milliseconds 

        # directions
        self.dir = 0

        # make snake 
        self.snake = Snake(self.grids)

        # make the initial "food"
        self.food = [0, 0]
        self.gen_food()

        self.update()

    def gen_food(self): 
        self.food = [random.randint(0, self.grids-1), random.randint(0, self.grids-1)]
        fx, fy = self.food 
        self.create_oval(fx*self.size, fy*self.size, 
                              (fx+1)*self.size, (fy+1)*self.size, fill="#FFFF00", tags="food")      

    def dir_change(self, val):
        self.dir += val 
        self.dir = self.dir % 4

    def move_snake(self):
        dx, dy = 0, 0
        if self.dir == 0:
            dy = -1
        elif self.dir == 1:
            dx = 1
        elif self.dir == 2:
            dy = 1
        elif self.dir == 3:
            dx = -1
        hx, hy = self.snake.body[0]
        new_head = [hx+dx, hy+dy]
        self.snake.body = self.snake.body[:-1]
        self.snake.body.insert(0, new_head)

    def food_collision(self, old_tail):
        sx, sy = self.snake.body[0]
        fx, fy = self.food 
        if sx == fx and sy == fy: 
            self.points.set(self.points.get()+1)
            self.delete("food")
            self.gen_food()
            self.snake.body.append(old_tail)

    def update(self): 
        # update snake position
        tail = self.snake.body[-1]
        self.move_snake()
        self.food_collision(tail)
        # redraw the snake
        self.delete("snake")
        for coord in self.snake.body:
            x,y = coord
            self.create_rectangle(x*self.size, y*self.size, 
                                  (x+1)*self.size, (y+1)*self.size, fill="#00FF00", tags="snake")      
        
        # check collision with "walls"
        if self.snake.collision(): 
            self.game = False 
        
        if self.game: 
            self.after(self.spd, self.update)
            self.parent.event_generate("<<GameEnd>>")
            

        
