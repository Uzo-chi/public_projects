#include "HeartRates.h"
#include <iostream>
#include <string>
using namespace std;

HeartRates::HeartRates(string fname, string lname, int month, int day,
                       int year) {
  setFirstName(fname);
  setLastName(lname);
  setBirthMonth(month);
  setBirthDay(day);
  setBirthYear(year);
}

void HeartRates::setFirstName(string fname) { firstName = fname; }

void HeartRates::setLastName(string lname) { lastName = lname; }

void HeartRates::setBirthMonth(int month) {
  if (month > 0 && month <= 12)
    birthMonth = month;
  else {
    cout << "Invalid month!\nResetting month to 1..." << endl;
    birthMonth = 1;
  }
}

void HeartRates::setBirthDay(int day) {
  if (day > 0 && day <= 31)
    birthDay = day;
  else {
    cout << "Invalid day!\nResetting day to 1..." << endl;
    birthDay = 1;
  }
}

void HeartRates::setBirthYear(int year) { birthYear = year; }

string HeartRates::getFirstName() { return firstName; }

string HeartRates::getLastName() { return lastName; }

int HeartRates::getBirthMonth() { return birthMonth; }

int HeartRates::getBirthDay() { return birthDay; }

int HeartRates::getBirthYear() { return birthYear; }

int HeartRates::getAge() {
  int day, month, year, age;

  cout << "Enter present day: ";
  cin >> day;
  cout << "Enter present month(in numbers): ";
  cin >> month;

  if (month < 1 || month > 12) {
    cout << "Invalid month entered! Setting month to 1..." << endl;
    month = 1;
  }

  cout << "Enter present year: ";
  cin >> year;

  if (month < birthMonth) {
    age = (year - birthYear) - 1;
  } else if (month == birthMonth) {
    if (day >= birthDay)
      age = year - birthYear;
    else
      age = (year - birthYear) - 1;
  } else if (month > birthMonth) {
    age = year - birthYear;
  }

  return age;
}

int HeartRates::getMaximumHeartRate(int age) {
  int maxHeartRate = 220 - age;
  return maxHeartRate;
}

string HeartRates::getTargetHeartRate(int heartrate) {
  int lowerLimit, upperLimit;
  lowerLimit = heartrate * 0.5;
  upperLimit = heartrate * 0.85;

  string targetHeartRate = to_string(lowerLimit) + "-" + to_string(upperLimit);

  return targetHeartRate;
}
