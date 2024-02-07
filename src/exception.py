def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    index_to_begin = 0
    i =0
    sum_=0
    count = 0
    max_count =0
    while i < len(a):
        
        if a[i] == k:
            count = 0
            sum_ = a[i]
            count = count + 1
            if  max_count==0 or count > max_count:
                max_count = count
            
        
                
            
        elif sum_ < k:
            sum_ = sum_ + a[i]
            count = count + 1
            
    
        elif sum_==k or sum_ > k or a[i]:
                    
            if sum_ ==k:
                if count >max_count:
                    max_count = count
            
            count = 0
            sum_ = 0

            i = index_to_begin + 1
            index_to_begin = index_to_begin + 1

        i = i + 1
    return max_count 

print(longestSubarrayWithSumK([1,2,1,3],2))