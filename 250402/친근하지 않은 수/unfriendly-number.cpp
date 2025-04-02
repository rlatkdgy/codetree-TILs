#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    //친근한수는 2,3,5로 떨어지는수
    int N;
    int cnt =0;
    cin >> N;

    for (int i=1; i<N+1; i++){
        if(i%5==0){
            cnt += 1;
            break;
        }else if(i%3==0){
            cnt +=1;
            break;
        }else if(i%2==0){
            cnt +=1;
        }

    }
    cout << cnt ;
    return 0;
}