#include <bits/stdc++.h>
using namespace std;

#define fo(i, n) for (long i = 0; i < n; ++i)
#define bug(x) cout << #x << ": " << x << '\n'
#define bug2(x, y) cout << #x << "=" << x << "|" << #y << "=" << y << '\n'
#define bug3(x, y, z)                                                          \
  cout << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": "   \
       << z << "\n"
#define bugVec(v)                                                              \
  cout << #v << ": ";                                                          \
  fo(i, v.size()) cout << v[i] << ", ";                                        \
  cout << '\n'

vector<string> NUMBER_NAMES{"zero", "one", "two",   "three", "four",
                            "five", "six", "seven", "eight", "nine"};

int get_number(string input) {
  int first_digit = -1;
  for (int i = 0; i < input.length(); ++i) {
    if (first_digit != -1)
      break;

    char c = input[i];
    if (isdigit(c))
      first_digit = int(c - '0');

    for (int n = 0; n < NUMBER_NAMES.size(); ++n)
      if (input.substr(0, i).find(NUMBER_NAMES[n]) != string::npos)
        first_digit = n;
  }

  int last_digit = -1;
  for (int i = input.length() - 1; i >= 0; --i) {
    if (last_digit != -1)
      break;

    char c = input[i];
    if (isdigit(c))
      last_digit = int(c - '0');

    for (int n = 0; n < NUMBER_NAMES.size(); ++n)
      if (input.substr(i).find(NUMBER_NAMES[n]) != string::npos)
        last_digit = n;
  }

  int number = first_digit * 10 + last_digit;
  return number;
}

int main(int argc, char **argv) {
  for (int f = 1; f < argc; ++f) {
    cout << "\n===== " << argv[f] << " =====\n";

    int ans = 0;

    ifstream infile(argv[f]);

    string line;
    while (getline(infile, line)) {
      int number = get_number(line);
      ans += number;
    }

    bug(ans);
  }

  return 0;
}
