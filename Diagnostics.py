from fileHandler import getLines

INPUT_LENGTH = 12

def extractBinaryNumberFromString(inputString):
  return int(inputString, 2)

#109876543210 - index
#011010111110 - example input
def getValueAtPosition(binaryInput, index):
  if index > 11:
    raise IndexError(f"Inputs are 12 bits long, indexed right to left from 0. Provided index was {index}")
  return (binaryInput & (1 << index)) >> index #Create bit mask, apply bit mask, then remove trailing zeros to find digit at given index

def getFrequencyAtPosition(inputs, index):
  frequency = 0
  for input in inputs:
    frequency += getValueAtPosition(input, index)
  return frequency

def getFrequencyAtPositions(inputs):
  totalsAtPosition=[0] * INPUT_LENGTH
  for index in range(INPUT_LENGTH):
    totalsAtPosition[INPUT_LENGTH-1-index] += getFrequencyAtPosition(inputs, index)
  return totalsAtPosition

def filterInputsAtIndex(inputs, filter, index):
  result = []
  for input in inputs:
    if(getValueAtPosition(input, index) == filter):
      result.append(input)
  return result

def getGammaAndEpsilon(count, frequencies):
  gammaString = ''
  epsilonString = ''
  for frequency in frequencies:
    proportion = frequency/count
    if proportion > 0.5: #more 1's
      gammaString += '1'
      epsilonString += '0'
    else: #more 0's
      gammaString += '0'
      epsilonString += '1'
    print(f"{gammaString} - {epsilonString}")

  return int(gammaString, 2), int(epsilonString, 2)

def getOxygenRating(inputs, inputLength):
  result = inputs
  for index in reversed(range(inputLength)):
    if(len(result) == 1):
      break
    frequency = getFrequencyAtPosition(result, index)
    if(frequency/len(result) >= 0.5): #more 1's
      result = filterInputsAtIndex(result, 1, index)
    else: #more 0's
      result = filterInputsAtIndex(result, 0, index)
  return result[0]

def getScrubberRating(inputs, inputLength):
  result = inputs
  for index in reversed(range(inputLength)):
    if(len(result) == 1):
      break
    frequency = getFrequencyAtPosition(result, index)
    print(f"index:{index} freq:{frequency} count:{len(result)} prop:{frequency/len(result)} result:{list(map(bin, result))}")
    if(frequency/len(result) <= 0.5): #more 0's
      result = filterInputsAtIndex(result, 1, index)
    else: #more 1's
      result = filterInputsAtIndex(result, 0, index)
  return result[0]

def main():
  inputs = list(map(extractBinaryNumberFromString, getLines('input/day3')))

  [gamma, epsilon] = getGammaAndEpsilon(len(inputs), getFrequencyAtPositions(inputs))
  print(f"Power consumption: {gamma * epsilon}")

  oxygenRating = getOxygenRating(inputs, INPUT_LENGTH)
  scrubberRating = getScrubberRating(inputs, INPUT_LENGTH)
  print(f"Life Support Rating: {oxygenRating * scrubberRating}")

def test():
  testData = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]
  inputs = list(map(extractBinaryNumberFromString, testData))

  filterResult = filterInputsAtIndex(inputs, 1, 4)
  expectedResult = ["11110", "10110", "10111", "10101", "11100", "10000", "11001"]
  assert filterResult == list(map(extractBinaryNumberFromString, expectedResult)), f"{list(map(bin, filterResult))}"

  oxygenResult = getOxygenRating(inputs, 5)
  assert oxygenResult == 23, f"{oxygenResult} - {bin(oxygenResult)}"

  scrubberResult = getScrubberRating(inputs, 5)
  assert scrubberResult == 10, f"{scrubberResult} - {bin(scrubberResult)}"

if __name__ == "__main__":
  test()