"""
Generate test cases for addition

Generates tests for all possible N-bit additions, with different amounts of leading zeroes.
"""

def rbfy(v):
	return v.replace('0', 'R').replace('1', 'B')

bits = 5
N = 2**bits

for a in range(N):
	A = bin(a)[2:]
	for b in range(N):
		B = bin(b)[2:]
		c = a + b
		C = bin(c)[2:]
		for ai in range(bits - len(A) + 2):
			A2 = ai*'0' + A
			for bi in range(bits - len(B) + 2):
				B2 = bi*'0' + B
				C2 = '|'.join(ci*'0' + C for ci in range(bits - len(C) + 2))
				print(rbfy(A2+'G'+B2), rbfy(C2), 'ACCEPT')

