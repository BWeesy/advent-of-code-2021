import fileHandler as fh
from statistics import median

ANGLED_OPEN = '<'
ANGLED_CLOSE = '>'
CURLY_OPEN = '{'
CURLY_CLOSE = '}'
SQUARE_OPEN = '['
SQUARE_CLOSE = ']'
BRACKET_OPEN = '('
BRACKET_CLOSE = ')'

OPEN_BRACKETS = [ANGLED_OPEN, CURLY_OPEN, SQUARE_OPEN, BRACKET_OPEN]
CLOSE_BRACKETS = [ANGLED_CLOSE, CURLY_CLOSE, SQUARE_CLOSE, BRACKET_CLOSE]

BRACKET_PAIRS = {
  ANGLED_CLOSE   : ANGLED_OPEN,
  CURLY_CLOSE    : CURLY_OPEN,
  SQUARE_CLOSE   : SQUARE_OPEN,
  BRACKET_CLOSE  : BRACKET_OPEN,
}

ILLEGAL_SCORES = {
  BRACKET_CLOSE : 3,
  SQUARE_CLOSE : 57,
  CURLY_CLOSE : 1197,
  ANGLED_CLOSE : 25137
}

INCOMPLETE_SCORES = {
  BRACKET_OPEN : 1,
  SQUARE_OPEN : 2,
  CURLY_OPEN : 3,
  ANGLED_OPEN : 4
}

class ChunkValidator():
  def __init__(self) -> None:
    self.illegalCharacters = []
    self.startingChunk = []

  def setStartingChunk(self, chunk):
    self.startingChunk = chunk
    self.illegalCharacters = []

  def getIllegalScore(self):
    return ILLEGAL_SCORES[self.illegalCharacters[0]]

  def getIncompleteScore(self):
    completionChars = []
    for char in self.startingChunk:
      if len(completionChars) == 0:
        completionChars.append(char)
        continue
      if char in CLOSE_BRACKETS and completionChars[-1] == BRACKET_PAIRS[char]:
        completionChars.pop(-1)
        continue
      completionChars.append(char)
    #printChunk(completionChars)
    score = 0
    for char in reversed(completionChars):
      score *= 5
      score += INCOMPLETE_SCORES[char]
    return score

  def isIllegal(self):
    return len(self.illegalCharacters) > 0

  def validateChunk(self, chunk):
    self.setStartingChunk(chunk)
    self.validateStep(self.startingChunk.copy())

  def validateStep(self, startingChunk):
    #printChunk(startingChunk)
    if len(startingChunk) == 2 and startingChunk[0] in OPEN_BRACKETS and startingChunk[1] in CLOSE_BRACKETS and startingChunk[0] == BRACKET_PAIRS[startingChunk[1]]:
      #print(f"Leaf found")
      return
    if len(startingChunk) < 2:
      #print(f"Incomplete chunk - {printChunk(startingChunk)}")
      return
    openingBracket = startingChunk.pop(0)
    openBrackets = {ANGLED_OPEN: 0, CURLY_OPEN: 0, SQUARE_OPEN: 0, BRACKET_OPEN: 0}
    openBrackets[openingBracket] += 1
    nextChunk = []
    while len(startingChunk) > 0 and sum(openBrackets.values()) != 0:
      nextChar = startingChunk.pop(0)
      if nextChar in OPEN_BRACKETS:
        openBrackets[nextChar] += 1
        nextChunk.append(nextChar)
        #print(f"open Bracket - {nextChar} openBrackets - {openBrackets}")
        continue
      else:
        if openBrackets[BRACKET_PAIRS[nextChar]] == 0:
          self.illegalCharacters.append(nextChar)
          #print(f"Illegal - {nextChar}")
          return
        openBrackets[BRACKET_PAIRS[nextChar]] -= 1
        nextChunk.append(nextChar)
        #print(f"Legal close - {nextChar}")
        continue
    self.validateStep(nextChunk)
    self.validateStep(startingChunk)
    
def printChunk(chunk):
  print("".join(chunk))

def getCharList(line):
  return [char for char in line]

def getScores(lines):
  validator = ChunkValidator()

  illegalScore = 0
  incompleteScores = []
  for line in lines:
    validator.validateChunk(line)
    if validator.isIllegal():
      illegalScore += validator.getIllegalScore()
    else:
      incompleteScores.append(validator.getIncompleteScore())

  return illegalScore, median(incompleteScores)

def main():
  lines = fh.getMappedLines('input/day10', getCharList)
  print(getScores(lines))

def test():
  testData = ["[({(<(())[]>[[{[]{<()<>>", "[(()[<>])]({[<{<<[]>>(",
  "{([(<{}[<>[]}>{[]{[(<()>", "(((({<>}<{<{<>}{[]{[]{}",
  "[[<[([]))<([[{}[[()]]]", "[{[{({}]{}}([{[{{{}}([]",
  "{<[[]]>}<{[{[{[]{()[[[]", "[<(<(<(<{}))><([]([]()",
  "<{([([[(<>()){}]>(<<{{", "<{([{{}}[<[[[<>{}]]]>[]]"]
  lines = list(map(getCharList, testData))
  scores = getScores(lines)

  assert 26397 == scores[0]
  assert 288957 == scores[1]

  print("Day 10 Tests passed")

if __name__ == "__main__":
  main()