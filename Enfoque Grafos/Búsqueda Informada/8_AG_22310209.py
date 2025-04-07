import random

def crear_individuo(tam_gen):
    return [random.randint(0, 1) for _ in range(tam_gen)]

def fitness(individuo):
    return sum(individuo)

def seleccionar(poblacion):
    return random.choices(poblacion, k=2)

def cruzar(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1)-1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

def mutar(individuo, tasa_mutacion):
    return [bit if random.random() > tasa_mutacion else 1 - bit for bit in individuo]

def algoritmo_genetico(tam_poblacion, tam_gen, generaciones, tasa_mutacion):
    poblacion = [crear_individuo(tam_gen) for _ in range(tam_poblacion)]
    for _ in range(generaciones):
        poblacion = sorted(poblacion, key=fitness, reverse=True)
        nueva_poblacion = poblacion[:tam_poblacion // 2]
        while len(nueva_poblacion) < tam_poblacion:
            padre1, padre2 = seleccionar(poblacion)
            hijo1, hijo2 = cruzar(padre1, padre2)
            nueva_poblacion.append(mutar(hijo1, tasa_mutacion))
            nueva_poblacion.append(mutar(hijo2, tasa_mutacion))
        poblacion = nueva_poblacion
    return max(poblacion, key=fitness)

# Uso del algoritmo
tam_poblacion = 10
tam_gen = 20
generaciones = 50
tasa_mutacion = 0.01

mejor_individuo = algoritmo_genetico(tam_poblacion, tam_gen, generaciones, tasa_mutacion)
print(f"Mejor Individuo: {mejor_individuo} con Fitness: {fitness(mejor_individuo)}")
