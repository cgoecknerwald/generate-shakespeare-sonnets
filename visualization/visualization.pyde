def load_dict(s):
    lines = loadStrings(s)
    d = {}
    for pair in lines:
        if not pair.strip():
            continue
        k, v = map(str, pair.split())
        if k.isdigit():
            k = int(k)
        if v.isdigit():
            v = int(v)
        d[k] = v
    return d

def load_array(s):
    lines = loadStrings(s)
    lst = []
    for line in lines:
        lst.append(map(float, line.split()))
    return lst

from math import sin, cos, pi
    
def transition(A, a, b, control):
    ''' from a to b '''
    if a == b:
        control *= -0.5
    c_rad = 300
    prob = A[a][b]
    stroke(map(a, 0, len(A), 0, 255), 200, 255, map(prob, 0, 1, 35, 255))
    # stroke(map(prob, 0, 1, 35, 255))
    noFill()
    
    rad1 = 2 * pi * a/len(A)
    rad2 = 2 * pi * b/len(A)
    rad3 = 2 * pi * (b-2)/len(A)
    rad4 = 2 * pi * (a+2)/len(A)
    p1 = c_rad * cos(rad1), c_rad * sin(rad1)
    p2 = c_rad * cos(rad2), c_rad * sin(rad2)
    e1 = c_rad * cos(rad3), c_rad * sin(rad3)
    e2 = c_rad * cos(rad4), c_rad * sin(rad4)    
    c1 = map(control, 0, 1, p1[0], e1[0]), map(control, 0, 1, p1[1], e1[1])
    c2 = map(control, 0, 1, p2[0], e2[0]), map(control, 0, 1, p2[1], e2[1])
    
    bezier(p1[0], p1[1], c1[0], c1[1], c2[0], c2[1], p2[0], p2[1])

def setup():
    size(1100, 1100)
    colorMode(HSB, 255)
    ellipseMode(CENTER)
    textAlign(CENTER)
    textFont(createFont("Courier Regular",16))
    textSize(25)

    strokeWeight(5)
    
control = 0.5
def draw():
    background(35)
    textSize(25)
    translate(width/2, height/2 - 100)
    A = load_array('A.txt')
    O = load_array('O.txt')
    word_map = load_dict('word_map.txt')
    
    c_rad = 300
    s = 50
    l = []
    for a in range(len(A)):
        for b in range(len(A)):
            l.append((A[a][b], a, b))
    
    l.sort(key=lambda x: x[0])
    for _, a, b in l:
        transition(A, a, b, control)

    noStroke()
    fill(255)
    for state in range(len(A)):
        rad = 2 * pi * state/len(A)
        x, y = c_rad * cos(rad), c_rad * sin(rad)
        fill(35)
        stroke(map(state, 0, len(A), 0, 255), 200, 255)
        ellipse(x, y, s, s)
        fill(255)
        text(str(state), x, y + 7)
        
    # Print words for each state.
    top = [[] for _ in range(len(A))]
    for word in range(len(O[0])):
        state = max(((s, O[s][word]) for s in range(len(A))), key=lambda x: x[1])[0]
        top[state].append((O[state][word], word_map[word]))
    
    for t in top:
        t.sort(reverse=True)
    fill(255)
    textSize(14)
    for state in range(len(A)):
        # top_words = map(lambda x: word_map[x[0]], sorted(enumerate(O[state]), reverse=True, key=lambda x: x[1])[:10])
        top_words = map(lambda x: x[1], top[state][:10])
        rad = 2 * pi * state/len(A)
        x, y = (c_rad + 150) * cos(rad), (c_rad + 150) * sin(rad)
        if state in (1, 5):
            x += 40
        if state in (2, 4):
            x -= 50
        if state in (1, 2):
            y -= 150
        if state in(0, 3):
            y -= 100
        text('\n'.join(top_words), x, y)
    
    noLoop()


    