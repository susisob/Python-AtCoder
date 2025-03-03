def main():
	N = int(input())
	A = list(map(int, input().split()))
	for i in range(N-1):
		if A[i] < A[i+1]:
			continue
		else:
			print("No")
			return
	else:
		print("Yes")
		return
if __name__ == "__main__":
	main()
