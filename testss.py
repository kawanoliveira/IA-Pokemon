import psutil
import os
import sys

def checar_memoria():
    processo = psutil.Process(os.getpid())
    memoria_usada = processo.memory_info().rss / (1024 ** 3)  # Converte para GB
    print(f"{memoria_usada:.2f} GB.")