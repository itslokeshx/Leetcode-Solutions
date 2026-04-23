# LeetCode Solutions in C++

This repository collects my C++ solutions to LeetCode problems, organized by problem ID and title.

## Repository Layout

Each problem lives in its own folder and usually contains:

- a `README.md` with the original LeetCode problem statement
- a `.cpp` file with the solution

## Current Problems

| Problem                                                                 | Solution                                                                                                       |
| ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| [Two Sum](1-two-sum/)                                                   | [two-sum.cpp](1-two-sum/two-sum.cpp)                                                                           |
| [Best Time to Buy and Sell Stock](121-best-time-to-buy-and-sell-stock/) | [best-time-to-buy-and-sell-stock.cpp](121-best-time-to-buy-and-sell-stock/best-time-to-buy-and-sell-stock.cpp) |
| [Contains Duplicate](217-contains-duplicate/)                           | [contains-duplicate.cpp](217-contains-duplicate/contains-duplicate.cpp)                                        |
| [Palindrome Number](9-palindrome-number/)                               | [palindrome-number.cpp](9-palindrome-number/palindrome-number.cpp)                                             |

## How to Run a Solution

Compile a solution with any modern C++ compiler. For example:

```bash
g++ -std=c++17 -O2 -Wall -Wextra 1-two-sum/two-sum.cpp -o two-sum
./two-sum
```

## Adding a New Problem

1. Create a new folder named with the LeetCode problem number and title.
2. Add the solution source file inside that folder.
3. Optionally include a `README.md` with the problem statement or notes.
4. Update this README so the new problem appears in the table above.

## Notes

- Folder names follow the pattern `<problem-number>-<problem-title>`.
- Solutions are written in C++ and kept close to the original problem name for easy lookup.
