# 🏆 LeetCode Solutions in C++

A structured, clean collection of C++ solutions for LeetCode problems, designed for optimal time and space complexity.

---

## 📊 Progress & Stats

<p align="left">
  <a href="https://leetcode.com/"><img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=LeetCode&logoColor=black" alt="LeetCode" /></a>
  <a href="https://en.cppreference.com/"><img src="https://img.shields.io/badge/Language-C%2B%2B17-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white" alt="C++17" /></a>
</p>

| Category | Solved | Progress Bar | Percentage |
| :--- | :---: | :--- | :---: |
| 🟢 **Easy** | **5** | `████████████████████████████████` | `100%` |
| 🟡 **Medium**| **0** | `░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░` | `0%` |
| 🔴 **Hard**  | **0** | `░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░` | `0%` |
| 📦 **Total** | **5** | `████████████████████████████████` | `100%` |

---

## 📚 Problem Directory

| # | Problem | Solution | Difficulty | Category | Time Complexity | Space Complexity |
| :---: | :--- | :--- | :---: | :--- | :---: | :---: |
| **1** | [Two Sum](https://leetcode.com/problems/two-sum) | [two-sum.cpp](./1-two-sum/two-sum.cpp) | 🟢 Easy | `Array` | $O(N^2)$ | $O(1)$ |
| **9** | [Palindrome Number](https://leetcode.com/problems/palindrome-number) | [palindrome-number.cpp](./9-palindrome-number/palindrome-number.cpp) | 🟢 Easy | `Math` / `String` | $O(\log_{10} N)$ | $O(\log_{10} N)$ |
| **121** | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock) | [best-time-to-buy-and-sell-stock.cpp](./121-best-time-to-buy-and-sell-stock/best-time-to-buy-and-sell-stock.cpp) | 🟢 Easy | `Array` / `DP` | $O(N)$ | $O(1)$ |
| **217** | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate) | [contains-duplicate.cpp](./217-contains-duplicate/contains-duplicate.cpp) | 🟢 Easy | `Array` / `Sorting` | $O(N \log N)$ | $O(1)$ |
| **242** | [Valid Anagram](https://leetcode.com/problems/valid-anagram) | [valid-anagram.cpp](./242-valid-anagram/valid-anagram.cpp) | 🟢 Easy | `String` / `Sorting` | $O(N \log N)$ | $O(1)$ |

---

## 🛠️ How to Compile & Run

Every solution is written in standard C++ and can be compiled using a modern compiler (e.g., GCC 7+).

### Compile Command
Navigate to the root directory and compile a solution with optimizations:
```bash
g++ -std=c++17 -O2 -Wall -Wextra <folder-name>/<file-name>.cpp -o solution
```

**Example (Two Sum):**
```bash
g++ -std=c++17 -O2 -Wall -Wextra 1-two-sum/two-sum.cpp -o two_sum
```

### Run Command
Run the compiled executable:
```bash
./two_sum
```

---

## 🚀 Repository Guidelines

### Folder Structure
Each problem has its dedicated folder following the naming convention `<problem-id>-<problem-slug>`:
```text
.
├── 1-two-sum/
│   ├── README.md        # Problem description
│   └── two-sum.cpp      # C++ Solution source code
```

### Adding a New Solution
1. Create a new directory matching the schema above.
2. Code your C++ solution (e.g., `<problem-slug>.cpp`).
3. Add the problem statement and description inside a `README.md` within that directory.
4. Update the **Problem Directory** table above with correct links and complexity analysis.

---

## 📔 Key Learning Resources

* [C++ Reference Guide](https://en.cppreference.com/) - Comprehensive C++ Standard Library reference.
* [LeetCode Practice](https://leetcode.com/problemset/all/) - Link to the problems dashboard.
