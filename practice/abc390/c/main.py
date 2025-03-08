def main():
	H, W = list(map(int, input().split()))
	S = []
	for _ in range(H):
		S.append(list(input()))
	a = W
	b = -1
	c = H
	d = -1
	for i in range(H):
		for j in range(W):
			if S[i][j] == "#":
				if a > j:
					a = j
				if b < j:
					b = j
				if c > i:
					c = i
				if d < i:
					d = i
	for i in range(c, d+1, 1):
		for j in range(a, b+1, 1):
			if S[i][j] == ".":
				print("No")
				return
	else:
		print("Yes")
		return

if __name__ == "__main__":
	main()
