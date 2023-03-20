print("choose a sign:'+','-','*','/','sqrt','^' ")
sign = str(input())
number1 = int(input())
number2 = int(input())
match sign:
    case "+":
        print(number1 + number2)
    case "-":
        print(number1 - number2)
    case "*":
        print(number1 * number2)
    case "/":
        print(number1 * number2)
    case "^":
        print(number1 ** number2)
    case "sqrt":
        print(number1 ** (1/number2))
