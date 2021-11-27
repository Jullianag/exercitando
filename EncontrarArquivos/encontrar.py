import os

print('-' * 33)
print('Vamos ver se você me encontrar!!!')
print('-' * 33)
print()
caminho_procura = input('Digite o caminho do arquivo a procurar: ')
termo_procura = input('Digite algo do arquivo: ')


def tamanho_formatado(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4

    if tamanho < kilo:
        texto = 'Byte'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'KB'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'MB'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'GB'
    else:
        tamanho /= tera
        texto = 'TB'

    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'


conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print('Encontrei o arquivo: ', arquivo)
                print('Caminho: ', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extensão: ', ext_arquivo)
                print('Tamanho: ', tamanho)
                print('Tamanho formatado: ', tamanho_formatado(tamanho))
            except PermissionError as e:
                print('Sem permissão para acessar o arquivo!')
            except FileNotFoundError as e:
                print('O arquivo não foi encontrado!')
            except Exception as e:
                print('Erro desconhecido!', e)

print()
print(f'{conta} arquivo(s) encontrado(s).')