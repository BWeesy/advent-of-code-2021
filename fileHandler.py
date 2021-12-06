def stripNewLine(line):
  return line.strip()

def getLines(file):
  lines = [str]
  with open(file, 'r') as raw:
    lines = raw.readlines()
    lines = map(stripNewLine, lines)
    raw.close()
  return lines