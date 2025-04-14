import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()
    
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.itemconfig(overlapping_object, fill="white")

def activate_eraser(canvas):
    eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill="pink")

    def move_eraser(event):
        canvas.coords(eraser, event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE)
        erase_objects(canvas, eraser)

    canvas.bind("<Motion>", move_eraser)

def main():
    root = tk.Tk()
    root.title("Eraser Grid")

    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="blue")
    erase_button = tk.Button(root, text="Activate Eraser", command=lambda: activate_eraser(canvas))
    erase_button.pack()
    
    root.mainloop()

if __name__ == '__main__':
    main()