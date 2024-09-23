import tkinter as tk

# Constants
BASE_SIZE = 200  # Size of the filled square


# Recursive function to draw the Sierpinski Carpet
def draw_sierpinski_carpet(canvas, x, y, size, order):
    if order == 0:
        canvas.create_rectangle(x, y, x + size, y + size, fill="black")
    else:
        new_size = size // 3
        for row in range(3):
            for col in range(3):
                if not (col == 1 and row == 1):  # Skip the center square
                    x_i = x + col * size // 3
                    y_i = y + row * size // 3
                    draw_sierpinski_carpet(canvas, x_i, y_i, new_size, order - 1)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sierpinski Carpet")

    canvas_size = 600  # Size of the canvas
    canvas = tk.Canvas(root, width=canvas_size, height=canvas_size)
    canvas.pack()

    # Draw the Sierpinski Carpet
    draw_sierpinski_carpet(canvas, 0, 0, canvas_size, 4)  # You can change the order

    root.mainloop()
