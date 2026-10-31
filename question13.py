import numpy as np

r, c = int(input("Rows: ")), int(input("Columns: "))
img = np.array(input(f"Enter {r*c} pixel values (0-255): ").split(), dtype=int).reshape(r, c)
print("Original image:\n", img)

nr, nc = int(input("New rows: ")), int(input("New columns: "))
print("Reshaped:\n", img.reshape(nr, nc))

r1, r2 = map(int, input("Slice rows (start end): ").split())
c1, c2 = map(int, input("Slice columns (start end): ").split())
print("Sliced region:\n", img[r1:r2, c1:c2])

b = int(input("Brightness value to add: "))
print("Brightened (broadcasting):\n", np.clip(img + b, 0, 255))

print("Horizontally flipped (matrix multiplication):\n", img @ np.eye(c)[::-1])