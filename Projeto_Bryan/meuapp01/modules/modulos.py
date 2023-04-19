def modulos(url, *nomeJson):
    import requests
    f = requests.get(url)
    f = f.json()
    valor = []

    for c in range(0, len(f)):
        for r in nomeJson:
            valor.append(f[c] [r])

        return valor