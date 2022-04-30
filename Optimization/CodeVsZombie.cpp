#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

class Human
{
    public:
        Human(int id_, int x_, int y_) : id(id_), x(x_), y(y_) {}

        int id;
        int x;
        int y;
};

struct Zombie
{
    public:
        Zombie(int id_, int x_, int y_, int nextX_, int nextY_) : id(id_), x(x_), y(y_), nextX(nextX_), nextY(nextY_) {}

        int id;
        int x;
        int y;
        int nextX;
        int nextY;
};

int dist(int x1, int y1, int x2, int y2)
{
    return sqrt(pow(x1-x2, 2) + pow(y1-y2, 2));
}

int main()
{
    // game loop
    while (1) {
        vector<Human> humans;
        vector<Zombie> zombies;

        int playerX;
        int playerY;
        cin >> playerX >> playerY; cin.ignore();
        int humanCount;
        cin >> humanCount; cin.ignore();
        for (int i = 0; i < humanCount; i++) {
            int humanId;
            int humanX;
            int humanY;
            cin >> humanId >> humanX >> humanY; cin.ignore();
            humans.emplace_back(humanId, humanX, humanY);
        }
        int zombieCount;
        cin >> zombieCount; cin.ignore();
        for (int i = 0; i < zombieCount; i++) {
            int zombieId;
            int zombieX;
            int zombieY;
            int zombieXNext;
            int zombieYNext;
            cin >> zombieId >> zombieX >> zombieY >> zombieXNext >> zombieYNext; cin.ignore();
            zombies.emplace_back(zombieId, zombieX, zombieY, zombieXNext, zombieYNext);
        }

        // Find the human with zombie closest
        pair<int,int> target;
        int minDist = numeric_limits<int>::max();
        for (auto& human : humans)
        {
            Zombie* closestZombie;
            int closestZombieDist = numeric_limits<int>::max();
            for (auto& zombie : zombies)
            {
                int zombieDist = dist(human.x, human.y, zombie.x, zombie.y);
                if (closestZombieDist > zombieDist)
                {
                    closestZombieDist = zombieDist;
                    closestZombie = &zombie;
                }
            }

            if (closestZombieDist < minDist)
            {
                int distance = dist(playerX, playerY, human.x, human.y);
                if (closestZombieDist / 400.0 >= (max(distance - 2000, 0)) / 1000.0)
                {
                    target = {closestZombie->x, closestZombie->y};
                    minDist = closestZombieDist;
                }
            }
        }

        // If player close to all zombie
        bool shouldGoMiddle = true;
        for (auto& zombie : zombies)
        {
            for (auto& human : humans)
            {
                if (dist(human.x, human.y, zombie.x, zombie.y) < dist(playerX, playerY, zombie.x, zombie.y))
                {
                    shouldGoMiddle = false,
                    break;
                }
            }

            if (!shouldGoMiddle)
                break;
        }

        // Move to center zombie if close = true
        if (shouldGoMiddle)
        {
            double centerX = 0;
            double centerY = 0;
            for (auto& zombie : zombies)
            {
                centerX += zombie.x;
                centerY += zombie.y;
            }
            centerX /= zombies.size();
            centerY /= zombies.size();

            target = {centerX, centerY};
        }

        cout << target.first << " " << target.second << endl;
    }
}