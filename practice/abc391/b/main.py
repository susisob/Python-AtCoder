def main():
	N, M = list(map(int, input().split()))
	S = []
	T = []
	a = -1
	b = -1
	for _ in range(N):
		S.append(list(input()))
	for _ in range(M):
		T.append(list(input()))
	for i in range(N - M + 1):
		for j in range(N - M + 1):
			if S[i][j] == T[0][0]:
				for k in range(M):
					for l in range(M):
						if S[i + k][j + l] == T[k][l]:
							continue
						else:
							break
					else:
						continue
					break
				else:
					print(i+1, j+1)
					return

if __name__ == "__main__":
	main()
