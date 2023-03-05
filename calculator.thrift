# This IDL file defines a Thrift service named "Calculator" with four methods: add, subtract, multiply, and divide. 
# The methods take two arguments of type i32 or double, and return an i32 or double value. The divide method also 
# throws an exception of type string if the second argument is zero.

namespace tutorial
service Calculator {
    i32 add(1: i32 num1, 2: i32 num2),
    i32 subtract(1: i32 num1, 2: i32 num2),
    i32 multiply(1: i32 num1, 2: i32 num2),
    double divide(1: double num1, 2: double num2) throws (1: string message)
}



# run this command: thrift --gen py calculator.thrift
# 3 files will be generated
# The generated Python files for the Calculator service:
# tutorial/Calculator.py
# tutorial/constants.py
# tutorial/ttypes.py
