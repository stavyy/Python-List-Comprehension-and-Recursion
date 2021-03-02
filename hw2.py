
#This is recursive method compute quaternary value

def recursion(input_value):
    if input_value==0:
        return 0
    else:
        return (input_value%4 + 10* recursion(input_value//4))

#function call recursion function and compute sum of quaternary and retuen tuple value
def base_builder(input_value):
    quaternary_value=recursion(input_value)

    return (10 ,quaternary_value)

#input the value and print tuple result
input_value = int(input("Enter the decimal value:"))
Result_Tuple = base_builder(input_value);
print(Result_Tuple);