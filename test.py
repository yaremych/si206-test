def fab(num):
  if (num == 1 or num == 2):
    return 1
  return (fab(num - 1) + fab(num - 2))

print(fab(1))
print(fab(2))
print(fab(3))
print(fab(4))
print(fab(5))
print(fab(6))

print("I love coffee")