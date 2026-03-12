HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, "r")
    line = file.readline()
    if len(line) == 0:
        print("No history found.")
    else:
        for line in reversed(line):
            print(line.strip())
    file.close()

def clear_history():
    file=open(HISTORY_FILE, "w")
    file.close()
    print("History cleared.")
    
def save_to_history(expression, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"{expression} = {result}\n")
        file.close()
        
def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Please enter in the format: number operator number")
        return None
    
    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])
    
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return None
    else:
        print("Invalid operator. Please use one of: +, -, *, /")
        return None
    
    if int(result) == result:
        return int(result)
    print("Result:", result)
    save_to_history(user_input, result)
    
    
def main():
    user_input = input("enter calculation (e.g., 2 + 2): or 'history' to view history, 'clear' to clear history: ").strip( )
    if user_input.lower() == "history":
        show_history()
    elif user_input.lower() == "clear":
        clear_history()
    else:
        result = calculate(user_input)
        if result is not None:
            print("Result:", result)
            save_to_history(user_input, result)   