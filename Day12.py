import fileHandler as fh
from typing import List

START = "start"
END = "end"

class CaveSystem():
  def __init__(self, lines) -> None:
      self.navDictionary = self.generateNavigationDictionary(lines)
      self.paths = []

  def generateNavigationDictionary(self, lines) -> List[str]:
    navDict = {}
    for line in lines:
      caves = line.split('-')
      if caves[0] in navDict.keys():
        navDict[caves[0]] = set([caves[1]]).union(navDict[caves[0]])
      else:
        navDict[caves[0]] = set([caves[1]])

      if caves[1] in navDict.keys():
        navDict[caves[1]] = set([caves[0]]).union(navDict[caves[1]])
      else:
        navDict[caves[1]] = set([caves[0]])
    return navDict

  def canVisitFromNode(self, visited:list, currentNode) -> bool:
    return [node for node in self.navDictionary[currentNode] if node not in visited or node.isupper()]

  def recursiveVist(self, visited:list , currentNode:str):
    newVisited = visited.copy()
    newVisited.append(currentNode)
    if currentNode == END:
      self.paths.append(newVisited)
      return
    canVisit = self.canVisitFromNode(newVisited, currentNode)
    for node in canVisit:
      self.recursiveVist(newVisited, node)
    return

  def getAllPaths(self):
    self.recursiveVist([], START)
    return self.paths
    

def main():
  lines = fh.getLines('input/day12')
  caveSystem = CaveSystem(lines)
  caveSystem.recursiveVist([], START)
  print(f"Number of paths {len(caveSystem.paths)}")
  return

def test():
  testData1 = [ "start-A", "start-b", "A-c", "A-b", "b-d", "A-end", "b-end" ]
  caveSystem = CaveSystem(testData1)
  assert len(caveSystem.getAllPaths()) == 10

  testData2 = ["dc-end", "HN-start", "start-kj", "dc-start", "dc-HN", "LN-dc", "HN-end", "kj-sa", "kj-HN", "kj-dc", ]
  caveSystem = CaveSystem(testData2)
  assert len(caveSystem.getAllPaths()) == 19

  testData3 = ["fs-end", "he-DX", "fs-he", "start-DX", "pj-DX", "end-zg", "zg-sl", "zg-pj", "pj-he", "RW-he", "fs-DX", "pj-RW", "zg-RW", "start-pj", "he-WI", "zg-he", "pj-fs", "start-RW"]
  caveSystem = CaveSystem(testData3)
  assert len(caveSystem.getAllPaths()) == 226

  actualData = fh.getLines('input/day12')
  caveSystem = CaveSystem(actualData)
  assert set(caveSystem.canVisitFromNode(['ci'], START)) == set(['DK', 'TF'])
  assert set(caveSystem.canVisitFromNode([], START)) == set(['DK', 'TF', 'ci'])

  print("Day 12 Tests passed")
if __name__ == "__main__":
  main()