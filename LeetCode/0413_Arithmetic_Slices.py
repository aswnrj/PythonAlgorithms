class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        """
        Function to find the numbers of pairs of 3 or more numbers that are in AP
        
        A : The list consisting of numbers
        
        returns the number of AP slices
        """
#       Initialize two variables 'c' and 'cnt' to 0 to start with
        c = 0
        cnt = 0
        
#       If number of elements in the array is 2 or less, there cant be any AP slice. So return 0
        if len(A) <= 2:
            return 0
        
#       Iterate through the loop starting the pointer from 2nd index to the last index        
        for i in range(2, len(A)):
        
#           If the current pointer points to the last element of an AP slice, increment c by 1
            if A[i-2] + A[i] == 2*(A[i-1]):
                c += 1
#           If it doesnt, that is the end of the streak and from that streak we can obtain 1+2+...+N AP slices if N is the length of the streak. This can be represented by (N*(N+1))//2
#           Also we must reset 'c' to zero to start counting the next streak
            else:
                cnt += (c*(c+1))//2
                c = 0
                
#       If a streak is going on (c!=0), add the numbers of AP slices in that streak to cnt
        cnt += (c*(c+1))//2
    
#       Return the cnt variable which is the answer to our problem
        return cnt
