import sys

n,m = map(int,sys.stdin.readline().split())
site_password=dict()
for _ in range(n):
    site,password = sys.stdin.readline().split()
    site_password[site] = password

for _ in range(m):
    site = sys.stdin.readline().rstrip()
    print(site_password[site])