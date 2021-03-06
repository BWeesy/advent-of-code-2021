import fileHandler as fh

class Vector():
  def __init__(self, line):
    [start, end] = line.split(' -> ')
    [startX, startY] = list(map(int, start.split(',')))
    [endX, endY] = list(map(int, end.split(',')))
    self.startX = startX
    self.startY = startY
    self.endX = endX
    self.endY = endY

  def getCoveredCoordinates(self):
    if self.startX == self.endX: #Vertical line
      return [(self.startX, y) for y in range(min(self.startY, self.endY), max(self.startY, self.endY) + 1)]
    if self.startY == self.endY: #Horizontal line
      return [(x, self.startY) for x in range(min(self.startX, self.endX), max(self.startX, self.endX) + 1)]
    
    #Diagonal line
    xRange = range(self.startX, self.endX+1, 1) if self.startX < self.endX else range(self.startX, self.endX-1, -1)
    yRange = range(self.startY, self.endY+1, 1) if self.startY < self.endY else range(self.startY, self.endY-1, -1)

    coveredCoords = []
    for i, x in enumerate(xRange):
      y = yRange[i]
      coveredCoords.append((x, y))
    return coveredCoords

  def __str__(self):
    return f"({self.startX}, {self.startY}) -> ({self.endX}, {self.endY})"

def main():
  vectors = fh.getMappedLines('input/day5', lambda x: Vector(x))

  ventLocations = {}
  for vector in vectors:
    coveredCoords = vector.getCoveredCoordinates()
    for coveredCoord in coveredCoords:
      ventLocations[coveredCoord] = ventLocations.setdefault(coveredCoord, 0) + 1
  dangerousVents = [ventLocations[loc] for loc in ventLocations if ventLocations[loc]>1]
  print(f"There are {len(dangerousVents)} dangerous vents")
  return

if __name__ == "__main__":
  main()