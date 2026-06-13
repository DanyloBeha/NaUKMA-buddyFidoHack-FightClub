N = int(input())

a, b, c = [n for n in reversed(range(1,N+1))], [], []

# alg
while c != [list(reversed(range(1, N+1)))]:
    disk = a.pop()
    print(f"Move disk {disk} from A to C")
    c.append(disk)

    disk = a.pop()
    print(f"Move disk {disk} from A to B")
    b.append(disk)


    disk = c.pop()
    print(f"Move disk {disk} from C to B")
    b.append(disk)


    disk = a.pop()
    print(f"Move disk {disk} from A to C")
    c.append(disk)


    disk = b.pop()
    print(f"Move disk {disk} from B to A")
    a.append(disk)


    disk = b.pop()
    print(f"Move disk {disk} from B to C")
    c.append(disk)


    disk = a.pop()
    print(f"Move disk {disk} from A to C")
    c.append(disk)
    print(c)
    print(list(reversed(range(1, N+1))))

# FAIL