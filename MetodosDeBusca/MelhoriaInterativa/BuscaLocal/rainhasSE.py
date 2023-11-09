import random
import math

def vetAleatorio(r, n, a, t):
	if t > 0:
		vetAleatorio(r, n, a+1, t//n)
		r[a] = t%n

def geraAleatorio(r, n, a, t):
	na = random.randint(0,t)
	vetAleatorio(r, n, a, na)

def quantidadeDeAtaques(r):
	qtd = 0
	for i in range(0, len(r)-1):
		for j in range(i+1, len(r)):
			if r[i] == r[j] or abs(i-j)==abs(r[i]-r[j]):
				qtd = qtd + 1
	return qtd

def melhorVizinho(r):
	na = r[0:len(r)]
	mr = r[0:len(r)]
	mv = quantidadeDeAtaques(r)
	va = mv
	for i in range(0, len(r)):
		for j in range(0, len(r)):
			if j == r[i]:
				continue
			na = r[0:len(r)]
			na[i] = j
			va = quantidadeDeAtaques(na)
			if va < mv:
				mr = na[0: len(na)]
				mv = va
	return mr, mv

def subidaDeEncosta(r):
	vr = quantidadeDeAtaques(r)
	while True:
		proximo, vp = melhorVizinho(r)
		if vp < vr:
			r = proximo[0:len(proximo)]
			vr = vp
		else:
			break
	return r

n = 5
r = []
proximo = []
vp = 0
for i in range(0, n):
	r.append(0)

geraAleatorio(r, n, 0, n**n)
print("Estado Inicial: ", r, " - Ataques: ", quantidadeDeAtaques(r))
reinicios = -1

while quantidadeDeAtaques(r) > 0:
	geraAleatorio(r, n, 0, n**n)
	r = subidaDeEncosta(r)
	reinicios = reinicios + 1

print("Melhor estado: ", r, " - Ataques: ", quantidadeDeAtaques(r))
print("Reinicios: ", reinicios)