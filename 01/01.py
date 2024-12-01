with open("input.txt") as input_file:
  lines = input_file.readlines()

list_left = []
list_right = []

for line in lines:
  nums = line.split()
  list_left.append(int(nums[0]))
  list_right.append(int(nums[1]))

list_left = sorted(list_left)
list_right = sorted(list_right)

sum_of_differences = 0

for i in range(len(list_left)):
  sum_of_differences += abs(list_left[i] - list_right[i])

print(f"Part 1: {sum_of_differences}")

right_occurrence_dict = {}

for right_num in list_right:
  if right_num not in right_occurrence_dict:
    right_occurrence_dict[right_num] = 0
  right_occurrence_dict[right_num] += 1

similarity_score = 0

for left_num in list_left:
  if left_num in right_occurrence_dict:
    similarity_score += left_num * right_occurrence_dict[left_num]

print(f"Part 2: {similarity_score}")