
def invert_string(s):
    # Caso base: si la cadena está vacía o tiene un solo carácter

    if len(s) <= 1:
        return s
    else:
        return invert_string(s[1:]) + s[0]




