# Lab07 - Árvore Binária

## Objetivos:

1. Reforçar o conceito da estrutura de dados *Árvore*;
2. Codificar o TAD/Classe *ÁrvoreBinária* utilizando a linguagem *Python*;
3. Aprofundar a compreensão dessa estrutura de dados. 

## Exercicios: 

Com base na implementação parcial do **TAD Árvore Binária**, faça o que se pede.

1. Analise os módulos *cNo.py* e *cArvoreBinaria.py*. Neles, são fornecidos apenas os métodos básicos e um código de teste da classe. Repare que:

    * O atributo **chave** está definido fora do construtor da classe. Qual a diferença em relação aos atributos definidos no construtor?

2. Implemente o método **__MontaAB** que recebe como parâmetro o número de nós que a árvore binária conterá. O algoritmo desse método deve seguir os seguintes passos:

    * Aloca um nó para a raiz da subárvore atual;
    * Calcula quantos nós restam para inclusão;
    * Divide a quantidade de nós restantes para as subárvores direita e esquerda;
    * *Monta* a subárvore esquerda;
    * *Monta* a subárvore direita. 

3. Codifique os 3 métodos de percurso de uma árvore binária:

    * Pré-Ordem;
    * In-Ordem;
    * Pós-Ordem.

4. Modifique a classe *cNo* para que seja armazenado em cada nó o seu nível. Alterações nos métodos da classe *cArvoreBinaria* devem ser feitas para gerar e manter essa informação. 

5. Implemente um método que calcule a altura da *árvore binária*.

7. Implemente um método que calcule o número total de nós da árvore, sem utilizar o atributo **numNos** da classe.

6. Codifique um método que calcule o número de nós da árvore, para cada tipo:

    * Folha (sem filhos);
    * Completo (com 2 filhos);
    * Semi-Cheio ou incompleto (com um filho).

8. Dadas duas árvores binárias, verificar se são estruturalmente idênticas, ou seja, se possuem a mesma estrutura de nós, independentemente dos valores armazenados em seus nós. 

9. Dadas duas árvores binárias, verificar se são idênticas, ou seja, se possuem a mesma estrutura de nós e os mesmos valores armazenados. 

# Referências Bibliográficas:

Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. **Algoritmos – Teoria e Prática**. Editora Campus. 3ª Edição, 2012.

Canning, J., Broder, A., Lafore, R. **Data Structures & Algorithms in Python**. Addison-Wesley. 2022.

