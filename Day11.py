import fileHandler as fh
import gridHandler as gh

#0,0 is top left X horizontal, Y is vertical
class Field(gh.Grid):
  def doStep(self):
    return

def getIntList(line):
  return [int(element) for element in line]

def main():
  octopi = fh.getMappedLines('input/day11', getIntList)
  field = Field(octopi)
  field.print()

  print(field.getAllNeighbours(0, 0))

if __name__ == "__main__":
  main()