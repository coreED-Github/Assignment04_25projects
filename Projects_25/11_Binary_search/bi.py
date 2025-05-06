import streamlit as st
import random
import time
import matplotlib.pyplot as plt
import numpy as np

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint - 1)
    else:
        return binary_search(l, target, midpoint + 1, high)

def visualize_search_process(l, target, search_type="Naive"):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(l, label="Array", color="blue", alpha=0.6)

    if search_type == "Naive":
        for i, val in enumerate(l):
            if val == target:
                ax.plot(i, val, 'ro', label="Target Found")
                break
    elif search_type == "Binary":
        low, high = 0, len(l) - 1
        while low <= high:
            mid = (low + high) // 2
            ax.plot(mid, l[mid], 'go', label="Mid Point")
            if l[mid] == target:
                ax.plot(mid, l[mid], 'ro', label="Target Found")
                break
            elif l[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

    ax.legend()
    st.pyplot(fig)

def plot_performance_graph(lengths, naive_times, binary_times):
    fig, ax = plt.subplots()
    ax.plot(lengths, naive_times, label='Naive Search', color='blue')
    ax.plot(lengths, binary_times, label='Binary Search', color='green')
    ax.set_xlabel('Array Size')
    ax.set_ylabel('Time (Seconds)')
    ax.set_title('Search Time Comparison')
    ax.legend()
    st.pyplot(fig)

def main():
    st.title("🔍 Binary Search vs Naive Search")

    length = st.slider("Select array size:", min_value=10, max_value=20000, value=1000, step=100)

    if "target_input" not in st.session_state:
        st.session_state["target_input"] = random.randint(-3 * length, 3 * length)

    target_value = st.number_input("Enter target value to search:", key="target_input")

    if st.button("Generate and Compare"):
        sorted_list = sorted(random.sample(range(-3 * length, 3 * length), length))

        start = time.time()
        for target in sorted_list:
            naive_search(sorted_list, target)
        end = time.time()
        naive_time = end - start

        start = time.time()
        for target in sorted_list:
            binary_search(sorted_list, target)
        end = time.time()
        binary_time = end - start

        st.success(f"✅ Array of size `{length}` generated and searched.")
        st.write(f"📌 **Naive Search Time:** `{naive_time:.6f}` seconds")
        st.write(f"📌 **Binary Search Time:** `{binary_time:.6f}` seconds")

        st.subheader("Visualizing Search Process")
        visualize_search_process(sorted_list, target_value, search_type="Naive")
        st.write("### Binary Search Visualization")
        visualize_search_process(sorted_list, target_value, search_type="Binary")

        st.info("🎯 Binary Search is significantly faster for large sorted arrays due to its O(log n) time complexity!")

        lengths = [100, 500, 1000, 5000, 10000]
        naive_times = []
        binary_times = []

        for length in lengths:
            sorted_list = sorted(random.sample(range(-3 * length, 3 * length), length))

            start = time.time()
            for target in sorted_list:
                naive_search(sorted_list, target)
            end = time.time()
            naive_times.append(end - start)

            start = time.time()
            for target in sorted_list:
                binary_search(sorted_list, target)
            end = time.time()
            binary_times.append(end - start)

        plot_performance_graph(lengths, naive_times, binary_times)

if __name__ == "__main__":
    main()
