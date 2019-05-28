Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
   Constant.
   It is the same amount of operations no matter how large the buffer or input are.

2. What is the space complexity of your ring buffer's `append` function?
   Constant.
   For a given ring buffer, the space is initialized up front. Appending items to the ring buffer does not change the storage space that has already been set aside.

3. What is the runtime complexity of your ring buffer's `get` method?
   Constant.
   No matter the size of the RingBuffer, we are just returning an item. If the ring buffer is not full, we do an operation to convert the list to get rid of the 'None' values. While splicing a list is considered relatively intensive, it is still considered a constant operation.

4. What is the space complexity of your ring buffer's `get` method?
   Constant if the list is filled.
   Since we are using a list splice to get rid of 'None' values if the list is not filled, this creates an additional list and temporarily takes up more storage at worst case size O(n-1).

5. What is the runtime complexity of the provided code in `names.py`?
   n^2.
   since we have 2 nested loops that each go through size n, this is an O(n^2) pattern.

6. What is the space complexity of the provided code in `names.py`?
   linear.
   Considering the names_1 and names_2 arrays, their space complexity is each O(n) taking up a total space of 2n. ~ O(n)

7. What is the runtime complexity of your optimized code in `names.py`?
   linear.  
   we go through 2 for loops of size n, but they are not nested. So overall we go through 2n operations. ~ O(n)

8. What is the space complexity of your optimized code in `names.py`?
   linear.  
   Once again since we use the names_1 and names_2 arrays, these take up space on a linear scale. Additionally we use a hash table which also stores on O(n) space complexity.
