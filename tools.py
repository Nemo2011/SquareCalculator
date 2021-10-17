import sympy

def get_num(entry):
    str_num = entry.get()
    try:
        num = float(str_num)
        return num
    except:
        if str_num == 'oo':
            num = sympy.oo
            return num

def def_sym():
    a, b, c, d, e, f, g, h, i, j = sympy.symbols('a, b, c, d, e, f, g, h, i, j')
    k, l, m, n, o, p, q, r, s, t = sympy.symbols('k, l, m, n, o, p, q, r, s, t')
    u, v, w, x, y, z = sympy.symbols('u, v, w, x, y, z')

    A, B, C, D, E, F, G, H, I, J = sympy.symbols('A, B, C, D, E, F, G, H, I, J')
    K, L, M, N, O, P, Q, R, S, T = sympy.symbols('K, L, M, N, O, P, Q, R, S, T')
    U, V, W, X, Y, Z = sympy.symbols('U, V, W, X, Y, Z')

    alpha, beta, gamma, delta = sympy.symbols('alpha, beta, gamma, delta')
    epsilon, zeta, eta, theta = sympy.symbols('epsilon, zeta, eta, theta')
    iota, kappa, lamda, mu = sympy.symbols('iota, kappa, lamda, mu')
    nu, xi, omicron, pi = sympy.symbols('nu, xi, omicron, pi')
    rho, sigma, tau, upsilon = sympy.symbols('rho, sigma, tau, upsilon')
    phi, chi, psi, omega = sympy.symbols('phi, chi, psi, omega')