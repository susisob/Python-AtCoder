def main():
	A = list(map(int, input().split()))
	if A[0] * A[1] == A[2]:
		print("Yes")
	elif A[1] * A[2] == A[0]:
		print("Yes")
	elif A[2] * A[0] == A[1]:
		print("Yes")
	else:
		print("No")

if __name__ == "__main__":
	main()
