from cylib import particle

a = particle.Point(0.0, 0.0)
b = particle.Point(3, 4)
c = particle.norm(b)
print(a.x, a.y)
print(b.x, b.y, c)
