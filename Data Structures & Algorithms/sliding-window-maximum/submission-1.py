class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self._build(data, 1, 0, self.n - 1)
    
    def _build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            self._build(data, 2*node, start, mid)
            self._build(data, 2*node+1, mid+1, end)
            
            # Hijo izquierdo mayor o igual que el hijo derecho
            if self.tree[2*node] >= self.tree[2*node+1]:
                self.tree[node] = self.tree[2*node]
            # Caso contrario
            else:
                self.tree[node] = self.tree[2*node+1]
    def query(self, l, r, node=1, start=0, end=None):
        if end==None:
            end = self.n - 1
        if end < l or start>r:
            return float('-inf')
        elif l<=start and end<=r:
            return self.tree[node]
        else:
            mid = (start + end) // 2
            p1 = self.query(l, r, 2*node, start, mid) 
            p2 = self.query(l, r, 2*node+1, mid + 1, end)
            
            if p1 >= p2:
                return p1
            else:
                return p2


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        
        st = SegmentTree(nums)
        result = []
        
        # El rango l va desde el inicio hasta donde quepa una ventana de tamaño k
        for l in range(len(nums) - k + 1):
            # Consultamos el máximo desde el índice l hasta l + k - 1
            maximum = st.query(l, l + k - 1)
            result.append(maximum)
            
        return result