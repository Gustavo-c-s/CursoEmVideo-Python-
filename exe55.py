gorda = 0
magra = 0
for pess in range(1,6):
    p1 = float(input('Kilo da  {}º pessoa? '.format(pess)))
    if pess == 1:
        gorda = p1
        magra = p1
    else:
        if p1 > gorda:
            gorda = p1
        if p1 < magra:
            magra = p1
print('o maior peso foi de {}kg;\ne o menor pesso foi {}kg'.format(gorda,magra))
