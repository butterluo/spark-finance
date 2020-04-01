# -*- coding: utf-8 -*-
def separation(liste, pivot, i):
 2    """Entrée : une liste, un pivot et la place du pivot dans la liste
 3    Sortie : une liste listePetit contenant les éléments de liste strictement plus petits que le pivot et une liste listeGrand contentant, à l'exception du pivot, les éléments plus grands que le pivot"""
 4    listePetit = []
 5    listeGrand = []
 6    for k in range(len(liste)):
 7        """Cela permet d'exclure le pivot"""
 8        if k <> i:
 9            if liste[k] >= pivot :
10                listeGrand.append(liste[k])
11            else :
12                listePetit.append(liste[k])
13    return listePetit, listeGrand
14 
15 def quicksort(liste):
16    """Entrée : une liste
17       Sortie : une liste avec les mêmes éléments triés par l'algorithme de tri rapide randomisé"""
18    n = len(liste)
19    if n == 1:
20        """Une liste à 1 élément est toujours triée"""
21        return liste 
22    else:
23        """Choix du pivot AU HASARD dans la liste"""
24        i = randint(0, n - 1) 
25        pivot = liste[i]
26        
27        """On sépare en 2 listes de taille strictement plus petite que n car le pivot n'appartient à aucune des deux listes"""
28        liste1, liste2 = separation(liste, pivot, i) 
29        
30        """Le résultat est la concaténation des deux sous-listes auparavant triés, avec le pivot entre elles"""
31        return quicksort(liste1) + [pivot] + quicksort(liste2)



