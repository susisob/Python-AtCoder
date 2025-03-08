def main():
	S = input()
	count = 0
	for i in range(len(S)):
		if S[i] == "A":
			for j in range(i + 1, len(S), 1):
				if S[j] == "B":
					if 2 * j - i < len(S) and S[2 * j - i] == "C":
						count += 1
	print(count)

if __name__ == "__main__":
	main()
