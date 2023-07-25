class Boundaries:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __contains__(self, item):
        x, y = item
        return 0 <= x < self.width and 0 <= y < self.height


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.limits = Boundaries(width, height)

    def __contains__(self, item):
        return item in self.limits


if __name__ == "__main__":
    grid = Grid(2, 3)
    print((1, 1) in grid)
