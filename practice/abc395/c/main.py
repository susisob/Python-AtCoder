def main():
	N = int(input())
	A = list(map(int, input().split()))
	M = 1000001

	pos = [[] for _ in range(M)]
	for i in range(N):
		pos[A[i]].append(i)

	ans = N+1
	for i in range(M):
		if len(pos[i]) < 2:
			continue
		else:
			for j in range(1, len(pos[i])):
				ans = min(ans, pos[i][j] - pos[i][j-1] + 1)
	if ans == N+1:
		print(-1)
	else:
		print(ans)

if __name__ == "__main__":
	main()
