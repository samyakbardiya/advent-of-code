#include <bits/stdc++.h>
using namespace std;

#define f(i, a, n) for (long i = a; a < n ? i < n : i > n; a < n ? ++i : --i)
#define fo(i, n) for (long i = 0; i < n; ++i)
#define foe(i, n) for (auto i : n)
#define bug(x) cout << #x << ": " << x << '\n'
#define bug2(x, y) cout << #x << ": " << x << " | " << #y << ": " << y << '\n'
#define bugArr(a, n)                                                           \
    cout << #a << ": ";                                                        \
    fo(i, n) cout << a[i] << ", ";                                             \
    cout << '\n'
#define bugVec(v)                                                              \
    cout << #v << ": ";                                                        \
    fo(i, v.size()) cout << v[i] << ", ";                                      \
    cout << '\n'

bool checkIfPart(int r, int c, int max_r, int max_c,
                 vector<vector<char>> GRID) {
    vector<char> symbols;
    vector<char> all_chars;
    for (int i = max(0, r - 1); i < min(max_r, r + 2); ++i) {
        for (int j = max(0, c - 1); j < min(max_c, c + 2); ++j) {
            char ch = GRID[i][j];
            all_chars.push_back(ch);
            if (ch != '.' && !isdigit(ch)) {
                symbols.push_back(ch);
                return true;
            }
        }
    }
    bugVec(all_chars);
    if (symbols.size() > 0) {
        bugVec(symbols);
    }

    return false;
}

int adventOfCode(vector<vector<char>> GRID) {
    int ANS_1 = 0;
    int ANS_2 = 0;
    int R = GRID.size();
    int C = GRID[0].size();

    vector<int> ans_1;
    for (int r = 0; r < R; ++r) {
        int num = 0;
        vector<int> numbers;
        bool is_part = false;

        for (int c = 0; c < C; ++c) {
            char ch = GRID[r][c];

            if (isdigit(ch)) {
                num = num * 10 + int(ch - '0');
                bug(ch);
                is_part = checkIfPart(r, c, R, C, GRID);
            } else if (num > 0) {
                numbers.push_back(num);
                if (is_part) {
                    ANS_1 += num;
                    ans_1.push_back(num);
                    is_part = false;
                }
                num = 0;
            }
        }
        if (num > 0) {
            numbers.push_back(num);
            if (is_part) {
                ANS_1 += num;
                ans_1.push_back(num);
                is_part = false;
            }
            num = 0;
        }
        bugVec(numbers);
    }
    bugVec(ans_1);

    cout << "\n   ===== PART_01: " << ANS_1 << " =====\n";
    /* cout << "\n   ===== PART_02: " << ANS_2 << " =====\n"; */

    return 0;
}

int main(int argc, char **argv) {

    for (int f = 1; f < argc; ++f) {
        cout << "\n########## " << argv[f] << " ##########\n";

        int ANS_1 = 0;
        vector<int> ans_1;

        vector<vector<char>> grid;

        ifstream infile(argv[f]);
        string line;
        while (getline(infile, line)) {
            vector<char> ch_line;
            for (char c : line)
                ch_line.push_back(c);
            grid.push_back(ch_line);

            cout << line << endl;
        }
        cout << endl;

        adventOfCode(grid);

        /* int R = grid.size(); */
        /* int C = grid[0].size(); */
        /* for (int r = 0; r < R; ++r) { */
        /*     vector<int> numbers; */
        /*     int n = 0; */
        /*     bool is_part = false; */
        /*     for (int c = 0; c < C; ++c) { */
        /*         char ch = grid[r][c]; */
        /*         if (isdigit(ch)) { */
        /*             n = n * 10 + (ch - '0'); */
        /*             for (int rr = max(0, r - 1); rr < min(r + 1, R);
         * ++rr) {
         */
        /*                 cout << n << " -> "; */
        /*                 for (int cc = max(0, c - 1); cc < min(c + 1, C);
         * ++cc) { */
        /*                     if (rr == r && cc == c) */
        /*                         continue; */
        /*                     char _ch = grid[rr][cc]; */
        /*                     printf("(%c)[%d,%d] ", _ch, rr, cc); */
        /*                     if (_ch != '.' && !isdigit(_ch)) { */
        /*                         is_part = true; */
        /*                     } */
        /*                 } */
        /*                 cout << endl; */
        /*             } */
        /*         } else { */
        /*             if (n > 0) { */
        /*                 numbers.push_back(n); */
        /*                 if (is_part) { */
        /*                     ANS_1 += n; */
        /*                     ans_1.push_back(n); */
        /*                     is_part = false; */
        /*                 } */
        /*                 n = 0; */
        /*             } */
        /*         } */
        /*     } */
        /*     if (n > 0) { */
        /*         numbers.push_back(n); */
        /*         if (is_part) { */
        /*             ANS_1 += n; */
        /*             ans_1.push_back(n); */
        /*         } */
        /*     } */
        /*     bugVec(numbers); */
        /* } */
        /* bugVec(ans_1); */
        return 0;
    }
}
