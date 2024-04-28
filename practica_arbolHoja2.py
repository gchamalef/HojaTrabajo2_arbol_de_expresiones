import matplotlib.pyplot as plt
import networkx as nx

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def construir_arbol_expresion(expresion):
    expresion = expresion.replace(" ", "")
    return construir_arbol_recursivo(expresion)

def construir_arbol_recursivo(expresion):
    if len(expresion) == 0:
        return None

    nivel_par = 0
    operador_index = None
    for i in range(len(expresion) - 1, -1, -1):
        if expresion[i] == ')':
            nivel_par += 1
        elif expresion[i] == '(':
            nivel_par -= 1
        elif nivel_par == 0 and expresion[i] in "+-*/":
            operador_index = i
            break

    if operador_index is not None:
        nodo = Nodo(expresion[operador_index])
        nodo.izquierda = construir_arbol_recursivo(expresion[:operador_index])
        nodo.derecha = construir_arbol_recursivo(expresion[operador_index + 1:])
        return nodo
    else:
        if expresion[0] == '(' and expresion[-1] == ')':
            return construir_arbol_recursivo(expresion[1:-1])
        else:
            return Nodo(expresion)

def dibujar_arbol_expresion(arbol):
    G = nx.DiGraph()

    def agregar_nodo(nodo):
        if nodo:
            G.add_node(nodo.valor)
            if nodo.izquierda:
                G.add_edge(nodo.valor, nodo.izquierda.valor)
                agregar_nodo(nodo.izquierda)
            if nodo.derecha:
                G.add_edge(nodo.valor, nodo.derecha.valor)
                agregar_nodo(nodo.derecha)

    agregar_nodo(arbol)

    pos = nx.nx_pydot.graphviz_layout(G, prog="dot")
    nx.draw(G, pos, with_labels=True, arrows=True)
    plt.show()

# Ejemplo de uso
expresion = "3*(9-3*4)"
arbol_expresion = construir_arbol_expresion(expresion)
if arbol_expresion:
    dibujar_arbol_expresion(arbol_expresion)