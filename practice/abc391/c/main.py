def main():
	N, Q = list(map(int, input().split()))
	queries = [input() for _ in range(Q)]
	nest = {}
	pigeon = {}
	ans = set()
	for i in range(1, N+1, 1):
		nest[i] = [i]
		pigeon[i] = i
	for query in queries:
		if list(query.split())[0] == "1":
			nest, pigeon, ans = query1(nest, pigeon, query, ans)
		else:
			query2(ans)

def query1(nest, pigeon, query, ans):
	_, P, H, = list(map(int, query.split()))
	H_now = pigeon[P]
	nest[H_now].remove(P)
	nest[H].append(P)
	pigeon[P] = H
	if len(nest[H_now]) > 1:
		ans.add(H_now)
	elif H_now in ans:
		ans.discard(H_now)
	if len(nest[H]) > 1:
		ans.add(H)
	elif H in ans:
		ans.discard(H)
	return nest, pigeon, ans

def query2(ans):
	print(len(ans))

if __name__ == "__main__":
	main()
