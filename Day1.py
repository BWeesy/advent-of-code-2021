from fileHandler import getLines
class dataWindow:
  def __init__(self, windowData, windowSize):
    self.windowData = windowData
    self.windowSize = windowSize

  def addDatum(self, datum):
    self.windowData.append(datum)
    self.trimOldestData(self.windowSize)

  def isFull(self):
    return len(self.windowData) == self.windowSize

  def trimOldestData(self, size):
    if len(self.windowData) > size:
      self.windowData.pop(0)

  def getSum(self):
    sum = 0
    if (self.isFull()):
      for datum in self.windowData:
        sum += datum
    return sum

def signalIncreased(last, next):
  return last < next

def main():
  windowedData = []
  window = dataWindow([], 3)
  for line in getLines('input/day1.txt'):
    next = int(line.strip())
    window.addDatum(next)
    if(window.isFull()):
      windowedData.append(window.getSum())

  increasedCount = -1
  last = 0
  for next in windowedData:
    if (signalIncreased(last, next)): 
      increasedCount += 1
    last = next

  print(increasedCount)

if __name__ == "__main__":
  main()