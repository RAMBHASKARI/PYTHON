base=int(input("Enter length of Base : "))
perp=int(input("Enter length of Perpendicular : "))
hypo=int(input("Enter length of Hypotenuse : "))

if (base*base==perp*perp+hypo*hypo) or (perp*perp==base*base+hypo*hypo) or (hypo*hypo==base*base+perp*perp) :
    print("It's a right triangle")
else:
    print("It's not a right triangle")
    