def main():
	N = int(input())
	S = [["#" for _ in range(N)] for _ in range(N)]
	for i in range(1, N+1, 1):
		S = paint(N, S, i)
		# print(S)
	for i in range(N):
		for j in range(N):
			print(S[i][j], end="")
		print("")

def paint(N, S, i):
	if i % 2 == 0:
		s = "."
	else:
		s = "#"
	j = N + 1 - i
	if i > j:
		return S
	for column in range(i-1, j):
		for row in range(i-1, j):
			S[column][row] = s
	return S
if __name__ == "__main__":
	main()
