class BuscaEmProdundidade:
  def profundidade(self, o, d, g):
    pilha    = []
    pai      = []
    visitado = []
    pilha.append(o)
    pai.append(-1)
    topo = 0
    while len(pilha)>0:
      atual = pilha[topo]
      print("Estou em", atual.getNome())
      if atual == d:
        self.mostraCaminho(topo, pilha, pai)
        return True
      elif atual.getEstado() == 0 and not atual in visitado:
        atual.setEstado(1)
        sucessores = g.getSucessor(atual)
        sucessoresValidos = 0
        for i in sucessores:
          if not i in visitado:
            pilha.append(i)
            pai.append(topo)
            sucessoresValidos = sucessoresValidos + 1
        topo = topo + sucessoresValidos
        visitado.append(atual)
      else:
        pilha.pop()
        pai.pop()
        topo = topo - 1
    return False

  def mostraCaminho(self, atu, pilha, pai):
    if atu == -1:
      print("\n\nCaminho ************* ")
    else:
      self.mostraCaminho(pai[atu], pilha, pai)
      print(pilha[atu].getNome())


