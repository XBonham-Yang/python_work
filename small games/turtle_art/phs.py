import colorgram
import turtle as t
import random
#get all the colours out
colors = colorgram.extract('phs.png', 10)

c_list = []
for c in colors:
     r = c.rgb.r
     g = c.rgb.g
     b = c.rgb.b
     rgb = (r,g,b)
     c_list.append(rgb)

print(c_list)