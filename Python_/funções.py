"""
Um subprograma é uma abstração de processo, encapsulada, reutilizável, que
geralmente tem um nome e pode ser parametrizável.

Subprograma[definição pessoal]
"""

"""
Um subprograma é uma:

-abstração de processo(uma lista de passos)
-encapsulada(com sua lógica isolada)
-reutilizável(pode ser chamada diversas vezes)
-que geralmente tem um nome e
-pode ser parametrizável.
"""
#nome
def extract_audio(
      video_file: str, output_file: str, eq: bool = True
) -> Path | tuple[Path, ...]:
    
    audio: AudioSegment = AudioSegment.from_file(video_file)
    audio.export(output_file, format='wav')
    
    if eq:
        logger.info(f'-eq enabled')
        process_audio(output_file, 'eq_' + output_file)
        return Path(output_file), Path('eq_' + output_file)

    return Path(output_file)

path_1 = extract_audio('video_1.mp4', 'result_1.wav', eq=False)
path_2 = extract_audio('video_2.mp4', 'result_2.wav', eq=False)
path_3 = extract_audio('video_3.mp4', 'result_3.wav', eq=False)
path_4, path_eq_4 = extract_audio('video_4.mp4', 'result_4.wav', eq=True)


"""Tipos de Programas"""
# 1- Procedimentos [procedures]: Não retornam valores
# 2- Funções: Retornam valores.

def enviar_email(remetente, destinatário, assunto, corpo):
    mensagem = f"""
    subject: {assunto} {corpo}"""

    with smtplib.SMTP_SSL(servidor, porta, contexto) as servidor:
        server.login(remetente, senha)
        server.sendemail(remetente, destinatário, mensagem)


"""
Função:
    # Já a função se baseia somente no estado dos parâmetros recebidos via argumentos durante a chamada
        # Parâmetros: é o que eu defino na função. (o que define!)
        # Argumento: é o que eu passo quando eu chamo a função. (éo que tô recebendo!)
"""

"""
Efeitos colaterais: 
    Dizemos que quando um subprograma altera variáveis [estado] fora do
    seu escopo interno ele gera um efeito colateral na aplicação!
"""
lista = []
def aumenta_lista(val):
    lista.append(val)

aumenta_lista(1)
lista[1]

aumenta_lista(2)
lista[1, 2]