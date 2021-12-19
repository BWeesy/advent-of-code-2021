#0,0 is top left X horizontal, Y is vertical
class Grid():
  def __init__(self, points) -> None:
    print(points)
    self.points = points
    if points:
      self.maxX = len(points[0])
    else:
      self.maxX = 0
    self.maxY = len(points)
    self.maxXIndex = self.maxX - 1
    self.maxYIndex = self.maxY - 1

  def getPoint(self, x, y):
    return self.points[y][x]

  def setPoint(self, x, y, value):
    self.points[y-1][x-1] = value

  def allIndexes(self):
    for x in range(0, self.maxX):
      for y in range(0, self.maxY):
        yield (x, y)

  def getTopNeighbour(self, targetX, targetY):
    if targetX == 0 or targetY == None or targetX == None:
      return None, None
    else:
      return targetX - 1, targetY

  def getBottomNeighbour(self, targetX, targetY):
    if targetX == self.maxXIndex or targetY == None or targetX == None:
      return None, None
    else:
      return targetX + 1, targetY

  def getLeftNeighbour(self, targetX, targetY):
    if targetY == 0 or targetY == None or targetX == None:
      return None, None
    else:
      return targetX, targetY - 1

  def getRightNeighbour(self, targetX, targetY):
    if targetY == self.maxYIndex or targetY == None or targetX == None:
      return None, None
    else:
      return targetX, targetY + 1

  def getTopLeftNeighbour(self, targetX, targetY):
    (topX, topY) = self.getTopNeighbour(targetX, targetY)
    return self.getLeftNeighbour(topX, topY)

  def getTopRightNeighbour(self, targetX, targetY):
    (topX, topY) = self.getTopNeighbour(targetX, targetY)
    return self.getRightNeighbour(topX, topY)

  def getBottomLeftNeighbour(self, targetX, targetY):
    (topX, topY) = self.getBottomNeighbour(targetX, targetY)
    return self.getLeftNeighbour(topX, topY)

  def getBottomRightNeighbour(self, targetX, targetY):
    (topX, topY) = self.getBottomNeighbour(targetX, targetY)
    return self.getRightNeighbour(topX, topY)

  def getOrthogonalNeighbours(self, targetX, targetY):
    return list(filter(lambda x: x[0] != None and x[1] != None, [
      self.getTopNeighbour(targetX, targetY),
      self.getBottomNeighbour(targetX, targetY),
      self.getLeftNeighbour(targetX, targetY),
      self.getRightNeighbour(targetX, targetY),
    ]))

  def getDiagonalNeighbours(self, targetX, targetY):
    return list(filter(lambda x: x[0] != None and x[1] != None, [
      self.getTopLeftNeighbour(targetX, targetY),
      self.getTopRightNeighbour(targetX, targetY),
      self.getBottomLeftNeighbour(targetX, targetY),
      self.getBottomRightNeighbour(targetX, targetY),
    ]))

  def getAllNeighbours(self, targetX, targetY):
    return self.getOrthogonalNeighbours(targetX, targetY) + self.getDiagonalNeighbours(targetX, targetY)

  def getNeighbourValues(self, targetX, targetY):
    return list(map(lambda neighbour: self.getPoint(neighbour[0], neighbour[1]), self.getOrthogonalNeighbours(targetX, targetY)))    

  def isLowerThanAllNeighbours(self, targetX, targetY):
    return self.getPoint(targetX, targetY) < min(self.getNeighbourValues(targetX, targetY))

  def getAllIndexes(self):
    allIndexes = []
    [[allIndexes.append((x, y)) for y in range(0, self.maxY)] for x in range(0, self.maxX)]
    return allIndexes

  def getHigherNeighbours(self, targetX, targetY):
    return [(neighbourX, neighbourY) for neighbourX, neighbourY 
    in self.getOrthogonalNeighbours(targetX, targetY) 
    if self.getPoint(targetX, targetY) < self.getPoint(neighbourX, neighbourY) == self.getPoint(neighbourX, neighbourY) != 9]

  def getLowPoints(self):
    return [(targetX, targetY) for targetX, targetY in self.getAllIndexes() if self.isLowerThanAllNeighbours(targetX, targetY)]

  def print(self):
    for y in self.points:
      print(y)

  def getPointsByCriteria(self, criteria):
    return [(targetX, targetY) for targetX, targetY in self.getAllIndexes() if criteria(targetX, targetY)]

  def fillEmptyPoints(self, sizeX, sizeY):
    self.points = [[0 for y in range(0, sizeX)] for x in range(0, sizeY)]
