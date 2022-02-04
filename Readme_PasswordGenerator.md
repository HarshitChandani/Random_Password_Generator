Password Generator Program helps you to generate a random password
of the length of your choice.

Imported Modules:

    1. string
    2. random
 
Password Generator Logic explanations:

    If length is even: Then Divide the length by 4(Because 4 set's of character is being used) 
                           So that we can pick eqaul elements from all set's.
    
    If length is odd: Then divide the length by 3(Because 3 set's of character is being used)
                      for picking of equal elements and remaining set i.e;1 is used to pick 
                      remaining elements by finding out the remainder.
                      

Benefits of above logic:

    Unnecessary merging of all elements of all set's.
 
Constraints:

    Password Length must be <= 33.
    Length cannot be a negative integer.
    
Execution time for 10000 iterations:

    00.0034134 seconds. 