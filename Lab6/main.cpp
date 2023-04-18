#include <iostream>
#include <cmath>
using namespace std;

//Task 3
double solver(int n) {
    if (n == 1) {
        return pow(-1, n+1) / n;
    }
    else {
        return solver(n-1) + pow(-1, n+1) / n;
    }
}

//Task 4
double solver() {
    int n;
    cout << "Please enter a number for n: ";
    cin >> n;
    if (n == 1) {
        return pow(-1, n+1) / n;
    }
    else {
        return solver(n-1) + pow(-1, n+1) / n;
    }
}



int main() {
    int n;
    cout << "Please enter a number for n: ";
    cin >> n;
    double solution = solver(n);
    cout << "Solution: " << solution << endl;

    double solution2 = solver();
    cout << "Solution: " << solution2 << endl;

    return 0;


}
