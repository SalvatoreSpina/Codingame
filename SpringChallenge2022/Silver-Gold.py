from cmath import pi
import sys
from collections import namedtuple
import math
import random

# Functions

def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def isInCircle(x0, y0, radius, angle):
    x = x0 + radius * math.cos(angle)
    y = y0 + radius * math.sin(angle)
    return int(x), int(y)

def inRange(monster_x, monster_y, x, y, radius):
    return dist(monster_x, monster_y, x, y) <= radius

def getGuardPosition(x, y, radius):
    pos = []
    for i in range(12):
        angle = 2 * pi / 12 * (0.5+i)
        x_, y_ = isInCircle(x, y, radius, angle)
        if x_ < 0 or y_ < 0 or x_ > mapW or y_ > mapH:
            continue
        pos.append((x_, y_))
    return pos

# Functions

Entity = namedtuple('Entity', ['id', 'type', 'x', 'y', 'shieldLife', 'isControlled', 'health', 'vx', 'vy', 'nearBase', 'threatFor'])

MonsterType = 0
MyHeroType = 1
OpHeroType = 2

mapW, mapH = 17630, 9000

baseX, baseY = [int(i) for i in input().split()]
opponentBaseX, opponentBaseY = mapW-baseX, mapH-baseY
heroesPerPlayer = int(input())

attackOn = False

# Game Loop
while True:
    myHealth, myMana = [int(j) for j in input().split()]
    enemyHealth, enemyMana = [int(j) for j in input().split()]
    entityCount = int(input())  # Amount of heros and monsters you can see

    isMonsterTargeted = {}

    monsters = []
    myHeroes = []
    oppHeroes = []
    for i in range(entityCount):
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [int(j) for j in input().split()]
        entity = Entity(
            _id,            # _id: Unique identifier
            _type,          # _type: 0=monster, 1=your hero, 2=opponent hero
            x, y,           # x,y: Position of this entity
            shield_life,    # shield_life: Ignore for this league; Count down until shield spell fades
            is_controlled,  # is_controlled: Ignore for this league; Equals 1 when this entity is under a control spell
            health,         # health: Remaining health of this monster
            vx, vy,         # vx,vy: Trajectory of this monster
            near_base,      # near_base: 0=monster with no target yet, 1=monster targeting a base
            threat_for,      # threat_for: Given this monster's trajectory, is it a threat to 1=your base, 2=your opponent's base, 0=neither
        )

        if _type == MonsterType:
            monsters.append(entity)
            isMonsterTargeted[entity.id] = False
        elif _type == MyHeroType:
            myHeroes.append(entity)
        elif _type == OpHeroType:
            oppHeroes.append(entity)

    isHeroUsed = [False] * 3
    actions = [None,None,None]
    idAttacker = 1

    if myMana > 200:
        attackOn = True

    while True:
        bestAction = None
        bestValue = 0
        bestHero = None
        bestMonster = None

        for i in range(heroesPerPlayer):

            if isHeroUsed[i]:
                continue

            hero = myHeroes[i]

            # Moving to defense
            maxDist = 6200
            if attackOn:
                maxDist = 4500
            x, y = getGuardPosition(baseX, baseY, maxDist)[i]
            value = 1e5
            if value > bestValue:
                bestValue = value
                bestHero = i
                bestMonster = None
                if hero.x != x or hero.y != y:
                    bestAction = f'MOVE {x} {y} DEFENSE'
                else:
                    bestAction = f'WAIT HERO {i}'

            # Wind spell low prio
            if myMana >= 10:
                isMonsterNear = False
                for m in monsters:
                    if inRange(m.x, m.y,  hero.x, hero.y, 1280) and m.shieldLife == 0 and m.health+3 > 2*dist(m.x, m.y, baseX, baseY)/400:
                        isMonsterNear = True
                        break
                if isMonsterNear:
                    value = 1e8
                    if value > bestValue:
                        bestValue = value
                        bestHero = i
                        bestMonster = None
                        bestAction = f'SPELL WIND {opponentBaseX} {opponentBaseY} RED'

            # Farm strat
            for m in monsters:
                if isMonsterTargeted[m.id] or not inRange(m.x, m.y, baseX, baseY, 9000):
                    continue
                value = 1e6 - dist(m.x, m.y, hero.x, hero.y)
                if value > bestValue:
                    bestValue = value
                    bestHero = i
                    bestAction = f'MOVE {m.x + m.vx} {m.y + m.vy} LIMITLESS {m.id}'
                    bestMonster = m

            # Defense & Attack
            for m in monsters:
                if isMonsterTargeted[m.id] or not ((m.nearBase == 1 and m.threatFor == 1) or (m.nearBase == 0 and m.threatFor == 1)):
                    continue
                value = 1e7 - dist(baseX, baseY, m.x, m.y) - dist(m.x, m.y, hero.x, hero.y)
                if value > bestValue:
                    bestValue = value
                    bestAction = f'MOVE {m.x+m.vx} {m.y+m.vy} RED {m.id}'
                    bestHero = i
                    bestMonster = m

            # Saboting 
            if attackOn and i == idAttacker:

                # Heroe(s) to enemy base
                exRadius = random.randint(1500, 6000)
                possiblePosition = getGuardPosition(opponentBaseX, opponentBaseY, exRadius)
                targetX, targetY = random.choice(possiblePosition)
                value = 1e9
                if value > bestValue:
                    bestValue = value
                    bestHero = i
                    bestAction = f'MOVE {targetX} {targetY} PURPLE'
                    bestMonster = None

                # Keeping always mana for higher prio
                if myMana >= 30:

                    # Spell Shield if needed
                    for m in monsters:
                        if not ((m.nearBase == 1 and m.threatFor == 2) or (m.nearBase == 0 and m.threatFor == 2)):
                            continue
                        if m.shieldLife > 0 or dist(m.x, m.y, hero.x, hero.y) > 2200:
                            continue
                        if dist(m.x, m.y, opponentBaseX, opponentBaseY) > 5000:
                            continue
                        if m.health/2 < (dist(m.x, m.y, opponentBaseX, opponentBaseY) - 300)/400:
                            continue
                        value = 4e9
                        if value > bestValue:
                            bestValue = value
                            bestHero = i
                            bestAction = f'SPELL SHIELD {m.id} INFINITY {m.id}'
                            bestMonster = None

                    # Push with wind
                    isMonsterNear = 0
                    for m in monsters:
                        if inRange(m.x, m.y,  opponentBaseX, opponentBaseY, 5000+2200) and inRange(m.x, m.y,  hero.x, hero.y, 1280) and m.shieldLife == 0:
                            isMonsterNear += 1
                    if isMonsterNear >= 2:
                        value = 3e9
                        if value > bestValue:
                            bestValue = value
                            bestHero = i
                            bestMonster = None
                            bestAction = f'SPELL WIND {opponentBaseX} {opponentBaseY} RED'

                    # Use control
                    for m in monsters:
                        if (m.nearBase == 1 and m.threatFor == 2) or (m.nearBase == 0 and m.threatFor == 2):
                            continue
                        if m.health < 15:
                            continue
                        if dist(m.x, m.y, hero.x, hero.y) > 2200 or dist(hero.x, hero.y, opponentBaseX, opponentBaseY) > 7000:
                            continue
                        if dist(m.x, m.y, opponentBaseX, opponentBaseY) < 5000:
                            continue
                        value = 2e9
                        if value > bestValue:
                            bestValue = value
                            bestHero = i
                            bestAction = f'SPELL CONTROL {m.id} {opponentBaseX} {opponentBaseY} INFINITY {m.id}'
                            bestMonster = None

                    # Control on heroes
                    for opponent_hero in oppHeroes:
                        if opponent_hero.shieldLife > 0:
                            continue
                        if not inRange(opponent_hero.x, opponent_hero.y, opponentBaseX, opponentBaseY, 5000):
                            continue
                        if not inRange(opponent_hero.x, opponent_hero.y, hero.x, hero.y, 2200):
                            continue
                        if_attack_monster = 0
                        for m in monsters:
                            if inRange(m.x, m.y, opponent_hero.x, opponent_hero.y, 800):
                                if_attack_monster += 1
                        if if_attack_monster > 0:
                            value = 5e9 + if_attack_monster
                            if value > bestValue:
                                bestValue = value
                                bestHero = i
                                bestAction = f'SPELL CONTROL {opponent_hero.id} {mapW//2 } {mapH//2} BLUE {opponent_hero.id}'
                                bestMonster = None

                    # Wind opponent heroes
                    for opponent_hero in oppHeroes:
                        if opponent_hero.shieldLife > 0:
                            continue
                        if not inRange(opponent_hero.x, opponent_hero.y, opponentBaseX, opponentBaseY, 5000):
                            continue
                        if not inRange(opponent_hero.x, opponent_hero.y, hero.x, hero.y, 1280):
                            continue
                        if_attack_monster = 0
                        for m in monsters:
                            if inRange(m.x, m.y, opponent_hero.x, opponent_hero.y, 800) and m.shieldLife > 0:
                                if_attack_monster += 1
                        if if_attack_monster > 0:
                            value = 6e9 + if_attack_monster
                            if value > bestValue:
                                bestValue = value
                                bestHero = i
                                bestAction = f'SPELL WIND  {mapW//2 } {mapH//2} RED'
                                bestMonster = None

        if bestHero is None:
            break

        if bestMonster is not None:
            isMonsterTargeted[bestMonster.id] = True

        if 'SPELL' in bestAction:
            myMana -= 10

        isHeroUsed[bestHero] = True
        actions[bestHero] = bestAction

    for action in actions:
        print(action)