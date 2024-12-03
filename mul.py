import streamlit as st
import numpy as np
import time
import concurrent.futures

# Single-threaded matrix multiplication
def single_threaded_matrix_multiplication(A, B):
    rows, cols = A.shape[0], B.shape[1]
    result = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            result[i][j] = np.dot(A[i, :], B[:, j])
    return result

# Worker function for row-wise multi-threading
def row_worker(A, B, row, result):
    result[row] = np.dot(A[row, :], B)

# Multi-threaded row-wise matrix multiplication
def multi_threaded_matrix_multiplication_row(A, B):
    rows = A.shape[0]
    result = np.zeros((rows, B.shape[1]))
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(row_worker, A, B, i, result) for i in range(rows)]
        concurrent.futures.wait(futures)
    return result

# Compare performance of single vs multi-threaded
def compare_performance(A, B):
    # Single-threaded
    start_time = time.time()
    single_result = single_threaded_matrix_multiplication(A, B)
    single_duration = (time.time() - start_time) * 1000

    # Multi-threaded (row)
    start_time = time.time()
    row_threaded_result = multi_threaded_matrix_multiplication_row(A, B)
    row_threaded_duration = (time.time() - start_time) * 1000

    return single_duration, row_threaded_duration, single_result, row_threaded_result

# Streamlit UI
st.title("Matrix Multiplication: Single vs Multi-threaded Performance")

# User choice for input mode
input_mode = st.radio("Choose Input Mode", options=["User Input", "Random Generation"], index=0)

# Slider for matrix size
matrix_size = st.slider("Select Matrix Size", 2, 100, 3)

if input_mode == "User Input":
    st.subheader("Matrix A Input")
    A_input = st.text_area(
        "Enter values for Matrix A (comma-separated rows, e.g., 1,2,3; 4,5,6)",
        value="1,2,3; 4,5,6; 7,8,9" if matrix_size == 3 else "",
    )
    A = np.array([list(map(int, row.split(','))) for row in A_input.split(';')])

    st.subheader("Matrix B Input")
    B_input = st.text_area(
        "Enter values for Matrix B (comma-separated rows, e.g., 1,2,3; 4,5,6)",
        value="1,2,3; 4,5,6; 7,8,9" if matrix_size == 3 else "",
    )
    B = np.array([list(map(int, row.split(','))) for row in B_input.split(';')])

else:
    st.write("Randomly generating matrices based on the selected size...")
    A = np.random.randint(1, 10, size=(matrix_size, matrix_size))
    B = np.random.randint(1, 10, size=(matrix_size, matrix_size))

# Display matrices
st.write("Matrix A:")
st.write(A)

st.write("Matrix B:")
st.write(B)

# Check if dimensions are valid for multiplication
if A.shape[1] != B.shape[0]:
    st.error("Matrix A's columns must equal Matrix B's rows for multiplication!")
else:
    # Run comparison when button is clicked
    if st.button("Run Comparison"):
        # Compare performance
        single_duration, row_threaded_duration, single_result, row_threaded_result = compare_performance(A, B)

        # Display results
        st.write(f"Single-threaded duration: {single_duration:.2f} ms")
        st.write(f"Row-threaded duration: {row_threaded_duration:.2f} ms")

        # Display result matrices
        st.write("Single-threaded Result Matrix:")
        st.write(single_result)

        st.write("Row-threaded Result Matrix:")
        st.write(row_threaded_result)

        # Validate results
        if np.array_equal(single_result, row_threaded_result):
            st.success("Both methods produced the same result!")
        else:
            st.error("Results from single-threaded and multi-threaded methods do not match.")
