#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.

    string name[100];

    for(int i=0; i<2; i++){
        cin >> name[i];
    }

    if(name[0].length()>name[1].length()){
        cout << name[0] << " "<< name[0].length();
    }else if(name[0].length()<name[1].length()){
        cout << name[1] << " "<< name[1].length();
    }else{
        cout << "same" << endl;
    }




    return 0;
}