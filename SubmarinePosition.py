from fileHandler import getLines

class Submarine:
  def __init__(self):
    self.horizontal = 0
    self.depth = 0

  def forward(self, amount):
    self.horizontal += amount
  
  def up(self, amount):
    self.depth -= amount
  
  def down(self, amount):
    self.depth += amount

  def getPosition(self):
    return self.depth * self.horizontal

  def parseInstruction(self, instruction):
    [direction, amount] = instruction.split()
    if(direction == "forward"):
      self.forward(int(amount))
    if(direction == "up"):
      self.up(int(amount))
    if(direction == "down"):
      self.down(int(amount))

def main():
  submarine = Submarine()
  for line in getLines('input/day2.txt'):
    submarine.parseInstruction(line)
  print(submarine.getPosition())

if __name__ == "__main__":
  main()