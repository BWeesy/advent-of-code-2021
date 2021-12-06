from fileHandler import getLines

def extractBinaryNumberFromString(inputString):
  return int(inputString, 2)

#109876543210 - index
#011010111110 - example input
def getValueAtPosition(binaryInput, index):
  if index > 11:
    raise IndexError(f"Inputs are 12 bits long, indexed right to left from 0. Provided index was {index}")
  return (binaryInput & (1 << index)) >> index

def getFrequencyAtPositions(inputs, inputLength):
  totalsAtPosition=[0] * inputLength
  count = 0
  for input in inputs:
    count += 1
    for index in range(inputLength):
      totalsAtPosition[inputLength-1-index] += getValueAtPosition(input, index)
  return count, totalsAtPosition

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

def main():
  inputLength = 12
  inputs = map(extractBinaryNumberFromString, getLines('input/day3'))

  [count, frequencies] = getFrequencyAtPositions(inputs, inputLength)
  [gamma, epsilon] = getGammaAndEpsilon(count, frequencies)
  print(f"Power consumption: {gamma * epsilon}")

if __name__ == "__main__":
  main()