from tkinter import * 
from game import * 

def game(): 
    root = Tk()
    root.state("zoomed")

    root.geometry("500x500")
    root.minsize(width=500, height=500)
    root.maxsize(width=500, height=500)

    board = Board(root)
    board.pack(fill=BOTH, expand=True)
    
    # Binding directional keys 
    root.bind("<Left>", lambda e: board.dir_change(-1))
    root.bind("<Right>", lambda e: board.dir_change(1))
    
    root.mainloop()

if __name__ == "__main__": 
    game()
