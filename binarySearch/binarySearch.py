def binary_search(theValues, target):
    low = 0
    high = len(theValues) - 1
    rounds = 0
    
    while low <= high:
        mid = (high + low) // 2
        rounds += 1
        
        if theValues[mid] == target:
            return mid, rounds
        elif target < theValues[mid]:
            high = mid - 1
        else:
            low = mid + 1
            
    return -1, rounds  # If the element is not found

if __name__ == "__main__":
    test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 9
    
    result, rounds = binary_search(test_list, target)
    if result != -1:
        print("ตำแหน่งที่ :", result)
    else:
        print("ไม่พบตำแหน่ง")
    print("จำนวนครั้งในการทำงานของ while :", rounds, "รอบ")