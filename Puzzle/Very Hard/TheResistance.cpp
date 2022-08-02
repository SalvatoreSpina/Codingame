#include <iostream>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

typedef long long ll;

struct Nodes 
{
    Nodes* dt    = nullptr;
    Nodes* ds    = nullptr;
    ll     valid = 0;
};

string encode(string input) {
    string toPrint;
    for (auto& c : input)
    {
        switch (c)
        {
            case 'A': toPrint += ".-"  ; break;
            case 'B': toPrint += "-..."; break;
            case 'C': toPrint += "-.-."; break;
            case 'D': toPrint += "-.." ; break;
            case 'E': toPrint += "."   ; break;
            case 'F': toPrint += "..-."; break;
            case 'G': toPrint += "--." ; break;
            case 'H': toPrint += "...."; break;
            case 'I': toPrint += ".."  ; break;
            case 'J': toPrint += ".---"; break;
            case 'K': toPrint += "-.-" ; break;
            case 'L': toPrint += ".-.."; break;
            case 'M': toPrint += "--"  ; break;
            case 'N': toPrint += "-."  ; break;
            case 'O': toPrint += "---" ; break;
            case 'P': toPrint += ".--."; break;
            case 'Q': toPrint += "--.-"; break;
            case 'R': toPrint += ".-." ; break;
            case 'S': toPrint += "..." ; break;
            case 'T': toPrint += "-"   ; break;
            case 'U': toPrint += "..-" ; break;
            case 'V': toPrint += "...-"; break;
            case 'W': toPrint += ".--" ; break;
            case 'X': toPrint += "-..-"; break;
            case 'Y': toPrint += "-.--"; break;
            case 'Z': toPrint += "--.."; break;
        }
    }
    return toPrint;
}

void insert(Nodes* node, string wd, ll pos = 0) {
    while (pos < wd.size()) 
    {
        if (wd[pos] == '.') 
        {
            if (!node->dt) node->dt = new Nodes();
            node = node->dt;
        }
        else 
        {
            if (!node->ds) node->ds = new Nodes();
            node = node->ds;
        }
        pos += 1;
    }
    node->valid++;
}

void deleteNodes(Nodes* node) {
    if (node->dt) deleteNodes(node->dt);
    if (node->ds) deleteNodes(node->ds);
    delete node;
}

string L, W;
Nodes* root = new Nodes();
map<ll, ll> cache;

ll solve(ll pos) {
    Nodes* node = root;
    ll solutions = 0;
    while (pos < L.size()) 
    {
        if      ((L[pos] == '.') && node->dt) {node = node->dt;}
        else if ((L[pos] == '-') && node->ds) {node = node->ds;}
        else break;
        
        if (node->valid) 
        {
            if (pos == L.size()-1) {solutions += node->valid;}
            else {
                if (cache.find(pos+1) != cache.end()) 
                    solutions += node->valid *  cache[pos+1];
                else 
                {
                    ll toPrint = solve(pos+1);
                    if (toPrint > 0) solutions += node->valid * toPrint, cache[pos+1] = toPrint;
                }
            }
        }
        ++pos;
    }
    return solutions;
}

int main() {
    int N;
    cin >> L >> N; cin.ignore();
    
    for (int i = 0; i < N; i++)  
    {
        cin >> W; cin.ignore();
        insert(root, encode(W));
    }
    cout << solve(0) << endl;
    deleteNodes(root);
}