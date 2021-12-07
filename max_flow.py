import math


def get_max_vertex(k, g, s):
    m = 0
    v = -1
    for i, w in enumerate(g[k]):
        if i in s:
            continue

        if w[2] == 1:
            if m < w[0]:
                m = w[0]
                v = i
        else:
            if m < w[1]:
                m = w[1]
                v = i

    return v


def get_max_flow(m):
    w = [x[0] for x in m]
    return min(*w)


def update_graph(g, m, f):
    for t in m:
        if t[1] == -1:
            continue

        sgn = g[t[2]][t[1]][2]
        g[t[1]][t[2]][0] -= f * sgn
        g[t[1]][t[2]][1] += f * sgn

        g[t[2]][t[1]][0] -= f * sgn
        g[t[2]][t[1]][1] += f * sgn


def ford_fulkerson():
    init = 0
    end = 4
    m_init = (math.inf, -1, init)
    f = []

    j = init
    while j != -1:
        k = init
        m = [m_init]
        s = {init}

        while k != end:
            j = get_max_vertex(k, graph, s)
            if j == -1:
                if k == init:
                    break
                else:
                    k = m.pop()[2]
                    continue

            c = graph[k][j][0] if graph[k][j][2] == 1 else graph[k][j][1]
            m.append((c, j, k))
            s.add(j)

            if j == end:
                f.append(get_max_flow(m))
                update_graph(graph, m, f[-1])
                break

            k = j
    return sum(f)
