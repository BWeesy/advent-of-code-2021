import fileHandler as fh

def main():
  subLocations = fh.getMappedCommaSeparatedFirstLine('input/day7', int)

  minTotalCost = sum(subLocations)
  for rendevous in range(min(subLocations), (max(subLocations))):
    totalFuelCost = sum([abs(location - rendevous) for location in subLocations])
    if minTotalCost < totalFuelCost:
      print(f"Rendevous @ {rendevous-1} for totalCost {minTotalCost}")
      break
    minTotalCost = totalFuelCost
  return

if __name__ == "__main__":
  main()