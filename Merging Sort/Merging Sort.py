def merge_sort(listA, round_num=0):
    print("รอบที่", round_num, ":", listA)
    if len(listA) > 1:
        mid = len(listA) // 2
        left_half = listA[:mid]
        right_half = listA[mid:]
        
        round_num += 1  # Increment round number
        
        merge_sort(left_half, round_num)
        merge_sort(right_half, round_num)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                listA[k] = left_half[i]
                i += 1
            else:
                listA[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            listA[k] = left_half[i]
            i += 1
            k += 1
            
        while j < len(right_half):
            listA[k] = right_half[j]
            j += 1
            k += 1
    print("< เรียง > : ", listA)
    return listA  # Return the sorted list
    
listB = [5, 15, 35, 25, 55, 45, 75, 65, 95, 85]
listC = [1, 10, 2, 20, 3, 30, 4, 40, 6, 50]
listA = merge_sort(listB + listC)
print("ผลลัพท์ : \n", listA)