# Reg-ex match


def ismatch(s:str, p:str):
    result = False if len(p) == 0 and len(s) != 0 else True
    
    return result