def leftOfTheLine(x0, y0, x1, y1, x2, y2):
    result = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    return result > 0

def onTheSameLine(x0, y0, x1, y1, x2, y2):
    result = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    return result == 0

def rightOfTheLine(x0, y0, x1, y1, x2, y2):
    result = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    return result < 0

def main():
    count = 0
    while count < 3:
        x0 = float(input("Enter coordinates for the three points p0, p1, and p2:\n"))
        y0 = float(input())
        x1 = float(input())
        y1 = float(input())
        x2 = float(input())
        y2 = float(input())

        if onTheSameLine(x0, y0, x1, y1, x2, y2):
            print(f"({x2:.1f}, {y2:.1f}) is on the same line from ({x0:.1f}, {y0:.1f}) to ({x1:.1f}, {y1:.1f})")
        elif leftOfTheLine(x0, y0, x1, y1, x2, y2):
            print(f"({x2:.1f}, {y2:.1f}) is on the left side of the line from ({x0:.1f}, {y0:.1f}) to ({x1:.1f}, {y1:.1f})")
        elif rightOfTheLine(x0, y0, x1, y1, x2, y2):
            print(f"({x2:.1f}, {y2:.1f}) is on the right side of the line from ({x0:.1f}, {y0:.1f}) to ({x1:.1f}, {y1:.1f})")
        else:
            print(f"({x2:.1f}, {y2:.1f}) is on the line segment from ({x0:.1f}, {y0:.1f}) to ({x1:.1f}, {y1:.1f})")

        count += 1

        if count < 3:
            print()

if __name__ == "__main__":
    main()