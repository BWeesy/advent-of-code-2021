import fileHandler as fh
import gridHandler as gh

class Fold():
  def __init__(self, vertical, position) -> None:
    self.vertical = vertical
    self.position = position

class Paper(gh.Grid):
  def __init__(self, points) -> None:
      super().__init__(points)
  
def processLines(lines):
  points = []
  folds = []
  for line in lines:
    if line.startswith('fold'):
      foldLine = line.split(' ')
      fold = foldLine[2].split('=')
      folds.append(Fold(fold[0] == 'x', fold[1]))
      continue
    if  len(line) > 0:
      pointLine = line.split(',')
      points.append((int(pointLine[0]), int(pointLine[1])))
  return points, folds

def doFold(isVertical, position):
  if isVertical:
    return
  else:
    return

def getDimensions(points):
  maxX = max([x for x, _ in points])
  maxY = max([y for _, y in points])
  return maxX, maxY

def createPaper(points):
  paper = Paper([])
  maxX, maxY = getDimensions(points)
  paper.fillEmptyPoints(maxX, maxY)
  for point in points:
    paper.setPoint(point[0], point[1], 1)
  return paper

def main():
  lines = fh.getLines('input/day13')
  points, folds = processLines(lines)
  paper = createPaper(points)
  print(paper.points)

  for fold in folds:
    paper.doFold(fold.vertical, fold.position)
  return

if __name__ == "__main__":
  main()
