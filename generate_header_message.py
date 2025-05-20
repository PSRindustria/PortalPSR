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
    aniversariantes_path = os.path.join(diretorio, 'upload', 'aniversariantes.json')
    ferias_path = os.path.join(diretorio, 'upload', 'ferias.json')
    feriados_path = os.path.join(diretorio, 'upload', 'feriados.json')
    header_message_path = os.path.join(diretorio, 'upload', 'header_message.html')
    
    # Data atual
    hoje = datetime.datetime.now()
    dia_atual = hoje.day
    mes_atual = hoje.month
    data_atual_str = f"{dia_atual:02d}/{mes_atual:02d}"
    data_completa = hoje.strftime("%d/%m/%Y")
    
    # Mensagem padrão
    mensagem = "Aqui é o seu espaço. Aqui é PSR!"
    
    # Verificar retorno de férias (prioridade máxima)
    try:
        with open(ferias_path, 'r', encoding='utf-8') as f:
            ferias_data = json.load(f)
            
        for ferias in ferias_data:
            if ferias['retorno'] == data_completa:
                nome = ferias['colaborador']
                genero = determinar_genero(nome)
                pronome = "ela" if genero == "feminino" else "ele"
                mensagem = f"Hoje, {nome} volta de férias. Dê as boas-vindas a {pronome}!"
                # Encontrou retorno de férias, não precisa verificar outros eventos
                break
    except Exception as e:
        print(f"Erro ao processar arquivo de férias: {e}")
    
    # Se não encontrou retorno de férias, verifica aniversariantes
    if mensagem == "Aqui é o seu espaço. Aqui é PSR!":
        try:
            with open(aniversariantes_path, 'r', encoding='utf-8') as f:
                aniversariantes_data = json.load(f)
                
            for aniversariante in aniversariantes_data:
                if aniversariante['data'] == data_atual_str:
                    nome = aniversariante['nome']
                    genero = determinar_genero(nome)
                    pronome = "ela" if genero == "feminino" else "ele"
                    mensagem = f"Hoje é aniversário do {nome}, dê os parabéns para {pronome}!"
                    # Encontrou aniversariante, não precisa verificar feriados
                    break
        except Exception as e:
            print(f"Erro ao processar arquivo de aniversariantes: {e}")
    
    # Se não encontrou retorno de férias nem aniversariante, verifica feriados
    if mensagem == "Aqui é o seu espaço. Aqui é PSR!":
        try:
            with open(feriados_path, 'r', encoding='utf-8') as f:
                feriados_data = json.load(f)
                
            for feriado in feriados_data:
                if feriado['data'] == data_atual_str:
                    nome_feriado = feriado['nome']
                    mensagem = f"Hoje é {nome_feriado}. Bom feriado!"
                    break
        except Exception as e:
            print(f"Erro ao processar arquivo de feriados: {e}")
    
    # Escrever a mensagem no arquivo header_message.html
    try:
        with open(header_message_path, 'w', encoding='utf-8') as f:
            f.write(mensagem)
        print(f"Mensagem do dia gerada com sucesso: {mensagem}")
    except Exception as e:
        print(f"Erro ao escrever arquivo header_message.html: {e}")

if __name__ == "__main__":
    main()
