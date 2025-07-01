tipo = []
for a in range(3):
    tipo.append(input())


classes = {
    "vertebrado": {
        "ave": {
            "carnivoro": "aguia",
            "onivoro": "pomba"
        },
        "mamifero":{
            "onivoro": "homem",
            "herbivoro": "vaca"
        }
    },
    "invertebrado":{
        "inseto": {
            "hematofago": "pulga",
            "herbivoro": "lagarta"
        },
        "anelideo":{
            "hematofago": "sanguessuga",
            "onivoro": "minhoca"
        }
    }
}
animal= classes[tipo[0]][tipo[1]][tipo[2]]
print(animal)