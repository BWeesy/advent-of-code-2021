import fileHandler as fh

ZERO = 0 
ONE = 1
TWO = 2
THREE = 3
FOUR = 4 
FIVE = 5 
SIX = 6  
SEVEN = 7
EIGHT = 8
NINE = 9 

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

def reverseLookup(dic, value):
  return list(dic.keys())[list(dic.values()).index(value)]

def isSubset(possibleSub, super):
  return possibleSub & super == possibleSub

def findEasySequences(code):
  knownCodes = {}
  for element in code:
    length = len(element)
    if length == 2:
      knownCodes[ONE] = convertElementToBinary(element)
    if length == 3:
      knownCodes[SEVEN] = convertElementToBinary(element)
    if length == 4:
      knownCodes[FOUR] = convertElementToBinary(element)
    if length == 7:
      knownCodes[EIGHT] = convertElementToBinary(element)
  return knownCodes

def determineNextKnownCode(codes, knownCodes):
  result = knownCodes
  for code in codes:
    binaryCode = convertElementToBinary(code)

    if binaryCode in knownCodes.values():
      continue

    if len(code) == 6 and FOUR in knownCodes and isSubset(knownCodes[FOUR], binaryCode):
      result[NINE] = binaryCode
      continue

    if len(code) == 6 and ONE in knownCodes and isSubset(knownCodes[ONE], binaryCode):
      result[ZERO] = binaryCode
      continue

    if len(code) == 6 and ONE in knownCodes and FOUR in knownCodes:
      result[SIX] = binaryCode
      continue

    if len(code) == 5 and SIX in knownCodes and isSubset(binaryCode, knownCodes[SIX]):
      result[FIVE] = binaryCode
      continue

    if len(code) == 5 and ONE in knownCodes and isSubset(knownCodes[ONE], binaryCode):
      result[THREE] = binaryCode
      continue

    if len(code) == 5 and SIX in knownCodes and NINE in knownCodes:
      result[TWO] = binaryCode
      continue
  return result

def determineAllKnownCodes(codes):
  knownCodes = findEasySequences(codes)
  while len(knownCodes) < 10:
    knownCodes = determineNextKnownCode(codes, knownCodes)
  return knownCodes

def convertReadOutToNumber(readout):
  result = 0
  for i, digit in enumerate(reversed(readout)):
    result += digit * pow(10, i)
  return result

def decodeAndSumOutput(codes, output):
  knownCodes = determineAllKnownCodes(codes)
  result = []
  for element in [convertElementToBinary(output) for output in output]:
    result.append(reverseLookup(knownCodes, element))
  return convertReadOutToNumber(result)

def main():
  lines = fh.getMappedLines('input/day8', extractInputOutput)

  result = sum([decodeAndSumOutput(codes, output) for codes, output in lines])

  print(f"Sum of all outputs {result}")

def test():
  codesWithOutputs = extractInputOutput('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf')
  knownCodes = determineAllKnownCodes(codesWithOutputs[0])

  assert knownCodes == {8: 127, 7: 104, 4: 102, 1: 96, 3: 122, 9: 126, 6: 63, 0: 125, 5: 62, 2: 91}, f"{knownCodes}"

  result = decodeAndSumOutput(codesWithOutputs[0], codesWithOutputs[1])

  assert result == 5353, f"{result}"

  print("Tests passed")

if __name__ == "__main__":
  main()