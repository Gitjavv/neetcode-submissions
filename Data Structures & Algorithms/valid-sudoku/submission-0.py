from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def containsDuplicate(nums: List[int]) -> bool:
            return len(nums) != len(set(nums))

        # Estructura: cada número del 1-9 tiene sus índices de fila, col y sub-recuadro
        counter = defaultdict(lambda: {0: [], 1: [], 2: []})
        
        for i in range(9):
            for j in range(9):
                char = board[i][j]
                if char == ".":
                    continue
                
                num = int(char)
                subbox_index = 3 * (i // 3) + (j // 3)

                counter[num][0].append(i)            # Registra fila
                counter[num][1].append(j)            # Registra columna
                counter[num][2].append(subbox_index) # Registra sub-recuadro

        # Validamos cada número encontrado
        for data in counter.values():
            # data es el dict {0: [...], 1: [...], 2: [...]}
            if containsDuplicate(data[0]): return False
            if containsDuplicate(data[1]): return False
            if containsDuplicate(data[2]): return False
        
        return True
