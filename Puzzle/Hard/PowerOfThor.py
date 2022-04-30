import sys

WIDE = 4

class Thor:
    tx = 0
    ty = 0
    h = 0
    n = 0
    enemy = []
    action = "STRIKE"

    def __init__(self):
        self.tx, self.ty = [int(i) for i in input().split()]

    def scan(self):
        self.h, self.n = [int(i) for i in input().split()]
        self.enemy.clear()
        for i in range(self.n):
            x, y = [int(j) for j in input().split()]
            self.enemy.append({'x': x, 'y': y})

    def findCenter(self):
        centerX = centerY = 0
        for giant in self.enemy:
            centerX += giant['x']
            centerY += giant['y']

        centerX /= len(self.enemy)
        centerY /= len(self.enemy)
        print(int(centerX), int(centerY), file=sys.stderr)
        return [int(centerX), int(centerY)]

    def closest(self, x, y):
        closestEnemy = []
        for giant in self.enemy:
            if ((abs(giant['x'] - x) <= WIDE) and (abs(giant['y'] - y) <= WIDE)):
                closestEnemy.append(giant)

        return closestEnemy

    def enemyTooClose(self, x, y):
        for giant in self.enemy:
            if ((abs(giant['x'] - x) <= 1) and (abs(giant['y'] - y) <= 1)):
                return True
        return False

    def findMove(self, cx, cy):
        if (cx > self.tx):
            if (cy > self.ty):
                self.tx += 1
                self.ty += 1
                self.action = "SE"
            elif (cy < self.ty):
                self.tx += 1
                self.ty -= 1
                self.action = "NE"
            else:
                self.tx += 1
                self.action = "E"

        elif (cx < self.tx):
            if (cy > self.ty):
                self.tx -= 1
                self.ty += 1
                self.action = "SW"
            elif (cy < self.ty):
                self.tx -= 1
                self.ty -= 1
                self.action = "NW"
            else:
                self.tx -= 1
                self.action = "W"
                
        else:
            if (cy > self.ty):
                self.ty += 1
                self.action = "S"
            elif (cy < self.ty):
                self.ty -= 1
                self.action = "N"
            else:
                self.action = "WAIT"

    def dist(self, first, second):
        return int(abs(first[0] - second[0]) + abs(first[1] - second[1]))

    def runAway(self):
        profit = []
        if self.tx < 40:
            x = self.tx + 1
            y = self.ty
            if (not (self.enemyTooClose(x, y))):
                profit.append(["E", [len(self.closest(x, y)), [x, y]]])

        if self.ty > 0:
            x = self.tx
            y = self.ty - 1
            if not (self.enemyTooClose(x, y)):
                profit.append(["N", [len(self.closest(x, y)), [x, y]]])

        if (self.tx < 40) and (self.ty > 0):
            x = self.tx + 1
            y = self.ty - 1
            if not (self.enemyTooClose(x, y)):
                profit.append(["NE", [len(self.closest(x, y)), [x, y]]])

        if (self.tx > 0) and (self.ty > 0):
            x = self.tx - 1
            y = self.ty - 1
            if not (self.enemyTooClose(x, y)):
                profit.append(["NW", [len(self.closest(x, y)), [x, y]]])

        if self.ty < 18:
            x = self.tx
            y = self.ty + 1
            if not (self.enemyTooClose(x, y)):
                profit.append(["S", [len(self.closest(x, y)), [x, y]]])

        if (self.tx < 40) and (self.ty < 18):
            x = self.tx + 1
            y = self.ty + 1
            if not (self.enemyTooClose(x, y)):
                profit.append(["SE", [len(self.closest(x, y)), [x, y]]])

        if (self.tx > 0) and (self.ty > 0):
            x = self.tx - 1
            y = self.ty - 1
            if not (self.enemyTooClose(x, y)):
                profit.append(["SW", [len(self.closest(x, y)), [x, y]]])

        if self.tx > 0:
            x = self.tx - 1
            y = self.ty
            if not (self.enemyTooClose(x, y)):
                profit.append(["W", [len(self.closest(x, y)), [x, y]]])

        self.action = "STRIKE"
        bestOption = [0, [0, 0]]
        bestDist = 0
        center = self.findCenter()
        for i in range(len(profit)):
            option = profit[i]
            if ((option[1][0] > bestOption[0]) or (
                        (option[1][0] == bestOption[0]) and (self.dist(option[1][1], center) > bestDist))):
                bestOption = option[1]
                self.action = option[0]
                bestDist = self.dist(bestOption[1], center)

        if self.action != "STRIKE":
            self.tx = bestOption[1][0]
            self.ty = bestOption[1][1]

    def bestMove(self):
        centerX, centerY = self.findCenter()
        if (not (self.enemyTooClose(self.tx, self.ty))):
            self.findMove(centerX, centerY)
        else:
            self.runAway()

    def move(self):
        closestEnemy = self.closest(self.tx, self.ty)
        if len(self.enemy) == len(closestEnemy):
            self.action = "STRIKE"
        else:
            self.bestMove()
        print(self.action)

thor = Thor()

# Game loop
while True:
    thor.scan()
    thor.move()