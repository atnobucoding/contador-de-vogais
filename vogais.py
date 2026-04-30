# contador de vogais - sem frescura

def contar_vogais(texto):
    texto = texto.lower()
    
    vogais = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }
    
    for letra in texto:
        if letra in vogais:
            vogais[letra] += 1
    
    return vogais

def main():
    print("=== CONTADOR DE VOGAIS ===")
    print("digita uma frase e eu conto as vogais")
    
    frase = input("\n> ")
    
    if len(frase.strip()) == 0:
        print("ta de sacanagem? digita alguma coisa")
        return
    
    resultado = contar_vogais(frase)
    
    print("\n" + "-"*30)
    total = 0
    for vogal, contagem in resultado.items():
        print(f"{vogal.upper()}: {contagem}")
        total += contagem
    
    print("-"*30)
    print(f"TOTAL de vogais: {total}")
    
    if total == 0:
        print("cade as vogal cara?")
    elif total > 20:
        print("muita vogal. ta escrevendo musica?")

if __name__ == "__main__":
    main()
