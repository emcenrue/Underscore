#  a, b = 1, 2
#  [c, d] = 3, 4
#  [e, (f, g)] = 5, [6, 7]
#  
#  print(a, b, c, d, e, f, g)

(________, _________, __________, ___________, ____________, _____________, ______________) = (1, 2, 3, 4, 5, 6, 7)
(_, __) = (________, _________)
[___, ____] = (__________, ___________)
[_____, (______, _______)] = (____________, [_____________, ______________])
print (_, __, ___, ____, _____, ______, _______)
(a, b, c, d, e, f, g) = (_, __, ___, ____, _____, ______, _______)