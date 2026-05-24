
С какого-то перепугу код на C++ (вероятно, был призван показать, что на C++ можно писать в питонячьем стиле):

```cpp
/*
    https://inf-ege.sdamgia.ru/problem?id=27424
*/
#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main() {
    fstream FILE;
    int N;
    long int sum = 0;
    
    FILE.open("27-B_demo.txt");
    FILE >> N;
    vector<int> A(N), B(N), C(N);
    for (int i = 0; i < N; i++){
        FILE >> A[i] >> B[i];
    }
    FILE.close();

    for (int i = 0; i < N; i++){
        sum += max(A[i], B[i]);
        C[i] = abs(A[i] - B[i]);
    }

    sort(C.begin(), C.end());
    for (int i = 0; i < N; i++){
        if (C[i] % 3 != 0){
            sum -= C[i];
            break;
        }
    }
    
    cout << sum << endl;
    cout << sum % 3 << endl;
}
```
