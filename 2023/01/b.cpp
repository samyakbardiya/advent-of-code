#include <bits/stdc++.h>
using namespace std;

#define bug(x) cout << #x << "=" << x << '\n'

int get_number(string line) {
  int first_digit = 0;
  for (int i = 0; i < line.length(); ++i) {
    char c = line[i];
    if (isdigit(c)) {
      first_digit = int(c - '0');
      break;
    }
  }

  int last_digit = 0;
  for (int i = line.length() - 1; i >= 0; --i) {
    char c = line[i];
    if (isdigit(c)) {
      last_digit = int(c - '0');
      break;
    }
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
