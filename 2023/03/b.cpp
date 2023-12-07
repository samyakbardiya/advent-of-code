#include <bits/stdc++.h>
#include <cctype>
#include <utility>
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

void checkNearby(int r, int c, int max_r, int max_c,
                 vector<vector<char>> grid) {
    printf("[%d,%d] %c ", r, c, grid[r][c]);

    vector<char> nearby_chars;
    vector<pair<int, int>> nearby_coords;
    for (int i = max(0, r - 1); i < min(max_r, r + 2); ++i) {
        for (int j = max(0, c - 1); j < min(max_c, c + 2); ++j) {
            if (i == r && j == c)
                continue;
            nearby_chars.push_back(grid[i][j]);
            nearby_coords.push_back(make_pair(i, j));
        }
    }

    for (auto _ch : nearby_chars)
        cout << _ch;
    cout << " | ";
    for (auto _coord : nearby_coords)
        printf("[%d,%d] ", _coord.first, _coord.second);
    cout << '\n';

    vector<int> nearby_numbers;
    for (auto coord : nearby_coords) {
        char ch = grid[coord.first][coord.second];
        deque<int> digits;
        if (isdigit(ch)) {
            digits = {int(ch - '0')};

            // LEFT
            int left = coord.second - 1;
            while (left >= 0 && isdigit(grid[coord.first][left])) {
                pair curr_coord = make_pair(coord.first, left);
                auto pos = find(nearby_coords.begin(), nearby_coords.end(),
                                curr_coord);
                if (pos != nearby_coords.end())
                    nearby_coords.erase(pos);
                digits.push_front(
                    int(grid[curr_coord.first][curr_coord.second]));
                left--;
            }
        }
    }
}

void adventOfCode(vector<vector<char>> grid) {
    int ANS_1 = 0;
    int ANS_2 = 0;

    int max_r = grid.size();
    int max_c = grid[0].size();

    for (int r = 0; r < max_r; ++r) {
        for (int c = 0; c < max_c; ++c) {
            char ch = grid[r][c];
            if (ch != '.' && !isdigit(ch)) {
                checkNearby(r, c, max_r, max_c, grid);
            }
        }
    }

    cout << "\n   ===== PART_01: " << ANS_1 << " =====\n";
    /* cout << "\n   ===== PART_02: " << ANS_2 << " =====\n"; */
}

int main(int argc, char **argv) {
    for (int f = 1; f < argc; ++f) {
        cout << "\n########## " << argv[f] << " ##########\n";

        vector<vector<char>> grid;

        ifstream infile(argv[f]);
        string line;
        while (getline(infile, line)) {
            vector<char> ch_line;
            for (char c : line)
                ch_line.push_back(c);
            grid.push_back(ch_line);
        }

        for (vector<char> a : grid) {
            for (char b : a) {
                cout << b;
            }
            cout << '\n';
        }
        cout << '\n';

        adventOfCode(grid);
    }
    cout << '\n';
    return 0;
}
