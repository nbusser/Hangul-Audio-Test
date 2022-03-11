import random

N_CHOSUNG = 19
N_JUNGSUNG = 21
N_JONGSUNG = 28

def get_random_hangul():
    chosung = random.randint(0, N_CHOSUNG-1)
    jungsung = random.randint(0, N_JUNGSUNG-1)
    jongsung = 0 if random.randint(0, 2) else random.randint(0, N_JONGSUNG-1)

    hangul = 0xAC00 + chosung * (N_JUNGSUNG * N_JONGSUNG) + jungsung * N_JONGSUNG + jongsung
    return chr(hangul)
