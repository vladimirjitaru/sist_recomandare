import os
import re
import json
import pandas as pd
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import cosine_similarity

LAB05_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_DATASET = os.path.join(LAB05_DIR, 'tesco_sample.json')
PATH_MATRICE = os.path.join(LAB05_DIR, 'similarity_matrix.csv')


def incarca_produse():
    """Citeste dataset-ul Tesco si pastreaza o singura aparitie pentru fiecare produs (sku)"""
    with open(PATH_DATASET, encoding='utf-8') as f:
        produse = json.load(f)

    # Acelasi produs apare de mai multe ori in dataset (266 de randuri, 189 de sku-uri unice)
    df = pd.DataFrame(produse).drop_duplicates(subset='sku').reset_index(drop=True)
    print(f"S-au citit {len(produse)} de randuri, dintre care {len(df)} produse unice.")
    return df


def preproceseaza(descriere_html):
    """Elimina tag-urile HTML, cifrele si caracterele speciale, apoi stopwords-urile"""
    text = BeautifulSoup(descriere_html, 'html.parser').get_text(separator=' ')
    text = text.lower()
    text = re.sub(r'[^a-z\s]', ' ', text)
    cuvinte = [cuvant for cuvant in text.split() if cuvant not in ENGLISH_STOP_WORDS and len(cuvant) > 1]
    return ' '.join(cuvinte)


def main():
    df = incarca_produse()
    df['text'] = df['description'].apply(preproceseaza)

    # Transformam fiecare descriere intr-un vector TF-IDF
    tfidf = TfidfVectorizer()
    response = tfidf.fit_transform(df['text'])
    print(f"Vocabular: {len(tfidf.vocabulary_)} de cuvinte unice.")

    # Matricea de similaritate: celula [i][j] = cosine similarity intre produsul i si produsul j
    scoruri = cosine_similarity(response)
    matrice = pd.DataFrame(scoruri, index=df['name'], columns=df['name'])
    matrice.round(4).to_csv(PATH_MATRICE, encoding='utf-8')
    print(f"Matricea de similaritate ({len(df)} x {len(df)}) a fost salvata in {os.path.basename(PATH_MATRICE)}\n")

    # Perechile de produse diferite, ordonate descrescator dupa scor
    perechi = [
        (scoruri[i][j], df['name'][i], df['name'][j])
        for i in range(len(df)) for j in range(i + 1, len(df))
    ]
    perechi.sort(reverse=True)

    # Scorul 1.0 inseamna descrieri identice (variante ale aceluiasi produs), deci le sarim
    print("Top 10 perechi de produse asemanatoare (fara descrieri identice):")
    for scor, produs_a, produs_b in [p for p in perechi if p[0] < 0.999][:10]:
        print(f"  {scor:.4f}  {produs_a}  <->  {produs_b}")

    # Exemplu de recomandare: cele mai asemanatoare 5 produse pentru un produs ales
    produs = 'Castrol Edge 5W-30 1L'
    print(f"\nProduse recomandate pentru '{produs}':")
    for nume, scor in matrice[produs].drop(produs).nlargest(5).items():
        print(f"  {scor:.4f}  {nume}")


if __name__ == '__main__':
    main()
