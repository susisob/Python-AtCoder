def main():
	N, M = list(map(int, input().split()))
	A = set(list(map(int, input().split())))
	B = {i for i in range(1, N+1, 1)}
	C = sorted(list(B - A))
	num = len(C)
	print(num)
	if num > 0:
		for i in range(num):
			if i == num - 1:
				print(C[i])
			else:
				print(C[i], end=" ")
	else:
		print("")

if __name__ == "__main__":
	main()
