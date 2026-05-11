nums = [1, 2, 3, 4, 5]

di = {}  # sum → pair

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        s = nums[i] + nums[j]

        if s in di:
            print("Pairs with same sum:")
            print(di[s], "and", (nums[i], nums[j]))
            break
        else:
            di[s] = (nums[i], nums[j])
               