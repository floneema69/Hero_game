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
    print('Créez votre propre nom (name) ou générez (r):')
    x = input().strip().lower()
    return get_name_action(x)
def get_name_action(x):
    try:
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
    print("Entrez un nombre pour la couleur (0-15) ou générez (r) :")
    x = input().strip().lower()
    return get_color_action(x)
def get_color_action(x):
    try:
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
    print("Votre propre âge (age) ou générez (r):")
    age_generate = input().strip().lower()
    return get_age_action(age_generate)
def get_age_action(x):
    try:
        if x == 'r':
            return random.randint(16, 130)
        elif x == 'age':
            age = int(input("Votre âge : ").strip())
            if age < 16 or age > 130:
                raise ValueError("L'âge doit être compris entre 16 et 130 ans.")
            return age
        else:
            raise ValueError("Choix invalide. Veuillez entrer 'age' ou 'r'.")
    except Exception as e:
        print(f"Erreur : {e}")
        return get_age()
def get_genre():
    print("Votre propre genre (genre) ou générez (r):")
    genre_generate = input().strip().lower()
    return get_genre_action(genre_generate)
def get_genre_action(x):
    try:
        if x == 'r':
            mylist = ["Homme", "Femme", "Autre"]
            return random.choice(mylist)
        elif x == 'genre':
            genre = input("Votre genre : ").strip().lower()
            if genre not in ["homme", "femme", "autre"]:
                raise ValueError("Le genre doit être 'homme', 'femme' ou 'autre'.")
            return genre
    except ValueError as e:
        print(f"Erreur : {e}")
        return get_genre()
def get_hp():
    print("Votre propre hp (hp) ou generez (r):")
    hp_generate = input().strip().lower()
    return get_hp_action(hp_generate)
def get_hp_action(x):
    try:
        if x == 'r':
            return random.randrange(0, 100)
        elif x == 'hp':
            hp = int(x)
            if hp < 0 or hp > 100:
                raise ValueError("Les HP doit être compris entre 0 et 100 ans.")
            return hp
    except ValueError as e:
        print(f"Erreur : {e}")
        return get_hp()
    except Exception as e:
        print(f"Erreur : {e}")
        return get_hp()
def get_inventaire():
    inventaire = []
    continu = True
    while continu:
        print("Votre propre inventaire yes or no :")
        invetaire_generate = input().strip().lower()
        inventaire, continu = get_inventaire_action(inventaire, invetaire_generate)
    return inventaire

def get_inventaire_action(inventaire, x):
    try:
        if x == 'yes':
            moy = input("Votre inventaire : ")
            inventaire.append(moy)
            return inventaire, True
        elif x == 'no':
            return inventaire, False
        else:
            raise ValueError("Votre inventaire invalide")
    except ValueError as e:
        print(f"Erreur : {e}")
        return inventaire, True
    except Exception as e:
        print(f"get_inventaire : {e}")
        return inventaire, True


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
