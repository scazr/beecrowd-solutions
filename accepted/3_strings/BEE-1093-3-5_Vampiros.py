import math
while True:
    EV1, EV2, AT, D = map(int, input().split())
    if EV1 == 0 and EV2 == 0 and AT == 0 and D == 0: break

    pwin_EV1 = AT / 6
    pwin_EV2 = 1 - pwin_EV1

    n_EV1 = math.ceil(EV1 / D)
    n_EV2 = math.ceil(EV2 / D)
    
    ratio_q_p = pwin_EV2 / pwin_EV1
    
    if AT == 3:
        print(round(n_EV1 / (n_EV2 + n_EV1) * 100, 1))
    else:
        print(round((1 - ratio_q_p ** n_EV1) /( 1 - ratio_q_p ** (n_EV1 + n_EV2)) * 100, 1))