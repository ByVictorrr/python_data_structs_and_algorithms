import tkinter as tk


def draw_cantor(canvas: tk.Canvas, order: int, left_x, left_y, right_x, right_y):
    if order == 0:
        return
        # Draw the first line
    canvas.create_line(left_x, left_y, right_x, right_y, width=2)
    # Calculate 1/3 at the current line segment
    segment_len = (right_x - left_x) / 3
    # Move down the order to 20 pixels
    new_y = left_y + 20
    # left third: call recursively on the first 3rd of the segment
    draw_cantor(canvas, order - 1, left_x, new_y, left_x + segment_len, new_y)
    # right third: call recursively on the last third segment
    draw_cantor(canvas, order - 1, right_x - segment_len, new_y, right_x, new_y)


if __name__ == "__main__":
    # Tkinter setup
    window = tk.Tk()
    window.title("Cantor Set with Modified Params")

    # Create a canvas to draw on
    canvas = tk.Canvas(window, width=800, height=600)
    canvas.pack()

    # Initial call to draw the Cantor set
    initial_level = 5
    start_x = 50
    end_x = 750
    y_pos = 100

    draw_cantor(canvas, initial_level, start_x, y_pos, end_x, y_pos)

    # Run the Tkinter event loop
    window.mainloop()
