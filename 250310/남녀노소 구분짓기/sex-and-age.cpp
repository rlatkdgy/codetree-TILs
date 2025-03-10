#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a;
    int b;
    cin >> a >> b;

    if(a==0){
        if(b>=19){
            cout << "MAN" << endl;
        }else{
            cout << "BOY" << endl;
        }
    }else{
        if(b>=19){
            cout << "WOMAN" << endl;
        }else{
            cout << "GIRL"<< endl;
        }
    }


    return 0;
}