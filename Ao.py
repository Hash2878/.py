M = 'D'
I = 'C'
H = 'B'
A = 'A'
L = 'AND'
F = 'OR'
E = len
D = print

def J(n):
    R = False
    I = True
    global X
    D('Expanding Node:', n)
    
    G = []
    H = []
    if n in B:
        if L in B[n]:
            G = B[n][L]
        if F in B[n]:
            H = B[n][F]
    
    if E(G) == 0 and E(H) == 0:
        return
    
    M = R
    Q = {}
    
    while not M:
        if E(G) == E(G) + E(H):
            S, T = O(G, H, Q)
            M = I
            P(n, S)
            C[n] = I
            continue
        
        V, A = O(G, H, Q)
        N = R
        if E(A) > 1:
            if A[0] in B:
                N = I
                J(A[0])
            if A[1] in B:
                N = I
                J(A[1])
        elif A in B:
            N = I
            J(A)
        
        if N:
            if A == W:
                M = I
                P(n, V)
                C[n] = A
            else:
                M = I
                P(n, V)
                C[n] = A
                Q[A] = 1
                return K(n)

def O(and_nodes, or_nodes, marked):
    G = marked
    for B in and_nodes:
        if not B[G][B[1]] in G:
            A = 0
            A = A + K(B[0]) + K(B[1]) + 2
            C[B[0]] = B[1] = A
    e = 999999
    H = None
    for F in or_nodes:
        if C[F] <= e:
            E = C[F]
            H = F
    return [E, H]

def K(n):
    return N[n]

def P(n, cost):
    N[n] = cost
    return

def G(node):
    B = '->'
    A = node
    D(C[A], end='')
    A = C[A]
    if E(str(A)) > 1:
        if A[0] in C:
            D(A[0], end='')
            G(A[0])
        if A[1] in C:
            D(A[1], end='')
            G(A[1])
    elif A in C:
        D(A, end='')
        G(A)
    else:
        D(B, end='')

N = {'A': -1, 'H': 4, 'I': 2, 'M': 3, 'E': 6, 'F': 8, 'G': 2, 'H': 0, 'I': 0, 'J': 0}
B = {'A': {L: ['I', 'M'], F: ['H']}, 'H': {F: ['E', 'F']}, 'I': {F: ['G'], L: ['H', 'I']}, 'M': {F: ['J']}}

C = {}
Q = J(A)
D("Nodes which give optimal cost are")
G(A)
D("\n optimal cost is:", Q)
