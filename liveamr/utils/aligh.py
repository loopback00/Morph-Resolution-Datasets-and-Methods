import numpy as np

# Constantes para la matriz de punteros (backtracking)
DIAGONAL = 0
UP = 1
LEFT = 2

class ChineseTextAlignment:
    """
    Implementa el algoritmo de alineamiento de secuencias descrito en el paper "CMRight",
    basado en el algoritmo de Needleman-Wunsch.

    Este algoritmo alinea dos secuencias de texto (una con morphs y otra correcta)
    para generar datos de entrenamiento para un modelo posterior.

    Atributos:
        match_score (int): Puntuación por una coincidencia de caracteres.
        mismatch_score (int): Puntuación por una no coincidencia de caracteres.
        gap_penalty (int): Penalización por un hueco en el alineamiento.
    """
    def __init__(self, match_score=10, mismatch_score=0, gap_penalty=-5):
        """
        Inicializa el alineador con los parámetros de puntuación.

        Args:
            match_score (int): Puntuación si los caracteres son iguales.
                               El paper usa 10.
            mismatch_score (int): Puntuación si los caracteres son diferentes.
                                  El paper usa 0.
            gap_penalty (int): Penalización por insertar un hueco. El paper es
                               inconsistente, pero un valor negativo como -5
                               es necesario para un funcionamiento correcto.
        """
        self.match_score = match_score
        self.mismatch_score = mismatch_score
        self.gap_penalty = gap_penalty

    def _get_char_score(self, char1, char2):
        """Calcula la puntuación de sustitución entre dos caracteres."""
        if char1 == char2:
            return self.match_score
        return self.mismatch_score

    def align(self, seq1, seq2):
        """
        Alinea dos secuencias de texto utilizando el algoritmo de Needleman-Wunsch.

        Args:
            seq1 (str): La primera secuencia (ej. texto con morphs, M en el paper).
            seq2 (str): La segunda secuencia (ej. texto correcto, L en el paper).

        Returns:
            tuple[str, str]: Un tuple conteniendo las dos secuencias alineadas.
            int: La puntuación final del alineamiento.
        """
        n = len(seq2) + 1
        m = len(seq1) + 1

        # 1. Creación e Inicialización de Matrices
        # Matriz para almacenar las puntuaciones
        score_matrix = np.zeros((n, m))
        # Matriz para almacenar los punteros para el backtracking
        pointer_matrix = np.zeros((n, m), dtype=int)

        # Rellenar la primera fila y columna
        for i in range(1, n):
            score_matrix[i, 0] = i * self.gap_penalty
            pointer_matrix[i, 0] = UP
        for j in range(1, m):
            score_matrix[0, j] = j * self.gap_penalty
            pointer_matrix[0, j] = LEFT

        # 2. Propagación de la Matriz (Relleno)
        for i in range(1, n):
            for j in range(1, m):
                # Calcular las puntuaciones de las 3 posibles procedencias
                score_diag = score_matrix[i - 1, j - 1] + self._get_char_score(seq2[i - 1], seq1[j - 1])
                score_up = score_matrix[i - 1, j] + self.gap_penalty
                score_left = score_matrix[i, j - 1] + self.gap_penalty

                # Encontrar la puntuación máxima y establecer el puntero.
                # Se da prioridad a la diagonal para seguir la lógica del paper.
                if score_diag >= score_up and score_diag >= score_left:
                    score_matrix[i, j] = score_diag
                    pointer_matrix[i, j] = DIAGONAL
                elif score_up >= score_left:
                    score_matrix[i, j] = score_up
                    pointer_matrix[i, j] = UP
                else:
                    score_matrix[i, j] = score_left
                    pointer_matrix[i, j] = LEFT

        # 3. Backtracking (Trazado inverso)
        aligned_seq1 = ""
        aligned_seq2 = ""
        i, j = n - 1, m - 1

        while i > 0 or j > 0:
            if pointer_matrix[i, j] == DIAGONAL:
                aligned_seq1 += seq1[j - 1]
                aligned_seq2 += seq2[i - 1]
                i -= 1
                j -= 1
            elif pointer_matrix[i, j] == UP:
                aligned_seq1 += "-"  # Gap en seq1
                aligned_seq2 += seq2[i - 1]
                i -= 1
            else: # LEFT
                aligned_seq1 += seq1[j - 1]
                aligned_seq2 += "-"  # Gap en seq2
                j -= 1
        
        # Las secuencias se construyen al revés, así que las invertimos
        final_score = score_matrix[n - 1, m - 1]
        
        return aligned_seq1[::-1], aligned_seq2[::-1], int(final_score)

# --- Ejemplo de Uso ---

# Instanciar el alineador con los parámetros del paper (y un gap_penalty funcional)
aligner = ChineseTextAlignment(match_score=10, mismatch_score=0, gap_penalty=-5)

# Ejemplo 1: De la Figura 5 del paper
# El paper alinea "最薪福楸" con "最新福利".
# '薪' y '新' son homófonos, '楸' y '利' no.
seq1_fig5 = "最薪福楸"
seq2_fig5 = "最新福利"

aligned1, aligned2, score = aligner.align(seq1_fig5, seq2_fig5)

print("--- Ejemplo 1 (De la Figura 5) ---")
print(f"Secuencia 1 (Morph): {seq1_fig5}")
print(f"Secuencia 2 (Label): {seq2_fig5}")
print("-" * 20)
print(f"Alineamiento 1: {aligned1}")
print(f"Alineamiento 2: {aligned2}")
print(f"Puntuación Final: {score}\n")


# Ejemplo 2: De la Tabla 9, Caso 2
# El algoritmo alinea a nivel de carácter. No convierte '木其' a '棋'.
# Su objetivo es producir: (木,-), (其,棋), (排,牌)
seq1_case2 = "万乐木其排"
seq2_case2 = "万乐棋牌"

aligned1, aligned2, score = aligner.align(seq1_case2, seq2_case2)

print("--- Ejemplo 2 (De la Tabla 9, Caso 2) ---")
print(f"Secuencia 1 (Morph): {seq1_case2}")
print(f"Secuencia 2 (Label): {seq2_case2}")
print("-" * 20)
print(f"Alineamiento 1: {aligned1}")
print(f"Alineamiento 2: {aligned2}")
print(f"Puntuación Final: {score}\n")

# Ejemplo 3: Con inserciones/eliminaciones
seq1_insert = "注【册】有礼"
seq2_insert = "注册有礼"

aligned1, aligned2, score = aligner.align(seq1_insert, seq2_insert)

print("--- Ejemplo 3 (Con inserción de símbolos) ---")
print(f"Secuencia 1 (Morph): {seq1_insert}")
print(f"Secuencia 2 (Label): {seq2_insert}")
print("-" * 20)
print(f"Alineamiento 1: {aligned1}")
print(f"Alineamiento 2: {aligned2}")
print(f"Puntuación Final: {score}\n")