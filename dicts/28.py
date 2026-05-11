def find_duplicates(lst):
    seen = set()
    duplicates = set()

    for num in lst:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


# Example
data = [1, 2, 3, 2, 4, 1]
print(find_duplicates(data)) 