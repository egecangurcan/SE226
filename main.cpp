#include <iostream>
using namespace std;
int main() {

    string name;
    cout << "What is your name?" << endl;
    cin >> name;
    cout << "Hello " << name << "." << endl;

    string studnetID;
    cout << "What is your Student ID?" << endl;
    cin >> studnetID;
    cout << "Your ID is:" << studnetID << "." << endl;



    int var1, var2, sum, diff,prod;
    cout <<"Enter Your First Value: " << endl;
    cin >> var1;
    cout <<"Enter Your Second Value: " << endl;
    cin >> var2;

    sum = var1 + var2;
    diff = abs(var2 - var1);
    prod = var1 * var2;

    cout << "First Value Is: " << var1 << endl;
    cout << "Second Value IS: " << var2 << endl;
    cout << "Sum :" << sum << endl;
    cout << "Diff :" << diff << endl;
    cout << "Prod :" << prod << endl;



    string studentName;
    int labGrade;
    int midtermGrade;
    int finalGrade;
    int lastScore;

    cout << "Enter the Name of the Student: " << endl;
    cin >> studentName;
    cout << "Enter the Lab Grade of This Student: " << endl;
    cin >> labGrade;
    cout << "Enter the Midterm Grade of This Student: " << endl;
    cin >> midtermGrade;
    cout << "Enter the Final Grade of This Student: " << endl;
    cin >> finalGrade;
    lastScore = labGrade*0.25 + midtermGrade*0.35 + finalGrade*0.4;

    cout << "Name: " << studentName << endl;
    cout << "Lab Grade: " << labGrade << endl;
    cout << "Midterm Grade: " << midtermGrade << endl;
    cout << "Final Grade: " << finalGrade << endl;
    cout << "Last Score: " << lastScore << endl;



}
