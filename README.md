# Push_swap Performance Analysis

> 🇪🇸 **Español**: Existe una versión en español de este documento disponible en [README_es.md](README_es.md).

This repository contains a set of Python scripts designed to test, analyze, and measure the performance of the **push_swap** project from 42.

The scripts automate random number generation, execution of your program, and validation with the `checker`, providing detailed statistics on the move count.

## 📋 Requirements

Ensure you have the following files in the same directory where you execute the scripts:

1. **`push_swap`**: Your compiled executable.
2. **`checker_linux`**: The checker binary provided by 42 (make sure it has execution permissions: `chmod +x checker_linux`).
3. **Python 3**: To run the scripts.

> **Tip 💡:** All scripts include shebangs (`#!/usr/bin/env python3`). If you give them execution permissions with `chmod +x *.py`, you can run them directly (e.g., `./performance_analysis.py`) without typing `python3`.

> **Note:** The scripts are configured to use `./checker_linux`. If you wish to use the MacOS checker, you will need to modify the corresponding line in the `.py` files.

---

## 🛠️ Available Scripts

### 1. 📊 `performance_analysis.py` (Recommended)
This is the main script for obtaining detailed performance metrics. It calculates the minimum, maximum, average, and standard deviation of moves.

**Default usage (runs 100 tests of 100 numbers and 100 tests of 500 numbers):**
```bash
python3 performance_analysis.py
```

**Custom usage:**
You can specify the amount of numbers and the number of iterations:
```bash
# Syntax: python3 performance_analysis.py [NUMBER_COUNT] [ITERATIONS]

# Example: Analyze 100 numbers with 500 tests
python3 performance_analysis.py 100 500
```
*If the program detects failures (KO), it will save the failed cases in `ko_cases.txt`.*

### 2. 📈 `visual_analysis.py` (Visual & Graph)
Runs multiple tests increasing the stack size and generates a graph (`performance_graph.png`) to verify the complexity of your algorithm.
- **Requirements**: Needs `matplotlib` (`pip install matplotlib`).
- **Function**: Running it creates a graph with average, min, and max moves.

```bash
# Default (10 to 500 elements, step 50)
python3 visual_analysis.py

# Custom (e.g., specific range and more samples)
python3 visual_analysis.py --min 5 --max 500 --step 50 --samples 20
```

### 3. 🧪 `fuzz_test.py`
Performs a basic and quick check.
- Runs 20 global iterations.
- In each iteration, it tests: 100 numbers, 500 numbers, and a random size (6-100).
- It stops immediately if an error is found.

```bash
python3 fuzz_test.py
```

### 4. 🌀 `fuzz_test_v2.py`
Focuses on intensive testing of **small cases** and random cases.
- Intensive tests: Sizes from 6 to 20 (50 tests per size).
- Random tests: 100 tests with varied sizes (6-100).

```bash
python3 fuzz_test_v2.py
```

### 5. 📉 `fuzz_test_v3.py`
Tests **special cases** and extremes.
- Reverse sorted lists (sizes 6 to 100).
- "Almost sorted" lists (only 2 elements swapped).

```bash
python3 fuzz_test_v3.py
```

---

## 🚀 How to Start

1. Compile your `push_swap` project:
   ```bash
   make
   ```
2. Make sure you have `checker_linux` in the root directory.
3. Run the performance analysis:
   ```bash
   python3 performance_analysis.py
   ```

## 📈 Metrics Explained

The analysis script will give you output like this:
- **Min Moves**: The best execution (fewest moves).
- **Max Moves**: The worst execution. Important to know if you pass the evaluation limits.
- **Mean (Avg)**: The average number of moves.
- **Std Dev**: Standard deviation (how much your results vary; ideally it should be low).
- **Runs > Limit**: Percentage of tests that exceed the acceptable limit (700 for 100 numbers, 5500 for 500).

---

Good luck with your evaluation! 🐬

---
## 🤝 Contributions (Reporting Issues)
Contributions are highly welcome and are crucial for improving the quality of this test suite!
If you encounter any issue, please **open an issue** in this repository.
---
### How to Contribute
1.  **Report an Issue:** Open a new *Issues* tab on GitHub and describe the error you found, including the **exact test case** that is failing or missing.
2.  **Submit a Pull Request (Optional):** If you have created a new test to fix the problem, you can directly submit a *Pull Request* for us to review and integrate.
**Your collaboration ensures that this test suite is as robust and complete as possible for the entire community.**

---

## 📜 License

This project is licensed under a **non-commercial educational use license**. 

**Key Points:**
- ✅ Educational use, study, and personal modifications are allowed
- ✅ You can fork this repository for learning purposes
- ❌ Commercial use or monetization is prohibited
- ❌ Redistribution as part of a commercial product is not allowed

For full details, please see the [LICENSE](LICENSE) file in the repository root.

If you need permission for commercial use, please contact the author at: **05yaqi.liu@gmail.com**