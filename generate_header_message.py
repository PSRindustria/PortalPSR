#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import datetime
from unidecode import unidecode

# Função para determinar o gênero com base no nome
def determinar_genero(nome):
    # Lista de nomes femininos comuns no Brasil
    nomes_femininos = [
        'ana', 'maria', 'fernanda', 'juliana', 'patricia', 'camila', 'mariana', 'luciana', 
        'bruna', 'vanessa', 'jessica', 'amanda', 'leticia', 'gabriela', 'julia', 'beatriz', 
        'larissa', 'natalia', 'manuela', 'isabela', 'rafaela', 'giovanna', 'carolina', 'luiza', 
        'vitoria', 'bianca', 'clara', 'laura', 'sophia', 'alice', 'helena', 'valentina', 
        'cecilia', 'lara', 'heloisa', 'melissa', 'eduarda', 'sarah', 'yasmin', 'isabelly', 
        'lavinia', 'esther', 'sophie', 'joana', 'livia', 'lorena', 'isis', 'elisa', 'antonella', 
        'maya', 'luana', 'mirella', 'emanuelly', 'rebeca', 'ana clara', 'ana julia', 'ana luiza', 
        'iasmim', 'monique', 'selma', 'simone', 'rogeria'
    ]
    
    # Pega o primeiro nome (caso tenha mais de um)
    primeiro_nome = nome.split()[0].lower()
    primeiro_nome = unidecode(primeiro_nome)  # Remove acentos
    
    # Verifica se termina com 'a' (comum em nomes femininos)
    if primeiro_nome.endswith('a') and primeiro_nome != 'joshua' and primeiro_nome != 'luca':
        return 'feminino'
    
    # Verifica se está na lista de nomes femininos
    if primeiro_nome in nomes_femininos:
        return 'feminino'
    
    # Caso contrário, assume masculino
    return 'masculino'

def main():
    # Diretório atual
    diretorio = os.path.dirname(os.path.abspath(__file__))
    
    # Caminhos dos arquivos
    aniversariantes_path = os.path.join(diretorio, 'aniversariantes.json')
    ferias_path = os.path.join(diretorio, 'ferias.json')
    feriados_path = os.path.join(diretorio, 'feriados.json')
    header_message_path = os.path.join(diretorio, 'header_message.html')
    
    # Data atual
    hoje = datetime.datetime.now()
    dia_atual = hoje.day
    mes_atual = hoje.month
    data_atual_str = f"{dia_atual:02d}/{mes_atual:02d}"
    data_completa = hoje.strftime("%d/%m/%Y")
    
    # Inicializa lista de mensagens
    mensagens = []
    
    # Verificar aniversariantes
    try:
        with open(aniversariantes_path, 'r', encoding='utf-8') as f:
            aniversariantes_data = json.load(f)
            
        for aniversariante in aniversariantes_data:
            if aniversariante['data'] == data_atual_str:
                nome = aniversariante['nome']
                genero = determinar_genero(nome)
                pronome = "ela" if genero == "feminino" else "ele"
                # Emoji de festa 🥳 para aniversariantes
                mensagens.append(f"🥳 Hoje é aniversário do {nome}, dê os parabéns para {pronome}!")
    except Exception as e:
        print(f"Erro ao processar arquivo de aniversariantes: {e}")
    
    # Verificar retorno de férias
    try:
        with open(ferias_path, 'r', encoding='utf-8') as f:
            ferias_data = json.load(f)
            
        for ferias in ferias_data:
            if ferias['retorno'] == data_completa:
                nome = ferias['colaborador']
                genero = determinar_genero(nome)
                pronome = "ela" if genero == "feminino" else "ele"
                # Adiciona emoji de avião chegando ✈️
                mensagens.append(f"✈️ Hoje, {nome} volta de férias. Dê as boas-vindas a {pronome}!")
    except Exception as e:
        print(f"Erro ao processar arquivo de férias: {e}")
    
    # Verificar feriados
    try:
        with open(feriados_path, 'r', encoding='utf-8') as f:
            feriados_data = json.load(f)
            
        for feriado in feriados_data:
            if feriado['data'] == data_atual_str:
                nome_feriado = feriado['nome']
                # Adiciona emoji de calendário 📅
                mensagens.append(f"📅 Hoje é {nome_feriado}. Bom feriado!")
    except Exception as e:
        print(f"Erro ao processar arquivo de feriados: {e}")
    
    # Combinar mensagens ou usar mensagem padrão
    if mensagens:
        # Juntar com quebras de linha HTML
        mensagem_final = "<br>".join(mensagens)
    else:
        mensagem_final = "Aqui é o seu espaço. Aqui é PSR!"
    
    # Escrever a mensagem no arquivo header_message.html
    try:
        with open(header_message_path, 'w', encoding='utf-8') as f:
            f.write(mensagem_final)
        print(f"Mensagem do dia gerada com sucesso: {mensagem_final}")
    except Exception as e:
        print(f"Erro ao escrever arquivo header_message.html: {e}")

if __name__ == "__main__":
    main()
