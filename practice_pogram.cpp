#include <iostream>
using namespace std;

struct student {
    int rollNo;
    string name;
    string age;
    int marks;
};

int main(){
    int choice;
   cout << "===== STUDENT MANAGEMENT SYSTEM ===== " << "\n";
   cout << "1. Add Student" << "\n";
   cout << "2. View Students" << "\n";
   cout << "3. Search Student " << "\n";
   cout << "4. Update Student" << "\n";
   cout << "5. Delete Student " << "\n";
   cout << "6. Statistics" << "\n";
   cout << "7. Grade Report" << "\n";
   cout << "8. Exit" << "\n";
  cout << "Enter the number to operate the list the options" << "\n";
  cin >> choice;
 
  switch (choice){
    case 1 :
    { cout << "add student";};
    break;
      case 2 :
    { cout << "View Students";};
    break;
      case 3 :
    { cout << "Search Student";};
    break;
      case 4 :
    { cout << "update Student";};
    break;
      case 5 :
    { cout << "Delete Student";};
    break;
      case 6 :
    { cout << "Statistics";};
    break;
      case 7 :
    { cout << "Grade Report";};
    break;
      case 8 :
    { cout << "Exit";};
    break;
    default:
     cout << "Invalid choice";
  }






}