def max_sum_subarray(arr):
    max_sum = arr[0]
    cur_sum = max_sum
    for i in range(1,len(arr)):
        cur_sum = max(arr[i],arr[i] + cur_sum)
        max_sum = max(cur_sum,max_sum)
    return max_sum
