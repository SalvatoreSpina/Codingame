import sys
from collections import namedtuple

# Functions

def dist(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2) ** 0.5

# Utilities

Entity = namedtuple('Entity', ['id', 'type', 'x', 'y', 'shieldLife', 'isControlled', 'health', 'vx', 'vy', 'nearBase', 'threatFor'])

MonsterType = 0
MyHeroType = 1
OpHeroType = 2

baseX, baseY = [int(i) for i in input().split()]
heroesPerPlayer = int(input())

# Game Loop
while True:
    myHealth, myMana = [int(j) for j in input().split()]
    enemyHealth, enemyMana = [int(j) for j in input().split()]
    entityCount = int(input())  # Amount of heros and monsters you can see

    monsters = []
    myHeroes = []
    oppHeroes = []
    for i in range(entityCount):
        _id, _type, x, y, shield_life, is_controlled, health, vx, vy, near_base, threat_for = [
            int(j) for j in input().split()]
        entity = Entity(
            _id,            # _id: Unique identifier
            _type,          # _type: 0=monster, 1=your hero, 2=opponent hero
            x, y,           # x,y: Position of this entity
            shield_life,    # shield_life: Ignore for this league; Count down until shield spell fades
            is_controlled,  # is_controlled: Ignore for this league; Equals 1 when this entity is under a control spell
            health,         # health: Remaining health of this monster
            vx, vy,         # vx,vy: Trajectory of this monster
            near_base,      # near_base: 0=monster with no target yet, 1=monster targeting a base
            threat_for      # threat_for: Given this monster's trajectory, is it a threat to 1=your base, 2=your opponent's base, 0=neither
        )

        if _type == MonsterType:
            monsters.append(entity)
        elif _type == MyHeroType:
            myHeroes.append(entity)
        elif _type == OpHeroType:
            oppHeroes.append(entity)

    wantMyBase = None
    toBeDangerous = 5500
    dangerousMonster = None

    if monsters:
        wantMyBase = [m for m in monsters if (m.nearBase == 1 and m.threatFor == 1) or (m.nearBase == 0 and m.threatFor == 1)]
        if wantMyBase:
            wantMyBase.sort(key=lambda m: dist(m.x, m.y, baseX, baseY))
            if dist(wantMyBase[0].x, wantMyBase[0].y, baseX, baseY) < toBeDangerous:
                dangerousMonster = wantMyBase[0]
    for i in range(heroesPerPlayer):
        if dangerousMonster:
            print(f'MOVE {dangerousMonster.x} {dangerousMonster.y}')
            continue
        if wantMyBase:
            monster = wantMyBase[i % len(wantMyBase)]
            print(f'MOVE {monster.x} {monster.y}')
        else:
            if dist(myHeroes[i].x, myHeroes[i].y, baseX, baseY) > 3000:
                print(f'MOVE {baseX} {baseY}')
            else:
                print('WAIT')