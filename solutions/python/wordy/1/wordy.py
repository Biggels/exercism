import re

VALID_OPERATIONS = ["plus", "minus", "multipliedby", "dividedby"]

def answer(question):

    chunks = question.replace("What is ", "").replace("?", "").replace("multiplied by", "multipliedby").replace("divided by", "dividedby").split(" ")


    print(chunks)

    try:
        result = int(chunks[0])
    except Exception:
        raise ValueError("syntax error")

    if len(chunks) % 2 == 0:
        chunks.append(None)

    for i in range(1, len(chunks), 2):
        operation, operand = chunks[i], chunks[i+1]

        if not operation.isalpha():
            raise ValueError("syntax error")

        # this is redundant, because the match case _ below would catch it,
        # but we have to do this first so that we specifically raise unknown operation
        # for "cubed", because otherwise we would hit a "syntax error" when we tried to coerce operand to int
        # since cubed is followed by None
        if operation not in VALID_OPERATIONS:
            raise ValueError("unknown operation")

        try:
            operand = int(operand)
        except Exception:
            raise ValueError("syntax error")
            
        match operation:
            case "plus":
                result += operand
            case "minus":
                result -= operand
            case "multipliedby":
                result *= operand
            case "dividedby":
                result /= operand
            case _:
                raise ValueError("unknown operation")       
    
    return result

    

    