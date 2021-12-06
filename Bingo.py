from fileHandler import getLines

class BoardUnit():
  def __init__(self, number):
    self.number = number
    self.marked = False

  def markNumber(self, number):
    if self.number == number:
      self.marked = True

  def __str__(self):
    return f"\x1b[32m {self.number}" if self.marked else f"\033[0m {self.number}"
  
class Card():
  def __init__(self, lines):
    self.cardData = []
    for line in lines:
      self.cardData.append([BoardUnit(int(x)) for x in filter(None,line.split(' '))])
  
  def printCard(self):
    for row in self.cardData:
      print("")
      for unit in row:
        print(unit, end = '')
    print("\033[0m")

  def markNumber(self, number):
    for row in self.cardData:
      for unit in row:
        unit.markNumber(number)

  def hasFullRow(self):
    won = False
    for row in self.cardData:
      rowCount = 0
      for unit in row:
        if unit.marked:
          rowCount += 1
      if rowCount == 5:
        won = True
    
    return won

  def hasFullColumn(self):
    markedPositions = [0,1,2,3,4]
    for row in self.cardData:
      markedPositions = [x for x in markedPositions if row[x].marked]
    return len(markedPositions) > 0
  
  def hasWon(self):
    return self.hasFullRow() or self.hasFullColumn()

  def getScore(self):
    unmarkedUnits = []
    for row in self.cardData:
      unmarkedUnits += filter(lambda unit: not unit.marked, row)
    score = 0
    for unit in unmarkedUnits:
      score += unit.number
    return score

def splitToCards(lines, n):
  filteredLines = list(filter(None, lines))
  for x in range(0, len(filteredLines), n):
      yield filteredLines[x: n+x]

def main():
  inputs = list(getLines('input/day4'))
  calledNumbers = list(map(int, inputs[0].split(",")))
  rawCards = splitToCards(inputs[1:], 5)

  cards = [Card(rawCard) for rawCard in rawCards]
  remainingCards = cards
  for calledNumber in calledNumbers:
    remainingCards
    winningCards = []
    for card in remainingCards:
      card.markNumber(calledNumber)
      if card.hasWon():
        print(f"Winning Score {calledNumber * card.getScore()}")
        winningCards.append(card)
    
    for card in winningCards:
      remainingCards.remove(card)

  return

if __name__ == "__main__":
  main()