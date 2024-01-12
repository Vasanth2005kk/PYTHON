metal_cost=float(input())
tip_percent=int(input())
tax_percent=int(input())

tip=(metal_cost/100)*tip_percent
tax=(tax_percent/100)*metal_cost
total=metal_cost+tip+tax

print(round(total))