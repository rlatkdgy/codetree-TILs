#include <iostream>
#include <iomanip>
using namespace std;


int main() {
    // Please write your code here.

    int A,B;
    cin >> A >> B;
    int sum = A+B;
    double avg = sum/2.0;

    cout <<fixed << setprecision(1)<< sum << " " << avg;


    return 0;
}