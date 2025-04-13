import streamlit as st
import matplotlib.pyplot as plt
import random

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    steps = []
    while low <= high:
        mid = (low + high) // 2
        steps.append((low, high, mid)) 
        if arr[mid] == target:
            return mid, steps 
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps 

def plot_array(arr, steps, target):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(range(len(arr)), arr, color="lightblue", label="Array Elements")

    for step in steps:
        low, high, mid = step
        ax.bar(mid, arr[mid], color="orange", label="Mid")
        if arr[mid] == target:
            ax.bar(mid, arr[mid], color="green", label="Target Found")
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_title('Binary Search Visualization')
    ax.legend()
    
    st.pyplot(fig)

def main():
    st.title('Enhanced Binary Search Visualization')

    arr_input = st.text_input("Enter a sorted list of numbers (comma separated):")
    target_input = st.number_input("Enter the target value:", step=1)
    
    if arr_input:

        arr = list(map(int, arr_input.split(',')))
        
        if len(arr) > 0:

            result, steps = binary_search(arr, target_input)
  
            if result != -1:
                st.success(f"Target found at index {result}")
            else:
                st.error("Target not found in the array")
 
            plot_array(arr, steps, target_input)
            
        else:
            st.error("Please enter a valid sorted list of numbers.")

    #Generate Random Array
    if st.button('Generate Random Array'):
        random_array = sorted(random.sample(range(1, 100), 10))
        st.write(f"Generated Array: {random_array}")
        
        #target for this array
        target_input = st.number_input("Enter target for the random array:", step=1)
        result, steps = binary_search(random_array, target_input)
        
        if result != -1:
            st.success(f"Target found at index {result}")
        else:
            st.error("Target not found in the array")
        
        #search process
        plot_array(random_array, steps, target_input)

if __name__ == "__main__":
    main()