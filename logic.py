from random import randint, choice
import requests
from funcs import *


HP_RANGE = [-55, -40, -25, 0, 25, 60, 100]
ATTACK_RANGE = [-12, -8, -4, 0, 5, 10, 15]

def get_offset(): #1 tier - 60%, 2 tier - 26%, 3 tier - 10,5%, 4 tier - 2,5%
    multiple = choice([1, -1])
    if chance(0.6):
        offset = 0
    elif chance(0.67):
        offset = 1
    elif chance(0.8):
        offset = 2
    else:
        offset = 3
    offset *= multiple
    offset += 3
    return offset

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer:str, hp:int, attack:int):

        self.pokemon_trainer = pokemon_trainer
        self.attack = attack
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        Pokemon.pokemons[pokemon_trainer] = self
        
        self.hp = hp + HP_RANGE[get_offset()]
        self.attack = attack + ATTACK_RANGE[get_offset()]
        

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['front_default'])
        else:
            return "Pikachu"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}\nЗдоровье твоего покемона: {self.hp}\nНаносимый урон твоего покемона: {self.attack}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def fight(self, enemy):
        if enemy.hp > self.attack:
            enemy.hp -= self.attack
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
