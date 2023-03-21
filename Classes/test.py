def slow_movement(position, time = 1000):
    """ Move the servo slowly to a specific position in a specified total time in ms """
    currentPos = 1000
    startPos = currentPos
    stepSize = 0
    stepTime = 0
    while stepTime == 0:
        stepSize += (1 if (position>currentPos) else -1)
        stepTime = int(time / ((position-currentPos)/stepSize))
    substepCount = (position-currentPos) // stepSize
    print(stepTime, stepSize, substepCount)
    for x in range(1, substepCount+1):
        print(f"move to: {startPos+stepSize*x}, wait: {stepTime}")
    print(f"move to: {position}")

slow_movement(990, 100)
