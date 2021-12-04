class dataWindow:
  def __init__(self, windowData, windowSize):
    self.windowData = windowData
    self.windowSize = windowSize

  def addDatum(self, datum):
    self.windowData.append(datum)
    return self.trimOldestData(self.windowSize)

  def isFull(self):
    return len(self.windowData) == self.windowSize

  def trimOldestData(self, size):
    if len(self.windowData) > size:
      return self.windowData.pop(0)
    else:
      return None

  def getSum(self):
    sum = 0
    if (self.isFull()):
      for datum in self.windowData:
        sum += datum
    return sum

def getLines(file):
  file1 = open(file, 'r')
  lines = file1.readlines()
  file1.close()
  return lines

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