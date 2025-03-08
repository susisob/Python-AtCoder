def main():
	N = int(input())
	P = list(map(int, input().split()))
	Q = list(map(int, input().split()))
	M = [_ for _ in range(1, N+1, 1)]
	zip_list = zip(Q, M)
	zip_sort = sorted(zip_list)
	Q_s, M = zip(*zip_sort)
	for i in Q_s:
		if i == N:
			print(Q[P[M[i-1] - 1] - 1])
		else:
			print(Q[P[M[i-1] - 1] - 1], end=" ")

if __name__ == "__main__":
	main()
