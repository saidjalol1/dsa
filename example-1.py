# Recutrsion and Memoization (progress : done - 100%)

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# print(fib(5))


def fac(n:int):
    if n <= 1:
        return 1
    return n * fac(n - 1)

# print(fac(15))


def reverse_string(s:str):
    if len(s) == 0:
        return s
    
    return s[-1] + reverse_string(s[:-1])

# print(reverse_string("Salom!"))




def is_palindrom(s):
    # Examples :
    # radar
    # 0 va 1 ->  r == r  ->  radar
    # 0 va 1 ->  a == a -> ada
    # d -> return 

    # amma
    # 0 va 1 -> a == a -> amma
    # 0 va 1 -> m == m -> mm
    
    if len(s) <= 1:
        return True
    
    if s[0] == s[-1]:
        return is_palindrom(s[1:-1])
    
# print(is_palindrom("amma"))


def nested_loop_search(_list, key):
    if len(_list) == 0:
        return False
    
    for item in _list:
        if item == key:
            return True
        elif isinstance(item, list):
            if nested_loop_search(item, key):
                return True
            
    return False
    

data = [1, [2, 3, [4, 5]], 7]
print(nested_loop_search(data, 7))
            

file_system = [
    "rasmlar", 
    ["ish_fayllari", ["hisobot.pdf", "shartnoma.docx"]], 
    ["shaxsiy", ["foto1.jpg", "foto2.jpg", [[[[[[[[[[[[[[[[[[[[["rasm"]]]]]]]]]]]]], "rasmlar-again"]]]]]]]]]],
    "yozuvlar.txt"
]

def find_file(file_system, file_name):
    if len(file_system) == 0 or len(file_name) == 0:
        return False
    
    for item in file_system:
        print(f"Solishtirilmoqda: '{item}' va '{file_name}'")
        if item == file_name:
            return True
        elif isinstance(item, list):
            if find_file(item, file_name):
                return True
    
    return False

print(find_file(file_system, "rasmlar-again"))


# Memoization recursion

def find_file_(file_system, file_name , memo):
    if memo is None:
        memo = {}
    
    if id(file_system) in memo:
        return memo[id(file_system)]
    
    found = False
    for item in file_system:
        if item == file_name:
            return True
        elif item != file_name:
            if isinstance(item, list):
                return find_file(item, file_name, memo)
    memo[id(file_system)] = found
    return False

print(find_file(file_system, "rasmlar-again"))


def fib_memo(n, memo):
    if memo is None:
        memo = {}
        
    if n <= 1:
        return n
    
    if n in memo:
        return memo[n]
    
    result = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    
    memo[n] = result
    return result

print(fib_memo(50, {}))

def climb_stairs(n, memo):
    if memo is None:
        memo = {}
        
    if n == 0: return 1
    if n < 0: return 0
    
    if n in memo:
        return memo[n]
    
    result =  climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    memo[n] = result
    return result

print(climb_stairs(3, {}))
print(climb_stairs(30, {}))