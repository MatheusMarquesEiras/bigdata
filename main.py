texto = "Olá, mundo!"
sub = "mundo"

def get_position(text: str, sub: str):
    begin = text.find(sub)
    end = begin + len(sub)

    return begin, end

inicio, fim = get_position(text=texto, sub=sub)

print(f"Substring começa em {inicio} e termina em {fim}")
# Saída: Substring começa em 5 e termina em 10
