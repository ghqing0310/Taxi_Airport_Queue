import matplotlib.pyplot as plt


def fare(s, night=False):
    if night:
        if s < 3:
            return 18
        elif s < 10:
            return 18 + (s - 3) * 3.1
        else:
            return 18 + 7 * 3.1 + 4.7 * (s - 10)
    else:
        if s < 3:
            return 14
        elif s < 10:
            return 14 + (s - 3) * 2.5
        else:
            return 14 + 7 * 2.5 + 3.6 * (s - 10)


tw = [340/120, 119/120, 1040/120, 670/120]
c = 0.56
v = 70
xa = 32.6
for i in range(4):
    xs1 = []
    xs2 = []
    for x in range(1, 61):
        xs1.append((fare(x)-c*x)/(tw[i]+x/v))
        xs2.append((fare(x)-2*c*x+fare(xa)-c*xa) / (2*tw[i]+(2*x+xa)/v))
    print(xs1)
    print(xs2)
    print('---')
    plt.plot(xs1)
    plt.plot(xs2)
    # plt.show()
print((fare(1)-2*c*1+fare(xa)-c*xa) / (2*tw[0]+(2*1+xa)/v))