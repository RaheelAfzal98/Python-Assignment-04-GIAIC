# Problem Statement
# Implement an 'eraser' on a canvas.
# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.


import tkinter as tk

# Constants
GRID_SIZE = 20  # Size of each cell in the grid
ERASER_SIZE = 2  # Size of the eraser (in terms of grid cells)

class EraserCanvas(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=400, height=400, bg="white")
        self.grid_cells = []
        self.eraser_rect = None
        self.eraser_position = [100, 100]  # Starting position of the eraser
        self.create_grid()
        self.create_eraser()
        self.bind("<B1-Motion>", self.move_eraser)
        self.pack()

    def create_grid(self):
        """Create a grid of blue cells."""
        for i in range(0, 400, GRID_SIZE):
            row = []
            for j in range(0, 400, GRID_SIZE):
                cell = self.create_rectangle(i, j, i + GRID_SIZE, j + GRID_SIZE, fill="blue", outline="blue")
                row.append(cell)
            self.grid_cells.append(row)

    def create_eraser(self):
        """Create the eraser rectangle."""
        x1, y1 = self.eraser_position
        x2, y2 = x1 + GRID_SIZE * ERASER_SIZE, y1 + GRID_SIZE * ERASER_SIZE
        self.eraser_rect = self.create_rectangle(x1, y1, x2, y2, fill="gray", outline="gray")

    def move_eraser(self, event):
        """Move the eraser rectangle and erase cells."""
        # Move the eraser rectangle to the mouse position
        x, y = event.x, event.y
        eraser_x = (x // GRID_SIZE) * GRID_SIZE
        eraser_y = (y // GRID_SIZE) * GRID_SIZE
        self.eraser_position = [eraser_x, eraser_y]
        
        # Move the eraser rectangle to the new position
        self.coords(self.eraser_rect, eraser_x, eraser_y, eraser_x + GRID_SIZE * ERASER_SIZE, eraser_y + GRID_SIZE * ERASER_SIZE)
        
        # Erase the affected cells
        for i in range(eraser_x, eraser_x + GRID_SIZE * ERASER_SIZE, GRID_SIZE):
            for j in range(eraser_y, eraser_y + GRID_SIZE * ERASER_SIZE, GRID_SIZE):
                self.erase_cell(i, j)

    def erase_cell(self, x, y):
        """Erase the cell by turning it white."""
        # Check if the coordinates are within bounds and if it's a blue cell
        for row in self.grid_cells:
            for cell in row:
                cx1, cy1, cx2, cy2 = self.coords(cell)
                if cx1 <= x < cx2 and cy1 <= y < cy2:
                    self.itemconfig(cell, fill="white")

def main():
    root = tk.Tk()
    root.title("Eraser on Canvas")
    canvas = EraserCanvas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
