import random

class Jogo:
  def __init__(self, probabilidadeA):
    self.probabilidadeA = probabilidadeA
    self.pontos = ['0','0']
    self.vencedor = None
    self.set = [0,0]
  
  def joga(self):
      while 2 not in self.set:
          self.joga_set()
          if self.vencedor == 'A':
              self.set[0] = self.set[0]+1
          else:
              self.set[1] = self.set[1]+1
      return self.vencedor,self.pontos

  def joga_set(self):
      while self.vencedor == None:
          self.joga_round()

  def joga_round(self):
      resultado = random.uniform(0, 1)
      if resultado <= self.probabilidadeA:
          self.ganha_A()
      else:
          self.ganha_B()
  
  def ganha_A(self):
      if self.pontos[0] == '0':
          self.pontos[0] = '15'
          self.pontos[1] = 'Love'
      elif self.pontos[0] == '15' and self.pontos[1] != '30' and self.pontos[1] != '40':
          self.pontos[0] = '30'
      elif self.pontos[0] == '30':
          self.pontos[0] = '40'
      elif self.pontos[0] == '40' or self.pontos[0] == 'Adv A':
          self.pontos[0] = 'G'
          self.vencedor = 'A'
      elif self.pontos[0] == 'Love':
          self.pontos[0] = '15'
      elif (self.pontos[0] == '15' and self.pontos[1] == '30') or self.pontos[0] == 'Adv B':
          self.pontos[0] = 'Deuce'
          self.pontos[1] = 'Deuce'
      elif self.pontos[0] == '15' and self.pontos[1] == '40':
          self.pontos[0] = 'Adv B'
          self.pontos[1] = 'Adv B'
      elif self.pontos[0] == 'Deuce':
          self.pontos[0] = 'Adv A'
          self.pontos[1] = 'Adv A'


  def ganha_B(self):
      if self.pontos[1] == '0':
          self.pontos[1] = '15'
          self.pontos[0] = 'Love'
      elif self.pontos[1] == '15' and self.pontos[0] != '30' and self.pontos[0] != '40':
          self.pontos[1] = '30'
      elif self.pontos[1] == '30':
          self.pontos[1] = '40'
      elif self.pontos[1] == '40' or self.pontos[1] == 'Adv A':
          self.pontos[1] = 'G'
          self.vencedor = 'B'
      elif self.pontos[1] == 'Love':
          self.pontos[1] = '15'
      elif (self.pontos[1] == '15' and self.pontos[0] == '30') or self.pontos[0] == 'Adv B':
          self.pontos[0] = 'Deuce'
          self.pontos[1] = 'Deuce'
      elif self.pontos[1] == '15' and self.pontos[0] == '40':
          self.pontos[0] = 'Adv A'
          self.pontos[1] = 'Adv A'
      elif self.pontos[1] == 'Deuce':
          self.pontos[0] = 'Adv B'
          self.pontos[1] = 'Adv B'
  


