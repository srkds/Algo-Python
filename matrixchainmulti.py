import sys

def DoMatrixChainMulti(d, i, j):

	if i == j:
		return 0

	_min = sys.maxsize

	for k in range(i, j):

		count = (DoMatrixChainMulti(d, i, k)
				+ DoMatrixChainMulti(d, k + 1, j)
				+ d[i-1] * d[k] * d[j])

		if count < _min:
			_min = count

	return _min

arr = [18, 4, 13, 7, 15]
length = len(arr)

result = DoMatrixChainMulti(arr, 1, length-1)
print("Minimum Multiplications Are:",result)
