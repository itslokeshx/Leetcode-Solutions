#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct student {
    int rollNo;
    string name;
    string age;
    int marks;
};
int student_no=0;
void addStudent(){
cout << "add student" << "\n";
vector <student> newStudent;
};
void viewStudents(){
 cout << "View Students";
};
void searchStudent(){
    cout << "Search Student";
};
void updateStudent(){
{ cout << "update Student";}
};
void deleteStudent(){
{ cout << "Delete Student";}
};
void statistics(){
  { cout << "Statistics";}
};
void gradeReport(){
  { cout << "Grade Report";}
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

    addStudent();
       return 0;
    break;
      case 2 :
    viewStudents();
       return 0;
    break;
      case 3 :
    searchStudent();
       return 0;
    break;
      case 4 :
    updateStudent();
       return 0;
    break;
      case 5 :
    deleteStudent();
       return 0;
    break;
      case 6 :
     statistics();
        return 0;
    break;
      case 7 :
     gradeReport();
     
    break;
      case 8 :
    { cout << "Exit";};
    break;
    default:
     cout << "Invalid choice";
  }

}