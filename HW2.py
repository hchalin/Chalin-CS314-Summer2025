import tkinter as tk

# Window class
class Window:
  def __init__(self):
    self.root = tk.Tk()
    self.root.title("Hw2")
    self.root.geometry("300x200")
    self.startPos = (25,25)
    self.x = self.startPos[0]
    self.y = self.startPos[1]

    # Buttons
    upBtn = tk.Button(self.root, text="Up", command=self.moveUp) # pass in self.root (window)
    upBtn.pack()
    downBtn = tk.Button(self.root, text="Down", command=self.moveDown) # pass in self.root (window)
    downBtn.pack()
    rightBtn = tk.Button(self.root, text="Right", command=self.moveRight) # pass in self.root (window)
    rightBtn.pack()
    leftBtn = tk.Button(self.root, text="Left", command=self.moveLeft) # pass in self.root (window)
    leftBtn.pack()

    # Label
    self.label = tk.Label(self.root, text=f"({self.x}, {self.y})")
    self.label.pack(pady=10)

  def start(self) -> None:
    self.root.mainloop()

  def updateLabel(self, x, y)-> None:
    self.label.config(text=f"({x}, {y})")   # Update the label

  # Movement commands
  def moveUp(self)->None:
    self.y += 1
    if (self.y == 51):
      self.y = 1      # Reset to 1
    self.updateLabel(self.x, self.y)
    print("Move up")

  def moveDown(self)->None:
    self.y -= 1
    if (self.y == 0):
      self.y = 50   # Reset to 50
    self.updateLabel(self.x, self.y)
    print("Move Down")

  def moveRight(self)->None:
    self.x += 1
    if (self.x == 51):
      self.x = 1      # Reset to 1
    self.updateLabel(self.x, self.y)
    print("Move Right")

  def moveLeft(self)->None:
    self.x -= 1
    if (self.x == 0):
      self.x = 50      # Reset to 50
    self.updateLabel(self.x, self.y)
    print("Move Left")

def main():

  # Start the window
  window = Window()
  window.start()




if __name__ == "__main__":
  main()







