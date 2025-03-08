def main():
	N = int(input())
	S_len = []
	S = []
	for i in range(N):
		s = input()
		S.append(s)
		S_len.append(len(s))
	zip_list = sorted(zip(S_len, S))
	S_len, S = zip(*zip_list)
	for i in range(N):
		if i == N - 1:
			print(S[i])
		else:
			print(S[i], end="")

if __name__ == "__main__":
	main()
