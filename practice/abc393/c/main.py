def main():
	N, M = list(map(int, input().split()))
	u = []
	v = []
	uv = []
	for _ in range(M):
		u_, v_ = list(map(int, input().split()))
		u.append(u_)
		v.append(v_)
		uv.append((u_, v_))
	uv_simple = simplify_graph(uv)
	print(len(uv) - len(uv_simple))

def simplify_graph(edges):
    uv = set()

    for u, v in edges:
        if u == v:
            continue  # 自己ループ削除
        uv.add(frozenset({u, v}))  # (u, v) と (v, u) を同じとみなす

    return [tuple(edge) for edge in uv]  # frozenset をタプルに変換して出力

if __name__ == "__main__":
	main()
