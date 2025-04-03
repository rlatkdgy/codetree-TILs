#include <iostream>
using namespace std;

int main() {
    // Please write your code here.


    int N;
    int cnt =0;
    cin >> N;
    for(int i=1; i<=100; i++ ){
         cnt += i;
       
        if(cnt>=N){
            cnt = i;
            break;
        }
       
    }
    cout << cnt;



    return 0;
}