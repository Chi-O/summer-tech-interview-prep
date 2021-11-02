arr = [[2,1],[4,4],[3,1],[4,1],[2,4],[3,4],[1,3],[4,3],[5,3],[5,3]]

freq = {}

for box in arr:
    try: 
        freq[box[1]] += box[0]
    except:
        freq[box[1]] = box[0]

print(freq)