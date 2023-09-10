def maior(*num):
    num_ordenados = sorted(num)
    print(f'O maior valor é o {num_ordenados[-1]}')

maior(10, 15, 2, 21, 3, 100)