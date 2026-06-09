# Reg-ex match (need to be solved by recursion using memoization technique)


def ismatch(s:str, p:str):
    result = False if len(p) == 0 and len(s) != 0 else True
    
    return result