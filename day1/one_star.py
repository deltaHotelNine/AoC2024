file_path = r"C:\Projects\AoC2024\inputs\day1_input.txt"

left = []
right = []

with open(file_path, "r") as f:
  for line in f:
    parts = line.strip().split("   ")
    left.append(int(parts[0]))
    right.append(int(parts[1]))

sorted_left = sorted(left)
sorted_right = sorted(right)

total = 0

for i in range(len(sorted_left)):
  if sorted_left[i] != sorted_right[i]:
    if sorted_left[i] > sorted_right[i]:
      total += (sorted_left[i] - sorted_right[i])
    else:
      total += (sorted_right[i] - sorted_left[i])

print("Total: ", total)
