def main():
	A = list(map(int, input().split()))
	if A == [2, 1, 3, 4, 5]:
		print("Yes")
	elif A == [1, 3, 2, 4, 5]:
		print("Yes")
	elif A == [1, 2, 4, 3, 5]:
		print("Yes")
	elif A == [1, 2, 3, 5, 4]:
		print("Yes")
	else:
		print("No")

if __name__ == "__main__":
	main()
