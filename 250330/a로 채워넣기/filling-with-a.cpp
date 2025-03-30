#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    string name;

    cin >> name ;
    int n = name.length();
    name[1] = 'a';
    name[n-2] = 'a';

    cout << name << endl;


    return 0;
}