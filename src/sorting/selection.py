
def selection_sort():
    for i in range(len(inp)):
        min_idx = i
        for j in range(i+1, len(inp)):
            if inp[min_idx] > inp[j]:
                min_idx = j
        tmp = inp[min_idx]
        inp[min_idx] = inp[i]
        inp[i] = tmp


if __name__ == "__main__":
    inp = [32, 434, 4, 1, 34]
    selection_sort(inp)
    print("Sorted array")
    print(inp)
