class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        # First simulate gravity (stones fall right), then rotate 90 degrees clockwise
        # Time: O(m*n), Space: O(m*n)
        
        m, n = len(box), len(box[0])
        
        # Simulate gravity for each row (stones fall right)
        for row in box:
            empty = n - 1  # rightmost empty position
            for col in range(n - 1, -1, -1):
                if row[col] == '*':  # obstacle
                    empty = col - 1
                elif row[col] == '#':  # stone
                    row[col], row[empty] = '.', '#'
                    empty -= 1
        
        # Rotate 90 degrees clockwise
        # (i, j) -> (j, m-1-i)
        result = [['' for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                result[j][m-1-i] = box[i][j]
        
        return result