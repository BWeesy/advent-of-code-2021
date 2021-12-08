def stripNewLine(line):
  return line.strip()

def getLines(file):
  lines = [str]
  with open(file, 'r') as raw:
    lines = raw.readlines()
    lines = map(stripNewLine, lines)
    raw.close()
  return lines

def getMappedLines(file, mappingFunction):
  return doMap(getLines(file), mappingFunction)
  
def getCommaSeparatedFirstLine(file):
  return list(getLines(file))[0].split(',')

def getMappedCommaSeparatedFirstLine(file, mappingFunction):
  return doMap(getCommaSeparatedFirstLine(file), mappingFunction)

def doMap(input, mappingFunction):
  return list(map(mappingFunction, input))