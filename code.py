history_file = "history.txt"

def show_history():
    file = open(history_file,"r")
    line = file.readlines()
    if len(line) ==0:
        print("no history")
    else:
        for line in reversed(line):
            print(line.strip())
    file.close()


def clear_history():
    file = open(history_file , "w")
    file.close()
    print("histry cleared")

def save_to_history(equation , result):
    file = open(history_file , "a")
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("invaid input \n use format number operator number ")

    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
            result = num1 - num2 
    elif op == "*":
            result = num1 * num2
    elif op == "/":
            if num2 == 0:
                 print("cant divide by 0")
                 return
            result = num1 / num2

    else:
         print("invalid operator")
         return

    if int(result) == result :
         result = int(result)
    print("result " , result)
    save_to_history(user_input,result) 

def main ():
    print("Simple Calculator (type history , clear or exit )")
    while True :
        user_input = input("enter calculation ")
        if user_input == "exit":
            print("good byeeee")
            break
        elif user_input == "history" :
                show_history()
        elif user_input == "clear" :
                clear_history()
        else :
            calculate(user_input)

main()