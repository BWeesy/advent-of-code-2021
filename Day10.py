import fileHandler as fh

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

class ChunkValidator():
  def __init__(self) -> None:
    self.illegalCharacters = []
    self.startingChunk = []

  def setStartingChunk(self, chunk):
    self.startingChunk = chunk
    self.illegalCharacters = []

  def getScore(self, chunk):
    self.setStartingChunk(chunk)
    self.validateChunk(self.startingChunk)
    print(f"Chunk validated - {self.illegalCharacters}")
    score = 0
    if len(self.illegalCharacters) > 0:
      if self.illegalCharacters[0] == BRACKET_CLOSE:
        score = 3
      if self.illegalCharacters[0] == SQUARE_CLOSE:
        score = 57
      if self.illegalCharacters[0] == CURLY_CLOSE:
        score = 1197
      if self.illegalCharacters[0] == ANGLED_CLOSE:
        score = 25137
    return score

  def validateChunk(self, startingChunk):
    printChunk(startingChunk)
    if len(startingChunk) == 2 and startingChunk[0] in OPEN_BRACKETS and startingChunk[1] in CLOSE_BRACKETS and startingChunk[0] == BRACKET_PAIRS[startingChunk[1]]:
      print(f"Leaf found")
      return
    if len(startingChunk) < 2:
      print(f"Incomplete chunk - {printChunk(startingChunk)}")
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
        print(f"open Bracket - {nextChar} openBrackets - {openBrackets}")
        continue
      else:
        if openBrackets[BRACKET_PAIRS[nextChar]] == 0:
          self.illegalCharacters.append(nextChar)
          print(f"Illegal - {nextChar}")
          return
        openBrackets[BRACKET_PAIRS[nextChar]] -= 1
        nextChunk.append(nextChar)
        print(f"Legal close - {nextChar}")
        continue
    self.validateChunk(nextChunk)
    self.validateChunk(startingChunk)
    
def printChunk(chunk):
  print("".join(chunk))

def getCharList(line):
  return [char for char in line]

def main():
  lines = fh.getMappedLines('input/day10', getCharList)

  validator = ChunkValidator()

  score = 0
  for line in lines:
    score += validator.getScore(line)
  print(score)

def test():
  testData = ["[({(<(())[]>[[{[]{<()<>>", "[(()[<>])]({[<{<<[]>>(",
  "{([(<{}[<>[]}>{[]{[(<()>", "(((({<>}<{<{<>}{[]{[]{}",
  "[[<[([]))<([[{}[[()]]]", "[{[{({}]{}}([{[{{{}}([]",
  "{<[[]]>}<{[{[{[]{()[[[]", "[<(<(<(<{}))><([]([]()",
  "<{([([[(<>()){}]>(<<{{", "<{([{{}}[<[[[<>{}]]]>[]]"]
  lines = list(map(getCharList, testData))
  
  validator = ChunkValidator()

  score = 0
  for line in lines:
    score += validator.getScore(line)
  print(score)

if __name__ == "__main__":
  main()