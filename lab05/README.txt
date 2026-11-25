Laborator 05 - Recomandări content-based folosind cosine similarity
=====================================================================

Student: Jitaru Vladimir


1. Dataset
----------
tesco_sample.json - produse din supermarketurile Tesco. Câmpul cu text folosit
este "description" (descrierea produsului, care conține și tag-uri HTML).

Dataset-ul are 266 de rânduri, dar același produs apare de mai multe ori (același
"sku"). După eliminarea duplicatelor rămân 189 de produse unice. Fără acest pas,
perechile "cele mai asemănătoare" ar fi fost un produs cu el însuși (scor 1.0).


2. Implementare (cosine_similarity.py)
--------------------------------------
Script adaptat după tutorialul de pe Moodle ("Document Similarity Using Cosine
Similarity"):

  a) Preprocesarea textului:
     - eliminarea tag-urilor HTML (BeautifulSoup);
     - transformarea în litere mici;
     - eliminarea cifrelor și a caracterelor speciale;
     - eliminarea stopwords-urilor (lista de cuvinte în engleză din scikit-learn).
  b) Fiecare descriere este transformată într-un vector TF-IDF (TfidfVectorizer).
     Vocabularul are 3689 de cuvinte unice.
  c) Se calculează cosine similarity între toți vectorii (cosine_similarity).


3. Matricea de similaritate
---------------------------
Fișierul similarity_matrix.csv conține matricea 189 x 189: celula de pe rândul i
și coloana j este scorul de similaritate dintre produsul i și produsul j
(1 = descrieri identice, 0 = niciun cuvânt comun). Diagonala este 1.


4. Două produse asemănătoare
----------------------------
  Bondi Sands Aero Self Tanning Foam 225Ml  <->  Bondi Sands 1 Hour Express Foam 225Ml
  Cosine similarity: 0.9117

Perechea are sens: ambele sunt spume autobronzante (aerated self tanning foam) de
la aceeași marcă, în același ambalaj de 225 ml. Descrierile au aproape aceleași
cuvinte: "dual action tanning formula", "quick dry formula", "coconut scent", aproape
aceeași listă de ingrediente și aceiași pași de aplicare. Diferența principală este
că varianta "1 Hour Express" dezvoltă bronzul într-o oră. Pentru Bondi Sands Aero,
următoarele recomandări sunt tot produse autobronzante:

  0.9117  Bondi Sands 1 Hour Express Foam 225Ml
  0.6641  Bondi Sands Liquid Gold Tan Oil 270Ml
  0.4396  Skinny Tan Coconut Water Tanning Mist 150Ml   (altă marcă)

Alt exemplu: pentru uleiul de motor "Castrol Edge 5W-30 1L", primele 4 recomandări
sunt tot uleiuri de motor (Castrol Mag 10W/40 1L - 0.7626, apoi trei uleiuri Redex).

Cele mai mari scoruri din toată matricea (peste 0.98) sunt variante ale aceluiași
produs care diferă doar prin culoare sau mărime, de exemplu "Blue Balloon Arch 60
Balloons" <-> "Pink Balloon Arch 60 Balloons" (0.9948).


5. Rulare
---------
  pip install scikit-learn pandas beautifulsoup4
  python lab05/cosine_similarity.py

Scriptul afișează cele mai asemănătoare 10 perechi de produse și recomandările
pentru un produs, apoi salvează matricea în similarity_matrix.csv.
