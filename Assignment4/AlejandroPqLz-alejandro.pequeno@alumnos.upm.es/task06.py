# -*- coding: utf-8 -*-
"""Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GWMelKza6MIaB-3L7Y8g5ywyjZIldNd8

**Task 06: Modifying RDF(s)**
"""

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/resources/example5.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.1: Create a new class named "University"**"""

ns = Namespace("http://somewhere#")
g.add((ns.University, RDF.type, RDFS.Class))

#visualizamos el resultado:
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

ns = Namespace("http://somewhere#")
g.add((ns.Person, RDF.type, RDFS.Class)) #definimos Person
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))

#visualizamos el resultado:
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""

# primero definimos la URI de Jane Smith
ns = Namespace("http://somewhere#")
janeURI = ns.JaneSmith # y definiremos su nombre en el siguiente apartado (6.4).

# definimos y añadimos en el grafo que Jane Smith sea de clase Researcher:
g.add((janeURI, RDF.type, ns.Researcher))

#visualizamos el resultado:
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**"""

# definimos un namespace con el predicado fullName(FN), givenName(Given), familyName(Family):
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#") 

# fullName
#################
fullName = Literal("Jane Smith") #definimos el fullName
fullName_triple = (janeURI, vcard.FN, fullName) #creamos el triple
# añadimos dicho triple al grafo
g.add(fullName_triple)

# GivenName 
#################
givenName = Literal("Jane")
g.add((janeURI, vcard.Given, givenName)) #definimos directamente el triple

# FamilyName
#################
familyName = Literal("Smith")
g.add((janeURI, vcard.Family, familyName))

#visualizamos el resultado:
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.5: Add UPM as the university where John Smith works**"""

# Namespaces para el problema 
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
ns = Namespace("http://somewhere#")

#Hacemos al comprobacion de que Jonh Smith se encuentre en el grafo:
for s,p,o in g:
  if s == ns.JohnSmith:
    print(True)
print("\n")

# Observamos que sí que esta definido, por tanto, podemos definimos lo pedido por el enunciado:
upmURI = ns.UPM
g.add((upmURI, RDF.type, ns.University)) #definimos y añadimos al grafo que UPM es una Universidad (de tipo Universidad)
g.add((ns.JohnSmith, vcard.Work, upmURI)) #definimos y añadimos al grafo que John Smith trabaja en la UPM

#visualizamos el resultado:
for s, p, o in g:
  print(s,p,o)

