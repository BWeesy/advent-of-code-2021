import fileHandler as fh
import gridHandler as gh
from functools import reduce

#0,0 is top left X horizontal, Y is vertical
class HeightMap(gh.Grid):

  def getRiskLevel(self, targetX, targetY):
    return self.getPoint(targetX, targetY) + 1

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