# Matrix Multiplication: Single vs Multi-threaded Performance

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

## About the Project

This project showcases the comparison between **single-threaded** and **multi-threaded matrix multiplication** techniques. It provides insights into the performance improvements achieved by leveraging concurrency in Python using `concurrent.futures`. The project also includes an interactive web-based UI built with **Streamlit** to visualize the computation and compare results.

---

## Features

- **Single-threaded Matrix Multiplication:** Sequential computation for multiplying two matrices.
- **Multi-threaded Matrix Multiplication:** Concurrent computation using row-wise threading.
- **Performance Comparison:** Measure and compare execution time for both methods.
- **Interactive UI:** Use Streamlit to input matrices or generate random matrices and observe results.
- **Error Handling:** Validates matrix dimensions for compatibility.
- **Visualization:** Display matrices and results with formatted output.

---

## Technologies Used

- **Python 3.10+**
- **Streamlit**
- **NumPy**
- **Concurrent Futures**

---

## Getting Started

### Prerequisites
Make sure you have Python installed. Use the following commands to install the dependencies:
```bash
pip install streamlit numpy
```
### Installation
Clone Repository
```bash
git clone https://github.com/Megamind0407/matrix_mul.git
```
### Usage
```bash
streamlit run mul.py
```
## Sample Input

### Matrix A 
```
1  2  3
4  5  6
7  8  9
```
### Matrix B
```
9  8  7
6  5  4
3  2  1
```
## Contribution
Contributions are welcome! Follow these steps:

**Fork the repository**

**Create a feature branch: `git checkout -b feature-name`**

**Commit changes: `git commit -m "Add a new feature"`**

**Push to the branch: `git push origin feature-name`**

**Submit a pull request.**
