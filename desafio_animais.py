a = input() 
b = input() 
c = input() 

animais = {
    "vertebrado": {"ave": {"carnivoro": "aguia", "onivoro": "pomba"}, "mamifero": {"onivoro": "homem", "herbivoro": "vaca"}},
    "invertebrado": {"inseto": {"hematofago": "pulga", "herbivoro": "largata"}, "anelideo": {"hematofago": "sanguessuga", "onivoro": "minhoca"}}
}

print(animais[a][b][c])