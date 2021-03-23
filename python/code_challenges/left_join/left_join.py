def left_join(hash1, hash2) -> list:
    output = []
    for node in hash1._buckets:
        if not node == None:
            key = node.head.data[0]
            val_left = node.head.data[1]
            if hash2.contains(key): val_right = hash2.get(key) 
            else: val_right = None
            output.append([key, val_left, val_right])
    return output

