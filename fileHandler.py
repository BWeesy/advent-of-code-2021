def getLines(file):
  lines = [str]
  with open(file, 'r') as raw:
    lines = raw.readlines()
    raw.close()
  return lines