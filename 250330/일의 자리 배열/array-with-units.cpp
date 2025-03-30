#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n[10];
    for(int i=0;  i<2; i++){
        cin >>n[i]; 
    }

    for(int i=2; i<10; i++){
        n[i] = (n[i-2]+n[i-1])%10;
    }
    for(int i=0; i<10 ; i++){
        cout << n[i]<< " ";
    }



    return 0;
}