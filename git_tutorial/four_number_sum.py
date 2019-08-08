# O(n^2) tme | O(n^2) space

def four_num_sum(array, targetsum):
    allpairs_sum = {}
    quadruplets = []
    
    for i in range(1, len(array, targetsum)):
        for j in range(i +1, len(array)):
            current_sum = array[i] + array[j]
            difference = targetsum - current_sum
            if difference in allpairs_sum:
                for pair in allpairs_sum[difference]:
                    quadruplets.append(pair+[array[i], array[j]])
                    
            for k in range(0, i):
                current_sum = array[i] + array[k]
                if current_sum not in allpairs_sum:
                    allpairs_sum[current_sum] = [[array[k], array[i]]]
                else:
                    allpairs_sum[current_sum].append([array[k], array[i]])

    return quadruplets