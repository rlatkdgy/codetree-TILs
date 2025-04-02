#include <iostream>
using namespace std;

int main() {
    int N;
    int cnt = 0;
    cin >> N;

for (int i = 1; i <= N; i++){
    if(i%5==0){
        cnt += 1;
    }else if(i%3==0){
        cnt +=1;
    }else if(i%2==0){
        cnt +=1;
    }

}
cout << N-cnt ;
}