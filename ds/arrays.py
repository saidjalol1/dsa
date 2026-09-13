"""
An arrays are collection of items stored at contagious memeory locations. The items can be of any data type. 
In Python , The built in 'list' data type serves as dynamic arrays.
Which means that python handles the resizing of the array automatically under the hood when the array is full.

Characteristics of arrays:
1. Arrays are of fixed size.
2. Contiguous memory locations are used to store the elements of an array. (This allows for efficient access to elements using their index.)
3. Index-based access: Elements in an array can be accessed using their index, which starts from 0.


Time complexity of operations on arrays:
1. Accessing an element by index: O(1) - Constant time complexity, as the index allows direct access to the element.
2. Inserting an element at the end (append): O(1) - Amortized constant time complexity, as Python lists handle resizing automatically.
3. Inserting an element at the beginning or in the middle: O(n) - Linear
4. in general deleting an element from an array: O(n) - Linear time complexity, as elements need to be shifted to fill the gap left by the deleted element.


"""


