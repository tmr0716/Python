S = [0,1,2]
print("* |",end = " ")
for b in S:
  print(b,end = " ")
print("\n--+" + "-------")
for a in S:
  print(a,"|",end = " ")
  for b in S:
    ans = (a+b)%3
    print(ans,end = " ")
  print()
