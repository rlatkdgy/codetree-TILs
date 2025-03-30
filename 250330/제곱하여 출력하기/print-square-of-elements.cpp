#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    

    cin >> N;
    int a[N];

    for(int i=0; i < N; i++){
        cin >> a[i];
    }
    for(int i=0; i<N; i++){
        cout << a[i]*a[i]<< " ";
    }
    
    return 0;
}