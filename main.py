import time

def Movimente(k, origem, destino):
    global movimentos
    # Recebe o disco k, sendo movimentado, e os dicionarios torre1 e torre2, que contém
    # o nome da torre e a lista de discos da torre.
    # Remove o disco da torre1 e o adiciona na torre2.
    if k not in origem["conteudo"]:
        print(f'Erro: Disco {k} não está na torre {origem["nome"]}.')
        exit(1)
    elif k in destino["conteudo"]:
        print(f'Erro: Disco {k} já está na torre {destino["nome"]}.')
        exit(1)
    elif origem["conteudo"][-1] != k:
        print(f'Erro: Disco {k} não está no topo da torre {origem["nome"]}.')
        exit(1)
    else:
        disco = origem["conteudo"].pop()
        destino["conteudo"].append(disco)
        movimentos += 1

def Mostre_Torres():
    # Acessa os dicionarios globais correspondentes a cada torre, que contém
    # o nome da torre e a lista de discos da torre.
    # Imprime os discos de cada torre, de cima para baixo.
    # Se a torre não tiver disco, imprime uma string vazia.
    # Utiliza um dicionário auxiliar para colorir as torres a fim de
    # facilitar a leitura humana do terminal.
    global torre_A, torre_B, torre_C
    n = max(len(torre_A["conteudo"]), len(torre_B["conteudo"]), len(torre_C["conteudo"]))
    colors = {
        'A': '\033[1;36m',  # Cyan
        'B': '\033[1;35m',  # Magenta
        'C': '\033[1;32m'   # Green
    }
    print()
    for i in range(n-1, -1, -1):
        for torre in [torre_A, torre_B, torre_C]:
            disco = torre["conteudo"][i] if i < len(torre["conteudo"]) else ''
            print(f'{colors[torre["nome"]]}{disco:^10}\033[0m', end='')
        print()
    for torre in [torre_A, torre_B, torre_C]:
        print(f'{colors[torre["nome"]]}{"torre " + torre["nome"]:^10}\033[0m', end='')
    print()

def Hanoi(n, torre1, torre2, torreAux):
    # Recebe o número de discos n, e os dicionarios 1, 2 e auxiliar, que contém
    # o nome da torre e a lista de discos de cada uma.
    # Resolve o problema das Torres de Hanoi, movendo os discos da torre 1 para a
    # torre 2, utilizando a torre auxiliar.
    # Se n == 1, move o disco da torre 1 para a torre 2.
    # Caso contrário, move o disco n-1 da torre 1 para a torre auxiliar; o disco n 
    # da torre 1 para a torre 2; e finalmente, o disco n-1 da torre auxiliar para a torre 2.
    # Registra o tempo de execução do algoritmo para fins de análise de eficiência.
    # Imprime os movimentos efetivamente realizados pela função e compara com o 
    # esperado para a solução conhecida ao problema das Torres.
    if n == 1:
        Movimente(n, torre1, torre2)
        Mostre_Torres()
    else:
        Hanoi(n-1, torre1, torreAux, torre2)
        Movimente(n, torre1, torre2)
        Mostre_Torres()
        Hanoi(n-1, torreAux, torre2, torre1)

def main():
    global torre_A, torre_B, torre_C, movimentos
    try:
        while True:
            try:
                n = int(input("Entre com o número de discos: "))
                if n <= 0:
                    print("Número inválido. Por favor, entre com um número maior que zero.")
                    continue
                
                start_time = time.time()
                
                torre_A = {'nome': 'A', 'conteudo': list(range(n, 0, -1))}
                torre_B = {'nome': 'B', 'conteudo': []}
                torre_C = {'nome': 'C', 'conteudo': []}
                movimentos = 0
                
                Mostre_Torres()
                Hanoi(n, torre_A, torre_B, torre_C)
                
                end_time = time.time()
                runtime = end_time - start_time
                
                print(f"\nNúmero de discos: {n}"
                      f"\nTempo de execução: {runtime:.4f} segundos"
                      f"\nNúmero de movimentos previsto: {2**n - 1}"
                      f"\nNúmero de movimentos realizados: {movimentos}\n")
                
            except ValueError:
                print("Entrada inválida. Por favor, entre com um número inteiro positivo.")
            except Exception as e:
                print(f'Erro: {e}')
                exit(1)
    except KeyboardInterrupt:
        print("\nCTRL+C Para sair")
        exit(0)

if __name__ == "__main__":
    main()
