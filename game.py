from tkinter import * 

class Snake():
    def __init__(self, size=1, spd=1):
        # The body should be a list of coordinates on the grid (0,0), ..., (size-1, size-1)
        self.size = 50*size
        self.body = [[0, self.size-2], [0, self.size-1]]

    def collision(self):
        x, y = self.body[0]
        if x < 0 or x > self.size-1: return True 
        if y < 0 or y > self.size-1: return True 
        if self.body.count(self.body[0]) > 1: return True 
        return False

class Board(Canvas): 
    def __init__(self, parent, size = 1, spd = 1): 
        Canvas.__init__(self, parent, highlightthickness=0,bg="black")
        self.game = True 

        # set the number of grid on the board and game speed 
        self.size = 10//size 
        self.spd = spd*100 # in milliseconds 

        # directions
        self.dir = 0

        # make snake 
        self.snake = Snake(size, spd)

        self.update()

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

    def update(self): 
        self.move_snake()
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

        
