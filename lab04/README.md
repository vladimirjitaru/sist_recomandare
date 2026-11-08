# Laborator 4 - Ontologie Pizza în WebProtégé

Ontologia descrie domeniul pizza (pizze, toppinguri, blaturi) și include un individ care îl reprezintă pe autor, identificat prin hash-ul SHA-256 al emailului instituțional.

- **Proiect WebProtégé:** [link de share](https://webprotege.stanford.edu/#projects/cc1be25b-6424-42dc-b956-106c414e718c/edit/Classes) (același link este în [`ontologie.txt`](ontologie.txt), fișierul predat pe Moodle)
- **Ontologia exportată (OWL, RDF/XML):** [`pizza.owl`](pizza.owl)

## Clase

| Clasă principală | Subclase |
| --- | --- |
| `Pizza` | `MargheritaPizza`, `PepperoniPizza`, `VegetarianPizza` |
| `Topping` | `CheeseTopping`, `MeatTopping`, `VegetableTopping`, `SauceTopping` |
| `PizzaBase` | `ThinCrustBase`, `DeepPanBase` |
| `Student` | - |

Cele 4 clase principale sunt declarate disjuncte (un individ nu poate fi, de exemplu, și `Pizza`, și `Topping`).

## Proprietăți de obiect

| Proprietate | Domeniu → Codomeniu | Observații |
| --- | --- | --- |
| `hasTopping` | `Pizza` → `Topping` | inversa lui `isToppingOf` |
| `isToppingOf` | `Topping` → `Pizza` | |
| `hasBase` | `Pizza` → `PizzaBase` | funcțională (o pizza are un singur blat) |
| `likesPizza` | `Student` → `Pizza` | preferințele studentului |

## Proprietăți de date

| Proprietate | Domeniu | Tip | Observații |
| --- | --- | --- | --- |
| `hasPrice` | `Pizza` | `xsd:decimal` | prețul, în lei |
| `hasCalories` | - | `xsd:integer` | kcal; folosită la pizze, toppinguri și blaturi |
| `isSpicy` | `Topping` | `xsd:boolean` | |
| `hasUserHash` | `Student` | `xsd:string` | hash-ul SHA-256 generat cu [`my_hash.py`](my_hash.py) |

## Indivizi

| Individ | Clasă | Valori |
| --- | --- | --- |
| `margheritaPizza1` | `MargheritaPizza` | `hasBase` thinBase1; `hasTopping` mozzarella1, tomatoSauce1; 32.50 lei; 790 kcal |
| `pepperoniPizza1` | `PepperoniPizza` | `hasBase` deepPanBase1; `hasTopping` mozzarella1, tomatoSauce1, pepperoni1; 39.90 lei; 1530 kcal |
| `vegetarianPizza1` | `VegetarianPizza` | `hasBase` thinBase1; `hasTopping` mozzarella1, tomatoSauce1, mushroom1; 35.00 lei; 830 kcal |
| `mozzarella1` | `CheeseTopping` | 280 kcal; nu e picant |
| `tomatoSauce1` | `SauceTopping` | 60 kcal; nu e picant |
| `pepperoni1` | `MeatTopping` | 490 kcal; picant |
| `mushroom1` | `VegetableTopping` | 40 kcal; nu e picant |
| `thinBase1` | `ThinCrustBase` | 450 kcal |
| `deepPanBase1` | `DeepPanBase` | 700 kcal |
| `euStudent` | `Student` | `likesPizza` margheritaPizza1, vegetarianPizza1; `hasUserHash` `3f02e819…2f68d6` |

## Import în WebProtégé

1. *Create New Project* → *Create from existing sources* → se încarcă `pizza.owl`.
2. *Share* → *Anyone with the link can View* → *Copy link*.
