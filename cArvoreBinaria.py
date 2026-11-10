# ##################################################
# Classe cArvoreBinária
# ##################################################

import cNo

# *******************************************************
#
# *******************************************************
class percursos:
  PRE_ORDEM   = 0
  IN_ORDEM    = 1
  POST_ORDEM  = 2

# *******************************************************
#
# *******************************************************
class cArvoreBinaria:
  
  chave = 0

# *******************************************************
  def __init__(self, n):
    self.__raiz   = None
    self.__numNos = 0

    self.__raiz   = self.__MontaAB(n)

# *******************************************************
  def getNumNos(self):
    return self.__numNos

# *******************************************************
  def percorreArvore(self, percurso=percursos.PRE_ORDEM):

    if percurso == percursos.PRE_ORDEM:
      self.__preOrdem(self.__raiz)

    elif percurso == percursos.IN_ORDEM:
      self.__inOrdem(self.__raiz)

    elif percurso == percursos.POST_ORDEM:
      self.__postOrdem(self.__raiz)
 
# *******************************************************
  def __MontaAB(self, n):

    return None
    

# *******************************************************
  def __preOrdem(self, raiz):
    return None

 
# *******************************************************
  def __inOrdem(self, raiz):

    return None

# *******************************************************
  def __postOrdem(self, raiz):
 
    return None

  
# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

  arvore = cArvoreBinaria(20)

  print("chave = ", arvore.chave)

  print("Percurso em Pré-Ordem:")
  print("======================")
  arvore.percorreArvore(percursos.PRE_ORDEM)
  print("======================")

  print("Percurso em In-Ordem:")
  print("======================")
  arvore.percorreArvore(percursos.IN_ORDEM)
  print("======================")

  print("Percurso em Post-Ordem:")
  print("======================")
  arvore.percorreArvore(percursos.POST_ORDEM)
  print("======================")

