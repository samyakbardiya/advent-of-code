#include <bits/stdc++.h>
using namespace std;

#define bug(x) cout << #x << "=" << x << '\n'

int main() {
  int ans = 0;

  while (true) {

    string str;
    cin >> str;

    int first_digit = -1;
    for (int i = 0; first_digit == -1 && i < str.length(); ++i) {
      char c = str[i];
      if (isdigit(c)) {
        int digit = int(c - '0');
        first_digit = digit;
      }
    }

    int last_digit = -1;
    for (int i = str.length() - 1; last_digit == -1 && i >= 0; --i) {
      char c = str[i];
      if (isdigit(c)) {
        int digit = int(c - '0');
        last_digit = digit;
      }
    }

    if (first_digit == -1 && last_digit == -1)
      break;

    int num = first_digit * 10 + last_digit;

    ans += num;
  }
  bug(ans);
  return ans;
}
