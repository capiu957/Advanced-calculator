import streamlit as st
import math

def factorial(n):
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def taylor_sine(x, terms=10):
    
    sine = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
        sine += term
    return sine

def taylor_cosine(x, terms=10):
    
    cosine = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
        cosine += term
    return cosine

def taylor_tangent(x, terms=10):
    
    cosine = taylor_cosine(x, terms)
    if cosine == 0:
        return 'Error: tangent undefined at this input!'
    return taylor_sine(x, terms) / cosine

def taylor_exp(x, terms=10):

    exp = 0
    for n in range(terms):
        term = (x ** n) / factorial(n)
        exp += term
    return exp

def taylor_ln(x, terms=10):
    
    if x <= 0:
        return 'Error: logarithm undefined for non-positive values!'
    if x > 2:
        return 'Error: input out of approximation range!'

    y = x - 1
    ln = 0
    for n in range(1, terms + 1):
        term = ((-1) ** (n + 1)) * (y ** n) / n
        ln += term
    return ln

def calculate(num1, num2, operation):
    try:
        if operation in ['Sine', 'Cosine', 'Tangent', 'Exp', 'Ln']:
            
            num1 = float(num1)
            if operation == 'Sine':
                return taylor_sine(num1)
            elif operation == 'Cosine':
                return taylor_cosine(num1)
            elif operation == 'Tangent':
                return taylor_tangent(num1)
            elif operation == 'Exp':
                return taylor_exp(num1)
            elif operation == 'Ln':
                return taylor_ln(num1)
        else:
            
            num1 = float(num1)
            num2 = float(num2)
            if operation == 'Sum':
                return num1 + num2
            elif operation == 'Sub':
                return num1 - num2
            elif operation == 'Mult':
                return num1 * num2
            elif operation == 'Div':
                if num2 == 0:
                    return 'Error: division by zero!'
                return num1 / num2
    except ValueError:
        return 'Error: invalid input! Please insert numbers.'


st.title('Advanced Calculator')
st.write('Choose two numbers (if applicable) and the operation you want to do.')


num1 = st.text_input('Type in the first number')
num2 = st.text_input('Type in the second number (leave blank for single-input operations)')
operation = st.selectbox('Choose the operation:', ['Sum', 'Sub', 'Mult', 'Div', 'Sine', 'Cosine', 'Tangent', 'Exp', 'Ln'])


if st.button('Calculate'):
    if operation in ['Sine', 'Cosine', 'Tangent', 'Exp', 'Ln']:
    
        result = calculate(num1, None, operation)
    else:
        result = calculate(num1, num2, operation)

    st.write(f"Result: {result}")
