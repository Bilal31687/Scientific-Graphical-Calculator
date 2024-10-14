import streamlit as st
import numpy as np
import matplotlib.pyplot as plt 

# Streamlit UI
st.title("Scientific Graphical Calculator")

# Operation selection
st.header("Select a Mathematical Operation")
operation = st.selectbox(
    "Choose a function:", 
    ("Addition", "Subtraction", "Multiplication", "Division", 
     "Sine", "Cosine", "Tangent", "Exponential", "Logarithm")
)

# Number inputs (for basic operations)
num1 = st.number_input("Enter first number", value=0.0, step=0.1, format="%.2f")
num2 = st.number_input("Enter second number (if applicable)", value=0.0, step=0.1, format="%.2f")

# Calculate result based on the selected operation
if operation in ["Addition", "Subtraction", "Multiplication", "Division"]:
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        result = num1 / num2 if num2 != 0 else "Error: Division by Zero!"
    
    st.success(f"The result of {operation.lower()} is: {result}")

# Graphical operations (sine, cosine, tangent, exponential, logarithm)
else:
    # Generate an array of x-values
    x = np.linspace(-10, 10, 100)

    if operation == "Sine":
        y = np.sin(x)
    elif operation == "Cosine":
        y = np.cos(x)
    elif operation == "Tangent":
        y = np.tan(x)
    elif operation == "Exponential":
        y = np.exp(x)
    elif operation == "Logarithm":
        y = np.log(x[x > 0])  # Only positive x-values for logarithm

    # Plotting the function
    fig, ax = plt.subplots()
    ax.plot(x, y, label=f"{operation} function")
    ax.legend()
    ax.grid(True)
    ax.set_xlabel("x")
    ax.set_ylabel(f"{operation}(x)")

    # Display the plot in Streamlit
    st.pyplot(fig)
