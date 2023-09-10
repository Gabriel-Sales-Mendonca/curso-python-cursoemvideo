palavras = ('Metamask', 'Ledger', 'Trezor', 'Ethereum', 'Bitcoin', 'Defi', 'NFT')
for palavra in palavras:
    print(f'\nA palavra {palavra} tem ', end=' ')
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
