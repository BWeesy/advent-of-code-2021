import fileHandler as fh
from functools import reduce

#0,0 is top left X horizontal, Y is vertical
class HeightMap():
  def __init__(self, points) -> None:
      self.points = points
      self.maxX = len(points[0])
      self.maxY = len(points)
      self.maxXIndex = self.maxX - 1
      self.maxYIndex = self.maxY - 1

  def getPoint(self, x, y):
    return self.points[y][x]

  def allIndexes(self):
    for x in range(0, self.maxX):
      for y in range(0, self.maxY):
        yield (x, y)

  def getTopNeighbour(self, targetX, targetY):
    if targetX == 0:
      return None
    else:
      return targetX - 1, targetY

  def getBottomNeighbour(self, targetX, targetY):
    if targetX == self.maxXIndex:
      return None
    else:
      return targetX + 1, targetY

  def getLeftNeighbour(self, targetX, targetY):
    if targetY == 0:
      return None
    else:
      return targetX, targetY - 1

  def getRightNeighbour(self, targetX, targetY):
    if targetY == self.maxYIndex:
      return None
    else:
      return targetX, targetY + 1

  def getNeighbours(self, targetX, targetY):
    return list(filter(lambda x: x != None, [
      self.getTopNeighbour(targetX, targetY),
      self.getBottomNeighbour(targetX, targetY),
      self.getLeftNeighbour(targetX, targetY),
      self.getRightNeighbour(targetX, targetY),
    ]))

  def getNeighbourValues(self, targetX, targetY):
    return list(map(lambda neighbour: self.getPoint(neighbour[0], neighbour[1]), self.getNeighbours(targetX, targetY)))    

  def isLowerThanAllNeighbours(self, targetX, targetY):
    return self.getPoint(targetX, targetY) < min(self.getNeighbourValues(targetX, targetY))

  def getRiskLevel(self, targetX, targetY):
    return self.getPoint(targetX, targetY) + 1

  def getAllIndexes(self):
    allIndexes = []
    [[allIndexes.append((x, y)) for y in range(0, self.maxY)] for x in range(0, self.maxX)]
    return allIndexes

  def getLowPoints(self):
    return [(targetX, targetY) for targetX, targetY in self.getAllIndexes() if self.isLowerThanAllNeighbours(targetX, targetY)]

  def getSumOfAllRiskLevels(self):
    return sum([self.getRiskLevel(targetX, targetY) for targetX, targetY in self.getLowPoints()])

  def getRecursiveBasin(self, targetX, targetY):
    result = [(targetX, targetY)]
    for neighbourX, neighbourY in self.getHigherNeighbours(targetX, targetY):
      for branchResults in self.getRecursiveBasin(neighbourX, neighbourY):
        result.append(branchResults)
    return result

  def getAllBasins(self):
    return [set(self.getRecursiveBasin(lowX, lowY)) for lowX, lowY in self.getLowPoints()]

  def getSizeOfAllBasins(self):
    return map(len, self.getAllBasins())

  def getHigherNeighbours(self, targetX, targetY):
    return [(neighbourX, neighbourY) for neighbourX, neighbourY 
    in self.getNeighbours(targetX, targetY) 
    if self.getPoint(targetX, targetY) < self.getPoint(neighbourX, neighbourY) == self.getPoint(neighbourX, neighbourY) != 9]

  def getLargestBasins(self, numberOfBasins):
    return sorted(self.getSizeOfAllBasins(), reverse=True)[0:numberOfBasins]

  def getMultipleOfLargestBasinSizes(self, numberOfBasins):
    return reduce(lambda a, b: a * b , self.getLargestBasins(numberOfBasins))

def mapPointsToArray(line):
  return [int(char) for char in line]

def main():
  points = fh.getMappedLines('input/day9', mapPointsToArray)
  heightMap = HeightMap(points) 
  print(f"Sum of risk levels {heightMap.getSumOfAllRiskLevels()}")
  print(f"Sum of 3 largest basin sizes {heightMap.getMultipleOfLargestBasinSizes(3)}")

def test():
  testData = ["2199943210", "3987894921", "9856789892", "8767896789", "9899965678"]
  points = list(map(mapPointsToArray, testData))
  heightMap = HeightMap(points)
  lowPoints = [(heightMap.getPoint(targetX, targetY), targetX, targetY) for (targetX, targetY) in heightMap.allIndexes() if heightMap.isLowerThanAllNeighbours(targetX, targetY)]
  #print(lowPoints)
  print(heightMap.getMultipleOfLargestBasinSizes(3))

if __name__ == "__main__":
  main()