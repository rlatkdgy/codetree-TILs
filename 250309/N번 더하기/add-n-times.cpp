#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A,N;
    cin >> A >> N;
    int sum = A+N;

    for(int i=0; i<N; i++){
        cout << sum << endl;
        sum += N;

    }
    return 0;
}