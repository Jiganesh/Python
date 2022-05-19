Find the Number is even or not.

Find the Number is even or not in recursive way.

Post Order Iterative Traversal for Binary Search Tree

Custom Question 

N is the Number of Houses 
K is the Number of Houses of Tax Officers
next K lines will be  tax collected at the house and index of that house.

Answer : Find the minimum Tax paid across the street for each house.

8
2
14 2
16 6

Visual Representation of Input :

                  H   H  14   H   H   H  16  H

Output : 16 15 14  15 16  17 16 17

O(NK)     16  15 14 15  16  17    _  19       Update with min each time of tax payer
                  22  21 20 19 18   17  16 18 

