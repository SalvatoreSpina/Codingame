#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main()
{
    string s;
    getline(cin, s);
    int a = 0;
    int actual = 0;
    int i = 0;
    while (s[i]) 
    {
        if (s[i] == ' ')
            actual = 27;
        else
            actual = int(s[i])-64;
        while (a != actual)
        {

            if (abs(a-actual) <= 13){
                while (actual < a){a--;cout << "-";}
                while (actual > a){a++;cout << "+";}
            }
            else {
                int dist = 27 - abs(a-actual);
                if (actual < a){while (dist){cout << "+";dist--;}}
                else {while (dist){cout << "-";dist--;}}
                a = actual;
            }
        }
        cout << ".";
        i++;
    }
    cout << "\n";
}