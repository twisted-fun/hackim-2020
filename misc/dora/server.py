#!/usr/bin/python2 -u
import time, random, sys
ims = []
lines = []
with open("b64","r") as f:
    lines = f.read().split("\n")
for line in lines:
    ims.append(line.split("."))
print "Where's Dora? 1 for upper right, 2 for upper left, 3 for lower left, 4 for lower right"
time.sleep(1)
numlist = random.sample(range(800),800)
failed = False
for num in numlist:
    print ims[num][0]+"\n"
    sys.stdout.flush()
    ans = raw_input()
    if ans[0] == ims[num][1]:
        continue
    else:
        failed = True
        break
if failed == True:
    print "No flag for you"
else:
    print "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WspyOPE5GGF4wZoMQ3cYPeZGww1P3/mnYt6Dau+62LFN65Sfa4wVvA/f6xotX3TiczBC3zkudE5UZ/GKmm1TWb/Eh9Xgi6J/WvzwxmtYWdwBcB320enze1m0p3ODV8xnJ1vedpBt7+UOgd+l1/oOOEsRkBo/vOlajX7VZLz77o41WszAok15UcSFsIYDrUVeH0G9EiKK6RmWz9hJ8HM2VxKOX6CeRMvh1/FPtKPl32PhvgPWOQkbm6zQYNnu3BaOTQl7tcVIfvzprr1q9M9m6y0TOw/YHnVT7+3nwNDyR2tneNaGQX6YtrBh+03LuchhvucGOdk4vYBYxkdYucJe4LmybQukhCFvkHLClkaTphO1FNyFoLQNYUwNmEe7bU24Rcuj3mkKAYMqr/Lo5ObL7J0dati1IY6OzfKZzw9l7yFF+XbE5TSpaJ7XmcnrVlRX3WTQTv4qq1sO1I6Rx02CdBiHj9h4qciVDK8ZE8l9sakquKOlpC/y9599JI8K4Pd9d986k9Xo0HiyloK7EGi1tpi5KMbV11jObMSscbM5cU4hgdNbe96F+pN8DK2O/U0PAavNvBvygkusgZVeetJX0VUtWEDdaRxV2Jz7ofpNE2FcQKy9i0L68T2BCxnJowebLemy2rDNV7f1TO98uHfySx47Se4zaKM4tKNHf/PvpSckCs2BCSGH2A4Wi7ZjLl8uKfkmUYa6FD8LsBjoVSR+FXXzHv/zKQ03/ll54OxFmNbmpfJWvfvAuBR/P/7+XvteqO7KEwPitZkaS2XYeqKz4PBT8N+ef96LPytamk0KySG1sBRSSCGFFGgBU4VrfCrX4/dvnvbnhZZzsP2XmGf9/wYlzQF2AlbDtOrluA9waeaflkgKKf4zcE6E6UjQCZPgoYzDqdFxA6i1MIcYJgjdCk2eIUuZZmOh3Fn6T0v6u0JqYSmkkEIKKSQHzAepHlSRhr+r/HzAGEG3pwO+t2yl6D0GY/W6+KuVBqqv4rO2p1suUBoWOfAmqMvuO+ffC7BA5AXtI4v+KvAkCbY/OxzRPItqxljUvaTjf588vxoUmCovBVM9iyJXN986Sz9gSnuYoh89ieau9HzAGP57m4NbJ7EWmTyaNr9rT0lAQSrxxq9vyV+tx//7LCyFFFJIIUX/4URlMEL3enk25zSpIsjpzJHGRNGj0kQdKaSQQgoppJBCCimk+K+CNFFHCimkkEIKKaSQQgop/qvwPxiKNVBQV2GxAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIwLTAxLTE2VDExOjMzOjEzKzA1OjAw95lLzQAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMC0wMS0xNlQxMTozMzoxMyswNTowMIbE83EAAABLdEVYdGxhYmVsAGhhY2tpbTIwe3N3aXBlcl9ub19zd2lwaW5nX3RoZV9mbGFnXzFmNTQ1YTZkNDliZDZkYzgxNWRkZDczMWQwYzJhMmFkfW7JK6YAAAAASUVORK5CYII="

