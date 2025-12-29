import numpy as np

# -------------------------------------------------------------
# Συνάρτηση που βρίσκει τη μεγαλύτερη αυξανόμενη διαδρομή
# -------------------------------------------------------------
def longestIncreasingPath(matrix):
    if matrix.size == 0:
        return 0, []

    m, n = matrix.shape
    memo = np.zeros((m, n), dtype=int)
    path_memo = [[None] * n for _ in range(m)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # ---------------------------------------------------------
    # Αναδρομική DFS που επιστρέφει ΜΗΚΟΣ και ΔΙΑΔΡΟΜΗ
    # ---------------------------------------------------------
    def dfs(i, j):
        if memo[i, j] != 0:
            return memo[i, j], path_memo[i][j]

        max_len = 1
        best_path = [(i, j)]

        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < m and 0 <= y < n and matrix[x, y] > matrix[i, j]:
                length, path = dfs(x, y)
                if 1 + length > max_len:
                    max_len = 1 + length
                    best_path = [(i, j)] + path

        memo[i, j] = max_len
        path_memo[i][j] = best_path
        return max_len, best_path

    # ---------------------------------------------------------
    # Εύρεση της μεγαλύτερης διαδρομής σε όλο τον πίνακα
    # ---------------------------------------------------------
    longest_path = 0
    best_full_path = []
    for i in range(m):
        for j in range(n):
            length, path = dfs(i, j)
            if length > longest_path:
                longest_path = length
                best_full_path = path

    return longest_path, best_full_path


# -------------------------------------------------------------
# ΚΥΡΙΟ ΠΡΟΓΡΑΜΜΑ
# -------------------------------------------------------------

# Ζήτα τις διαστάσεις
m = int(input("Δώσε αριθμό γραμμών: "))
n = int(input("Δώσε αριθμό στηλών: "))

# Δημιουργία τυχαίου πίνακα
matrix = np.random.randint(0, 100, size=(m, n))

# Εμφάνιση πίνακα
print("\nΟ πίνακας είναι:")
print(matrix)

# Υπολογισμός μεγαλύτερης αυξανόμενης διαδρομής
length, path = longestIncreasingPath(matrix)

# Εμφάνιση αποτελεσμάτων
print("\n📈 Μεγαλύτερη αυξανόμενη διαδρομή:")
for (i, j) in path:
    print(f"({i}, {j}) -> τιμή {matrix[i, j]}")

print("\n➡️ Μήκος διαδρομής:", length)