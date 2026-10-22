import matplotlib.pyplot as plt

# Битовые маски для кодов (Outcodes)
INSIDE = 0  # 0000
LEFT   = 1  # 0001
RIGHT  = 2  # 0010
BOTTOM = 4  # 0100
TOP    = 8  # 1000

def compute_outcode(x, y, xmin, ymin, xmax, ymax):
    """Вычисляет код области (Outcode) для точки"""
    code = INSIDE
    if x < xmin:   code |= LEFT
    elif x > xmax: code |= RIGHT
    if y < ymin:   code |= BOTTOM
    elif y > ymax: code |= TOP
    return code

def bisection_intersection(p1, p2, xmin, ymin, xmax, ymax, eps=1e-5):
    """
    Метод половинного деления для поиска точки пересечения 
    отрезка p1-p2 с одной из границ окна.
    Ищет точку, где меняется код Outcode.
    """
    x1, y1 = p1
    x2, y2 = p2
    c1 = compute_outcode(x1, y1, xmin, ymin, xmax, ymax)
    c2 = compute_outcode(x2, y2, xmin, ymin, xmax, ymax)

    while eps < abs(x2 - x1) or eps < abs(y2 - y1):
        xm = (x1 + x2) / 2.0
        ym = (y1 + y2) / 2.0
        cm = compute_outcode(xm, ym, xmin, ymin, xmax, ymax)

        if cm == INSIDE:
            x2, y2, c2 = xm, ym, cm
        elif cm == c1:
            x1, y1, c1 = xm, ym, cm
        else:
            x2, y2, c2 = xm, ym, cm

    return (x1 + x2) / 2.0, (y1 + y2) / 2.0


if __name__ == "__main__":
    # Задаем окно отсечения
    xmin, ymin = 2, 2
    xmax, ymax = 8, 7

    # Задаем отрезки для тестирования
    segments = [
        ((1, 1), (9, 8)),    # Пересекает окно
        ((3, 3), (7, 6)),    # Полностью внутри
        ((0, 0), (1, 1)),    # Полностью снаружи
        ((0, 5), (10, 5)),   # Проходит насквозь
        ((5, 0), (5, 10))    # Вертикальный насквозь
    ]

    fig, ax = plt.subplots(figsize=(8, 8))
    
    rect = plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, 
                         fill=False, edgecolor='red', linewidth=2, linestyle='--')
    ax.add_patch(rect)

    for i, (p1, p2) in enumerate(segments):
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'gray', linestyle=':', alpha=0.5)
            
        ax.scatter([p1[0], p2[0]], [p1[1], p2[1]], color='black', s=30)

    ax.set_xlim(-1, 11)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 11)
    ax.set_aspect('equal')
    ax.grid(True)
    plt.show()
