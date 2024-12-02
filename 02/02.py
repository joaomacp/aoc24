def is_safe(array):
  for index, curr_num in enumerate(array):
    if index == 0:
      last_num = curr_num
      continue

    if index == 1:
      sign = -1 if curr_num < last_num else (1 if curr_num > last_num else 0)
      if sign == 0:
        return False
    
    if sign == -1:
      min = last_num - 3
      max = last_num - 1
    else:
      min = last_num + 1
      max = last_num + 3
    
    if not (min <= curr_num <= max):
      return False

    last_num = curr_num
  
  return True

def is_safe_part_2(array):
  if is_safe(array):
    return True
  for i in range(len(array)):
    skipped_array = array[:i] + array[i+1 :]
    if is_safe(skipped_array):
      return True
  return False

with open("input.txt") as input_file:
  lines = input_file.readlines()

safe_reports_part_1 = 0
safe_reports_part_2 = 0

for line in lines:
  array = [int(num) for num in line.split()]
  safe_reports_part_1 += 1 if is_safe(array) else 0
  safe_reports_part_2 += 1 if is_safe_part_2(array) else 0

print(f"Part 1: {safe_reports_part_1}")
print(f"Part 2: {safe_reports_part_2}")