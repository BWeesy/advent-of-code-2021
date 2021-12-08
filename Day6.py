import fileHandler as fh

class Day():
  def __init__(self):
    self.fishInDays = []

  def ingestState(self, fishInDays):
    self.fishInDays = fishInDays
    return
  
  def getNextDay(self):
    newState = [0 for _ in range(0, 9)]
    for i, fish in enumerate(self.fishInDays):
      if i == 0:
        newState[8] += fish
        newState[6] += fish
      else:
        newState[i-1] += fish

    return newState

  def doDay(self):
    self.fishInDays = self.getNextDay()

  def doDays(self, numberOfDays):
    for _ in range(0, numberOfDays):
      self.doDay()
  
  def numberOfFish(self):
    return sum(self.fishInDays)


def main():
  input = fh.getMappedCommaSeparatedFirstLine('input/day6', int)
  firstDay = [input.count(x) for x in range(0, 9)]

  day = Day()
  day.ingestState(firstDay)
  day.doDays(256)

  print(f"{day.numberOfFish()} --> {day.fishInDays}")
  return

def test():
  input = [3,4,3,1,2]
  firstDay = [input.count(x) for x in range(0, 9)]

  day = Day()
  day.ingestState(firstDay)
  day.doDays(18)

  assert day.numberOfFish() == 26, f"{day.numberOfFish()} --> {day.fishInDays}"

if __name__ == "__main__":
  main()