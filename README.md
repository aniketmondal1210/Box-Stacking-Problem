# 📦 Box Stacking Problem

This project solves the **Box Stacking Problem** using **Dynamic Programming** in Python.

## 🚀 Problem Statement

Given `n` types of 3D rectangular boxes (height, width, depth), stack them to get the **maximum possible height**. You can:
- Rotate each box to get **3 orientations** 📐
- Use **multiple instances** of each box 🔁
- Only stack a box if it's **strictly smaller** in width and depth than the box below it

## 🧠 Approach

- Generate all 3 rotations for each box
- Sort all boxes by **base area** (width × depth) in **descending order**
- Use **Dynamic Programming (LIS style)** to find the tallest stack

## 📝 Example

### Input:
```python
[Box(4, 6, 7), Box(1, 2, 3), Box(4, 5, 6), Box(10, 12, 32)]
```
Output:

The maximum possible height of stack is 60

📂 Files

    main.py – Contains the complete Python implementation

🛠️ Requirements

    Python 3.x

▶️ How to Run

python main.py

📌 Time & Space Complexity

    Time: O(n²)

    Space: O(n)

📽️ Reference

Based on MIT OpenCourseWare:
🔗 http://people.csail.mit.edu/bdean/6.046/dp/

Made with ❤️ for DSA learning.
