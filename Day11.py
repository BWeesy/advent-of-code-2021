import fileHandler as fh
import gridHandler as gh

#0,0 is top left X horizontal, Y is vertical
class Field(gh.Grid):
  def __init__(self, points) -> None:
    self.points = points
    self.maxX = len(points[0])
    self.maxY = len(points)
    self.maxXIndex = self.maxX - 1
    self.maxYIndex = self.maxY - 1
    self.flashes = 0

  def doSteps(self, steps):
    for step in range(1, steps + 1):
      self.step = step
      self.doStep()

  def doStep(self):
    self.add1ToAll()
    self.resolveFlashes()
    return

  def findFirstFlash(self):
    step = 0
    while not self.allFlashed():
      self.doStep()
      step += 1
    return step

  def allFlashed(self):
    return sum([sum(line) for line in self.points]) == 0
  
  def add1ToAll(self):
    self.points = [[x + 1 for x in line] for line in self.points]

  def octopusShouldFlash(self, targetX, targetY):
    return self.getPoint(targetX, targetY) > 9

  def lineShouldFlash(self, line):
    return len(list(filter(lambda x: x > 9, line))) > 0

  def fieldShouldFlash(self):
    for line in self.points:
      if self.lineShouldFlash(line):
        return True
    return False

  def flashingNeighbours(self, targetX, targetY):
    return len(list(filter(lambda pos: self.getPoint(pos[1], pos[0]) > 9, self.getAllNeighbours(targetX, targetY))))

  def resolveFlashes(self):
    newPoints = self.points.copy()
    flashed = set()
    while self.fieldShouldFlash():
      newPoints = [[newPoints[x][y] + self.flashingNeighbours(x, y) if (y, x) not in flashed else newPoints[x][y] for y in range(0, self.maxY) ] for x in range(0, self.maxX)]
      flashingPoints = self.getPointsByCriteria(self.octopusShouldFlash)
      for (x, y) in flashingPoints:
        newPoints[y][x] = 0
        flashed.add((x,y))
        
      self.points = newPoints
    self.flashes += len(flashed)

def getIntList(line):
  return [int(element) for element in line]

def main():
  octopi = fh.getMappedLines('input/day11', getIntList)
  field = Field(octopi)
  field.doSteps(100)
  print(f"Flashes {field.flashes}")

  field = Field(octopi)
  print(f"First all flash {field.findFirstFlash()}")

def convertTestData(data):
  return list(map(getIntList, data))

def test():
  testData1 = ["5483143223","2745854711","5264556173","6141336146","6357385478","4167524645","2176841721","6882881134","4846848554","5283751526"]
  testData2 = ["01", "00"]
  testData3 = ["00", "00"]
  field = Field(convertTestData(testData1))
  field.doSteps(2)
  testData1Expected2Steps = ["8807476555", "5089087054", "8597889608", "8485769600", "8700908800", "6600088989", "6800005943", "0000007456", "9000000876", "8700006848"]
  expected = convertTestData(testData1Expected2Steps)
  assert expected == field.points, f"{field.points}"
  
  field = Field(convertTestData(testData1))
  field.doSteps(3)
  testData1Expected3Steps = ["0050900866", "8500800575", "9900000039", "9700000041", "9935080063", "7712300000", "7911250009", "2211130000", "0421125000", "0021119000"]
  expected = convertTestData(testData1Expected3Steps)
  assert expected == field.points, f"{field.points}"

  field = Field(convertTestData(testData1))
  field.doSteps(10)
  testData1Expected10Steps = ["0481112976", "0031112009", "0041112504", "0081111406", "0099111306", "0093511233", "0442361130", "5532252350", "0532250600", "0032240000"]
  expected = convertTestData(testData1Expected10Steps)
  assert expected == field.points, f"{field.points}"
  assert field.flashes == 204, f"{field.flashes}"

  field = Field(convertTestData(testData1))
  field.doSteps(100)
  testData1Expected100Steps = ["0397666866", "0749766918", "0053976933", "0004297822", "0004229892", "0053222877", "0532222966", "9322228966", "7922286866", "6789998766"]
  expected = convertTestData(testData1Expected100Steps)
  assert expected == field.points, f"{field.points}"
  assert field.flashes == 1656, f"{field.flashes}"

  assert True == Field(convertTestData(testData3)).allFlashed()
  assert False == Field(convertTestData(testData2)).allFlashed()

  field = Field(convertTestData(testData1))
  assert 195 == field.findFirstFlash()

  print("Day 11 Tests passed")

if __name__ == "__main__":
  main()
