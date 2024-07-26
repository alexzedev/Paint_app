import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import Image, ImageDraw, ImageTk

class Paint:
    def __init__(self, master):
        self.master = master
        self.master.title("Paint by alexzedev")
        self.master.geometry("800x600")

        self.color = "black"
        self.brush_size = 2
        self.canvas_width = 700
        self.canvas_height = 500

        self.setup_ui()

    def setup_ui(self):
        # Top frame for tools
        self.top_frame = tk.Frame(self.master)
        self.top_frame.pack(fill=tk.X, padx=5, pady=5)

        # Canvas
        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Create a blank image and drawing context
        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), "white")
        self.draw = ImageDraw.Draw(self.image)

        # Buttons
        tk.Button(self.top_frame, text="Color", command=self.choose_color).pack(side=tk.LEFT, padx=5)
        tk.Button(self.top_frame, text="Brush Size", command=self.choose_size).pack(side=tk.LEFT, padx=5)
        tk.Button(self.top_frame, text="Clear", command=self.clear).pack(side=tk.LEFT, padx=5)
        tk.Button(self.top_frame, text="Save", command=self.save).pack(side=tk.LEFT, padx=5)

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)
        self.draw.ellipse([x1, y1, x2, y2], fill=self.color, outline=self.color)

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def choose_color(self):
        self.color = colorchooser.askcolor()[1]

    def choose_size(self):
        self.brush_size = tk.simpledialog.askinteger("Brush Size", "Enter brush size:", minvalue=1, maxvalue=50)

    def clear(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), "white")
        self.draw = ImageDraw.Draw(self.image)

    def save(self):
        filename = filedialog.asksaveasfilename(defaultextension='.png')
        if filename:
            self.image.save(filename)

if __name__ == "__main__":
    root = tk.Tk()
    Paint(root)
    root.mainloop()