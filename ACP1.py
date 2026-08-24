# ── SHOPPING LIST MANAGER ASSIGNMENT ──────────────────────────────────────────

# Step 1: Create and write the initial shopping list to a text file ('w' mode)
file = open("shopping_list.txt", "w")
file.write("1. Apples\n")
file.write("2. Milk\n")
file.write("3. Bread\n")
file.close()

print("Initial shopping list saved to shopping_list.txt!")

# Step 2: Read and display the complete file using read() ('r' mode)
file = open("shopping_list.txt", "r")
content = file.read()
print("\n=== Current Shopping List ===")
print(content)
file.close()

# Step 3: Append new items to the existing list ('a' mode)
file = open("shopping_list.txt", "a")
file.write("4. Eggs\n")
file.write("5. Cheese\n")
file.close()

print("2 new items added to the list!")

# Step 4: Read and print the updated file line-by-line using readlines() ('r' mode)
file = open("shopping_list.txt", "r")
lines = file.readlines()

print("\n=== Updated Shopping List (Line by Line) ===")
for line in lines:
    print(line.strip())

file.close()

# Display total number of items in the list
print(f"\nTotal items in shopping list: {len(lines)}")