from tkinter import * 
from game import * 

def game(): 
    root = Tk()
    root.state("zoomed")

    root.state("zoomed")
    root.minsize(width=500, height=500)
    root.grid_columnconfigure([0,2], weight=1)
    root.grid_rowconfigure([0,2], weight=1)

    main_frame = Frame(root, width=500, height=500, bg="black")
    main_frame.grid_propagate(False)
    main_frame.pack_propagate(False)
    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)

    main_frame.grid(row=1, column=1)

    points = IntVar(value=0)
    point_label = Label(root, textvariable=points, font=("Helvetica", 24), anchor=CENTER)
    point_label.grid(row=0, column=1, sticky="n")

    board = Board(main_frame, points, 1, 2)
    board.grid(column=0, row=0, sticky="nsew")

    def keypressed(event): 
        k = event.char
        if k == "r" or k == "R": 
            board.new_game()
            root.unbind("<Key>")

    # Binding directional keys 
    root.bind("<Left>", lambda e: board.dir_change(-1))
    root.bind("<Right>", lambda e: board.dir_change(1))
    root.bind("<<GameEnd>>", lambda e: root.bind("<Key>", keypressed))
    
    root.mainloop()

if __name__ == "__main__": 
    game()
