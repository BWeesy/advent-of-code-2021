from fileHandler import getLines

class Vector():
  def __init__(self, line):
    [start, end] = line.split(' -> ')
    [startX, startY] = start.split(',')
    [endX, endY] = end.split(',')
    self.startX = int(startX)
    self.startY = int(startY)
    self.endX = int(endX)
    self.endY = int(endY)

  def __str__(self):
    return f"({self.startX}, {self.startX}) -> ({self.endX}, {self.endY})"

def main():
  inputs = list(getLines('input/day5'))
  vectors = [Vector(line) for line in inputs]

  return

if __name__ == "__main__":
  main()