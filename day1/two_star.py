file_path = r"C:\Projects\AoC2024\inputs\day1_input.txt"

left = []
right = []

with open(file_path, "r") as f:
  for line in f:
    parts = line.strip().split("   ")
    left.append(int(parts[0]))
    right.append(int(parts[1]))

similarity = 0

for i in range(len(left)):
  occurence = 0
  for j in range(len(right)):    
    if left[i] == right[j]:
      occurence += 1
  similarity += (left[i] * occurence)

print("Total: ", similarity)