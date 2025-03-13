#type:ignore
import streamlit as st

st.set_page_config(page_title="Simple Calculator", page_icon=":1234:")
st.title("Simple Calculator")

def main():
    st.write("Enter two numbers and select an operation to perform.")

    col1, col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("Enter the first number", value=0.0, step=1.0)

    with col2:
        num2 = st.number_input("Enter the second number", value=0.0, step=1.0)
    
    operation = st.selectbox("Select an operation", ["Addition ➕", "Subtraction ➖", "Multiplication ✖️", "Division ➗"])
    
    if st.button("Calculate"):
        try:
            if operation == "Addition ➕":
                result = num1 + num2
                symbol = "➕"
            elif operation == "Subtraction ➖":
                result = num1 - num2
                symbol = "➖"
            elif operation == "Multiplication ✖️":
                result = num1 * num2
                symbol = "✖️"
            elif operation == "Division ➗":
                if num2 == 0:
                    st.error("Division by zero is not allowed ❌")
                    return
                result = num1 / num2
                symbol = "➗"
            st.success(f"{num1} {symbol} {num2} = {result}")
            st.balloons()
        except Exception as e:
            st.error("An error occurred. Please try again.")
            st.error(e)


    
    st.write("---")
    st.write("Made with ❤️ by [Jam](https://github.com/Jamila654/ramadan-coding-nights-q3)")
        

if __name__ == "__main__":
 main()