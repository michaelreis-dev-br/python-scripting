import subprocess
from sys import argv, exit


def extracao_cdi():
    subprocess.run(['python3', 'extracao.py'], check=True)

def visualizacao(output_image):
    subprocess.run(['python3', 'visualizacao.py', output_image], check=True)

if __name__ == "__main__":
    if len(argv) < 2:
        print("Modo de uso: python analise.py <nome-do-grafico>")
        exit(1)

    output_image = f"{argv[1]}-explain"

    extracao_cdi()
    visualizacao(output_image)