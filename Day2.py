import fileHandler as fh

class Submarine:
  def __init__(self):
    self.horizontal = 0
    self.depth = 0
    self.aim = 0

  def forward(self, amount):
    self.horizontal += amount
    self.depth += amount * self.aim
  
  def up(self, amount):
    self.aim -= amount
  
  def down(self, amount):
    self.aim += amount

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
  for line in fh.getLines('input/day2'):
    submarine.parseInstruction(line)
  print(submarine.getPosition())

def test():
  submarine = Submarine()
  submarine.parseInstruction("forward 1")
  assert submarine.getPosition() == 0, f"{submarine.getPosition()}"
  submarine.parseInstruction("down 1")
  assert submarine.getPosition() == 0, f"{submarine.getPosition()}"
  submarine.parseInstruction("forward 1")
  assert submarine.getPosition() == 2, f"{submarine.getPosition()}"
  submarine.parseInstruction("up 2")
  assert submarine.getPosition() == 2, f"{submarine.getPosition()}"
  submarine.parseInstruction("down 1")
  assert submarine.getPosition() == 2, f"{submarine.getPosition()}"
  submarine.parseInstruction("forward 1")
  assert submarine.getPosition() == 3, f"{submarine.getPosition()}"
  submarine.parseInstruction("forward 1")
  assert submarine.getPosition() == 4, f"{submarine.getPosition()}"
  submarine.parseInstruction("down 1")
  assert submarine.getPosition() == 4, f"{submarine.getPosition()}"

if __name__ == "__main__":
  main()