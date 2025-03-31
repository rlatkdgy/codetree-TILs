#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int a;
    cin >> a;

    for( ; a<101; a++)
        if(100>=a && a>=90){
            cout << "A" << " ";
        }else if(a>=80){
            cout << "B" << " ";
        }else if(a>=70){
            cout << "C" << " ";
        }else if(a>=60){
            cout << "D" << " ";
        }else if(a<60){
            cout << "F" << " ";
        }
        
       
    return 0;
}