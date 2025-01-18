#include <string>
using namespace std;

class HeartRates {
public:
  HeartRates(string, string, int, int, int);
  void setFirstName(string);
  void setLastName(string);
  void setBirthMonth(int);
  void setBirthDay(int);
  void setBirthYear(int);
  string getFirstName();
  string getLastName();
  int getBirthMonth();
  int getBirthDay();
  int getBirthYear();
  int getAge();
  int getMaximumHeartRate(int);
  string getTargetHeartRate(int);

private:
  string firstName;
  string lastName;
  int birthMonth;
  int birthDay;
  int birthYear;
};
