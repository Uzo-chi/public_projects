#include "HeartRates.h"
#include <iostream>
using namespace std;

int main() {
  string fname, lname;
  int dob, mob, yob;
  cout << "-------Target Heart Rate Calculator-------" << "\n" << endl;
  cout << "Your first name: ";
  getline(cin, fname);
  cout << "Your last name: ";
  getline(cin, lname);
  cout << "Your day of birth: ";
  cin >> dob;
  cout << "Your month of birth: ";
  cin >> mob;
  cout << "Your year of birth: ";
  cin >> yob;

  HeartRates user1(fname, lname, mob, dob, yob);
  int userAge = user1.getAge();
  int maxHeartRate = user1.getMaximumHeartRate(userAge);
  string targetHeartRate = user1.getTargetHeartRate(maxHeartRate);

  // display user info
  cout << "\nName: " << user1.getLastName() << " " << user1.getFirstName() << "\n"
       << "Date of birth: " << user1.getBirthMonth() << "/"
       << user1.getBirthDay() << "/" << user1.getBirthYear() << "\n"
       << "Age: " << userAge << " years" << "\n"
       << "Maximum heart rate: " << maxHeartRate << " beats/min\n"
       << "Target heart rate: " << targetHeartRate << " beats/min" << endl;
}
