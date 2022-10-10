#Simple program that estimate Pi, given that you have random (0,1)
#These points would be generated using the random module and is called twice for each point
#once for the x-value and once for the y-value.
import random, math

def pi_estimation(num):
    "The more points user input, the more accurate value for pi"
    pt_circle = 0
    pt_total = 0
    for i in range(num):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        dist = math.sqrt(x**2 + y**2)
        if 1 >= dist:
            pt_circle += 1
        pt_total += 1
        
    return 4 * pt_circle/pt_total


