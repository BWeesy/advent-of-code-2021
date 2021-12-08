import fileHandler as fh

def getFuelCost(location, rendevous):
  numberOfSteps = abs(location - rendevous)
  return numberOfSteps * (numberOfSteps + 1) / 2

def main():
  subLocations = fh.getMappedCommaSeparatedFirstLine('input/day7', int)
  minTotalCost = sum(subLocations) * sum(subLocations)
  for rendevous in range(min(subLocations), (max(subLocations))):
    totalFuelCost = sum([getFuelCost(location, rendevous) for location in subLocations])
    if minTotalCost < totalFuelCost:
      print(f"Rendevous @ {rendevous-1} for totalCost {minTotalCost}")
      break
    minTotalCost = totalFuelCost

if __name__ == "__main__":
  main()