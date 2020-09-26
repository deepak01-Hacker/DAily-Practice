#User function Template for python3

"""
        Code By    : Deepak Kumar
        Contact us : a9649060356@gmail.com
        Contribute with GFG
""""
#Problem:- Given an array Arr[] of size N. Find the number of subarrays whose sum is an even number.



class Solution:
    def countEvenSum(self, arr, n):
        temp = [1, 0] 
  
    # Initialize count. sum is sum of elements 
    # under modulo 2 and ending with arr[i]. 
        result = 0
        sum = 0
      
        # i'th iteration computes sum of arr[0..i] 
        # under modulo 2 and increments even/odd  
        # count according to sum's value 
        for i in range(n): 
              
            # 2 is added to handle negative numbers 
            sum = ( (sum + arr[i]) % 2 + 2) % 2
      
            # Increment even/odd count 
            temp[sum]+= 1
      
        # Use handshake lemma to count even subarrays 
        # (Note that an even cam be formed by two even 
        # or two odd) 
        result = result + (temp[0] * (temp[0] - 1) // 2) 
        result = result + (temp[1] * (temp[1] - 1) // 2) 
      
        return (result) 
        


