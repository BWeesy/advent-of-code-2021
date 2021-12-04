def getLines(file):
  file1 = open(file, 'r')
  lines = file1.readlines()
  file1.close()
  return lines