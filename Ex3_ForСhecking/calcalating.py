
import math
import dilog

def calc():
    d1, d2, h, VSand, n = dilog.ask()
    theta1 = 0;
    t_dict = {}
    for theta1 in range(90) :
        d1 = d1 * 3
        x = d1 * math.tan(theta1 * 0.0174533)
        h = h * 3;
        VSand = VSand * 1.46667
        L1 = math.sqrt(pow(x, 2) + pow(d1, 2))
        L2 = math.sqrt(pow((h - x), 2) + pow(d2, 2))
        t = 1 / VSand * (L1 + n * L2)
        # if target<=t:
        #     break
        # else:
        #     target=t 
        t_dict[theta1] = t
           
    min_t = min(t_dict.values())
    theta1_min_t = min(t_dict, key=t_dict.get)
        
        
    return min_t,theta1_min_t

    # def calc():
    #     d1, d2, h, VSand, n = dilog.ask()
    #     theta1 = 0;
    #     i = 0;
    #     t_dict = {}
        
    #     for i in range(90) :
    #         theta1 = i;
    #         d1 = d1 * 3
    #         x = d1 * math.tan(theta1 * 0.0174533)
    #         h = h * 3;
    #         VSand = VSand * 1.46667
    #         L1 = math.sqrt(pow(x, 2) + pow(d1, 2))
    #         L2 = math.sqrt(pow((h - x), 2) + pow(d2, 2))
    #         t = 1 / VSand * (L1 + n * L2)
    #         t_dict[i] = t
            
           
            
               
    #     # Находим минимальное значение t в словаре
    #     min_t = min(t_dict.values())
        
    #     # Находим ключ i, соответствующий минимальному значению t
    #     min_i = min(t_dict, key=t_dict.get)
        
        
    #     return min_t,min_i
        