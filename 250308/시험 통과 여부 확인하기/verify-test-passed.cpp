#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
   
    cin >> N;
    int a = 80-N;
    

    if (N>=80){
        cout << "pass" << endl;
    }else{
        cout << a <<" " <<"more score"<< endl;
    }
    return 0;
}