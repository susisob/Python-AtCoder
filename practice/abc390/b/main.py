def main():
	N = int(input())
	A = list(map(int, input().split()))
	if N == 2:
		print("Yes")
		return
	for i in range(1, N - 1):
		if A[i] * A[i] == A[i + 1] * A[i - 1]:
			continue
		else:
			print("No")
			break
	else:
		print("Yes")

if __name__ == "__main__":
	main()
