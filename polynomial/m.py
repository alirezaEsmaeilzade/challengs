import io
import matplotlib.pyplot as plt
import numpy as np
import base64



def cal(A1, B1, C1, D1, A2, B2, C2, D2):
    a1 = int(A1)
    b1 = int(B1)
    c1 = int(C1)
    d1 = int(D1)
    a2 = int(A2)
    b2 = int(B2)
    c2 = int(C2)
    d2 = int(D2)
    p1 = np.poly1d([a1, b1, c1, d1])
    p2 = np.poly1d([a2, b2, c2, d2])
    x1 = np.arange(0, 100, 0.1)
    x2 = np.arange(0, 100, 0.1)
    y1 = p1(x1)
    y2 = p2(x2)
    plt.title('polynomial') 
    plt.plot(x1,y1, 'b', label=f'y=({a1})(x^3)+({b1})(x^2)+({c1})(x)+({d1})')
    plt.plot(x2,y2, 'c', label=f'y=({a2})(x^3)+({b2})(x^2)+({c2})(x)+({d2})')
    plt.legend(loc='best')
    plt.xlim([0, 100]) 
    plt.ylim([0, 100])  
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return f'data:image/png;base64,{plot_url}'

#cal(10, 1, 3, 4, 1, 2, 3, 4)