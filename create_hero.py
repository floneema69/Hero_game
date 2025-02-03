from faker import Faker
import random
import pyxel

fake = Faker()

class Hero:
    def __init__(self, name, age,hp, genre,inventaire,hair):
        self.name = name
        self.age = age
        self.hp = hp
        self.genre = genre
        self.inventaire = inventaire
        self.hair = hair

def to_string(p1):
    print(f"Votre nom : {p1.name}, votre age : {p1.age},vos hp : {p1.hp}, votre genre : {p1.genre}, votre couleur de cheuveux : {p1.hair}, votre inventaire : {p1.inventaire}")

def get_name():
    try:
        print('Créez votre propre nom (name) ou générez (r):')
        x = input().strip().lower()
        if x == 'r':
            return fake.name()
        elif x == 'name':
            return input("Votre nom : ").strip()
        else:
            raise ValueError("Choix invalide. Veuillez entrer 'name' ou 'r'.")
    except Exception as e:
        print(f"Erreur : {e}")
        return get_name()

def get_color():
    try:
        print("Entrez un nombre pour la couleur (0-15) ou générez (r) :")
        x = input().strip().lower()
        if x == 'r':
            return random.randint(0, 15)
        else:
            color = int(x)
            if 0 <= color <= 15:
                return color
            else:
                raise ValueError("Le nombre doit être compris entre 0 et 15.")
    except ValueError as e:
        print(f"Erreur : {e}")
        return get_color()
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return get_color()

def get_age():
    try:
        print("Votre propre âge (age) ou générez (r):")
        age_generate = input().strip().lower()
        if age_generate == 'age':
            age = int(input("Votre âge : ").strip())
            if age < 16 or age > 130:
                raise ValueError("L'âge doit être compris entre 16 et 130 ans.")
            return age
        elif age_generate == 'r':
            return random.randrange(16, 130)
        else:
            raise ValueError("Choix invalide. Veuillez entrer 'age' ou 'r'.")
    except ValueError as e:
        print(f"Erreur : {e}")
        return get_age()
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return get_age()

def get_genre():
    try:
        print("Votre propre genre (genre) ou générez (r):")
        genre_generate = input().strip().lower()
        if genre_generate == 'genre':
            genre = input("Votre genre : ").strip()
            if genre not in ["Homme", "Femme", "Autre"]:
                raise ValueError("Le genre doit être 'Homme', 'Femme' ou 'Autre'.")
            return genre
        elif genre_generate == 'r':
            mylist = ["Homme", "Femme", "Autre"]
            return random.choice(mylist)
        else:
            raise ValueError("Choix invalide. Veuillez entrer 'genre' ou 'r'.")
    except Exception as e:
        print(f"Erreur : {e}")
        return get_genre()
def get_hp():
    try:
        print("Votre propre hp (hp) ou generez (r):")
        hp_generate = input().strip().lower()
        if hp_generate == 'hp':
            hp = int(input("Votre hp : ").strip())
            if hp <0 or hp > 100:
                 raise ValueError("Les HP doit être compris entre 0 et 100 ans.")
        elif hp_generate == 'r':
            return random.randrange(0, 100)
        else:
            raise ValueError("Choix invalide. Veuillez entrer 'HP' ou 'r'.")
    except ValueError as e:
        print(f"Erreur : {e}")
        return get_hp()
    except Exception as e:
        print(f"Erreur : {e}")
        return get_hp()
def get_inventaire():
    inventaire = []
    try:
        continu = True
        while continu:
            print("Votre propre inventaire yes or no :")
            invetaire_generate = input().strip().lower()
            if (invetaire_generate == 'yes'):
                moy = input("Votre inventaire : ")
                inventaire.append(moy)
            elif (invetaire_generate == 'no'):
                continu = False
                return inventaire
            else:
                raise ValueError("Votre inventaire invalide")
    except ValueError as e:
        print(f"Erreur : {e}")
        return get_inventaire()
    except Exception as e:
        print(f"get_inventaire : {e}")
        return get_inventaire()


pyxel.init(160, 120)

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(7)
    x, y = 80, 60
    pyxel.rect(x, y, 8, 8, 9)
    pyxel.rect(x + 2, y + 8, 4, 8, 9)
    pyxel.rect(x, y + 16, 2, 4, 9)
    pyxel.rect(x + 6, y + 16, 2, 4, 9)
    pyxel.rect(x - 2, y + 8, 2, 4, 9)
    pyxel.rect(x + 8, y + 8, 2, 4, 9)
    if p1.genre == "Femme":
        pyxel.rect(x - 4, y - 8, 16, 8, p1.hair)
        pyxel.rect(x - 6, y, 4, 6, p1.hair)
        pyxel.rect(x + 10, y, 4, 6, p1.hair)
    else:
        pyxel.rect(x, y - 2, 10, 5, p1.hair)



try:
    name = get_name()
    age = get_age()
    genre = get_genre()
    hp = get_hp()
    inventaire = get_inventaire()
    hair = get_color()
    p1 = Hero(name, age,hp,genre,inventaire,hair)
    to_string(p1)
    pyxel.run(update, draw)
except Exception as e:
    print(f"Une erreur est survenue lors de la création du héros : {e}")
