# -*- coding: utf-8 -*-
"""exercicio3_fila_reversao.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13fX9-VB3maKuFso3Mv20kxjHFt7-SO-T
"""

class Fila:

  def __init__(self):
    self.sequencia = [1, 2, 3, 4]
    self.fila = []
    self.remocao = []

  def adicionar(self, valor=None):
    if valor is None:
      for i in self.sequencia:
        self.fila.append(i)
    else:
      self.fila.append(valor)

  def saida(self):
    while len(self.fila) > 0:
      self.frente = self.fila.pop()
      self.remocao.append(self.frente)
    return self.remocao

user = Fila()

user.adicionar()

print(user.saida())