import pytest
from unittest.mock import patch
from create_hero import Hero, get_name_action, get_age_action, get_genre_action, get_hp_action, get_color_action, get_inventaire_action

def test_hero_creation():
    hero = Hero("TestName", 25, 100, "Homme", ["épée", "bouclier"], 5)
    assert hero.name == "TestName"
    assert hero.age == 25
    assert hero.hp == 100
    assert hero.genre == "Homme"
    assert hero.inventaire == ["épée", "bouclier"]
    assert hero.hair == 5



