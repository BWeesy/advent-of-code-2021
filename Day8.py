import fileHandler as fh

CORRECT_SEQUENCES = {
'ZERO'  : 0b1110111,
'ONE'   : 0b0010010,
'TWO'   : 0b1011101,
'THREE' : 0b1011011,
'FOUR'  : 0b0111010,
'FIVE'  : 0b1101011,
'SIX'   : 0b1101111,
'SEVEN' : 0b1010010,
'EIGHT' : 0b1111111,
'NINE'  : 0b1111011,
}

CHAR_BINARY_MAP = {
  'a': 6,
  'b': 5,
  'c': 4,
  'd': 3,
  'e': 2,
  'f': 1,
  'g': 0,
}

def convertElementToBinary(element):
  binarySequence = 0b0
  for char in list(element):
    binarySequence = binarySequence ^ (1 << CHAR_BINARY_MAP[char])
  return binarySequence

def extractInputOutput(line):
  [codes, output] = line.split(" | ")
  codes = codes.split(" ")
  output = output.split(" ")
  return codes, output

def findEasySequences(code):
  knownCodes = {}
  for element in code:
    length = len(element)
    if length == 2:
      knownCodes['ONE'] = convertElementToBinary(element)
    if length == 3:
      knownCodes['SEVEN'] = convertElementToBinary(element)
    if length == 4:
      knownCodes['FOUR'] = convertElementToBinary(element)
    if length == 7:
      knownCodes['EIGHT'] = convertElementToBinary(element)
  return knownCodes

def main():
  codesWithOutputs = fh.getMappedLines('input/day8', extractInputOutput)
  oneFourSevenOrEightSum = 0

  for code, output in codesWithOutputs:
    knownCodes = findEasySequences(code)
    outputInBinary = [convertElementToBinary(output) for output in output]
    intersections = [x for x in outputInBinary if x in knownCodes.values()]
    oneFourSevenOrEightSum += len(intersections)
    print(f"{knownCodes} - {outputInBinary} - {intersections}")
    
  print(f"Intersections {oneFourSevenOrEightSum}")

if __name__ == "__main__":
  main()