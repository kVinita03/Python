def bubbleSort(theSeq):
    n = len(theSeq)
    rounds = 0
    
    for i in range(n-1):
        for j in range(n-i-1):
            if theSeq[j] > theSeq[j+1]:
                tmp = theSeq[j]
                theSeq[j] = theSeq[j+1]
                theSeq[j+1] = tmp       
        rounds += 1
        print(f"รอบที่ {rounds}: {theSeq}")

theSeq = [85, 10, 5, 15, 20, 7, 8, 1, 9, 25]
print("รอบที่ 0:", theSeq)

bubbleSort(theSeq)

print("ผลลัพท์:")
for i in range(len(theSeq)):
    print("%d" % theSeq[i], end=" ")