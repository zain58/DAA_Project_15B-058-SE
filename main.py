def invent_plan( n = [], m, c, D = [], d, h):
#let cost[1..n, 0..D] and make[1..n, 0..D] be new tables # Compute cost[n, 0..D] and make[n, 0..D]
 for s in range(len(D)):
        f = max(dn - s, 0)
        cost[n, s] = c * max(f - m, 0) + h(s + f - dn)
        make[n, s] = f
 U = dn
for k in range(len(n)):
   U = U + dk
   for s in range(len(D)):
     cost[k, s] = 0
     for f in range(max(dk - s, 0), U - s):
       val = cost[k + 1, s + f - dk] + c * max(f - m, 0) + h(s + f - dk)
       if val < cost[k, s]:
         cost[k, s] = val
         make[k, s] = f
         print(cost[1, 0])
         plan(make, n=[], d)
         return;
def plan(make, n=[], d):
  s = 0
  for k in range(len(n)):
    print("For month ", k ,"manufacture ", make[k, s], "machines")
    s = s + make[k, s] - dk
    return;