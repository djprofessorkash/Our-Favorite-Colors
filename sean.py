import tkinter as tk
import time

def fade_color(color1, color2, step):
    """Generate a color that is a step between color1 and color2."""
    def str_to_rgb(color):
        return tuple(int(color[i:i+2], 16) for i in (1, 3, 5))

    def rgb_to_str(rgb):
        return f"#{''.join(f'{int(c):02x}' for c in rgb)}"

    rgb1 = str_to_rgb(color1)
    rgb2 = str_to_rgb(color2)

    return rgb_to_str(tuple(rgb1[i] + (rgb2[i] - rgb1[i]) * step for i in range(3)))

def update_color():
    global step
    new_color = fade_color("#0000FF", "#00FFFF", step)
    root.configure(bg=new_color)
    step += 0.05
    if step > 1:
        step = 0
    root.after(100, update_color)

root = tk.Tk()
root.geometry("300x200")
step = 0
update_color()
root.mainloop()
