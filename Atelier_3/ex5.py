# Décorateur pour logger l'exécution d'une fonction
def log_execution(func):
    def info(*args, **kwargs):
        with open("log.txt", "a") as log_file:
            log_file.write(f"Fonction '{func.__name__}' exécutée avec les arguments : {args}, {kwargs}\n")
        return func(*args, **kwargs)
    return info

# Fonction qui additionne deux nombres en utilisant un lambda, décorée par log_execution
@log_execution
def addition_lambda(a, b):
    add = lambda x, y: x + y  # Lambda pour additionner
    return add(a, b)

# Test de la fonction
resultat = addition_lambda(3, 9)
print(f"Résultat : {resultat}")