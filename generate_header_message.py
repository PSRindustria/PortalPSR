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
    'abigail', 'abriele', 'adriane', 'agnes', 'aitana', 'alana', 'alba', 'alessia',  
    'alexia', 'aliceia', 'alzira', 'amalia', 'ana paula', 'anais', 'angelica', 'angelina',  
    'antonia', 'anita', 'antonieta', 'ara', 'ariana', 'ariane', 'arlete', 'arlene',  
    'arminda', 'audrey', 'aurora', 'ayla', 'azilda', 'barbara', 'beatrice', 'bellamy',  
    'benedita', 'bernadete', 'bertina', 'bertha', 'betsy', 'biana', 'blendina', 'blenda',  
    'branda', 'brigitte', 'camille', 'candida', 'carmela', 'carminha', 'caroline', 'catarina',  
    'cecília', 'celia', 'celina', 'chantal', 'charlene', 'charlotte', 'christiane', 'cielete',  
    'cilene', 'clarice', 'claudete', 'claudiana', 'claudine', 'claudionora', 'clelia', 'cleusa',  
    'clotilde', 'clementina', 'cordelia', 'corina', 'cristal', 'cristela', 'crislaine', 'dadá',  
    'dagmar', 'dalila', 'dalva', 'damiana', 'danila', 'danisa', 'darcília', 'darlene',  
    'deadina', 'deise', 'dela', 'delia', 'demetria', 'denise', 'derci', 'desirée',  
    'diana', 'dilma', 'dinorah', 'dionísia', 'dirce', 'divina', 'dominica', 'domingas',  
    'doroteia', 'edi', 'edilene', 'edite', 'elaine', 'elba', 'elderina', 'eleonora',  
    'elfrida', 'elisabete', 'elisângela', 'eliza', 'elizabete', 'elma', 'elvira', 'ema',  
    'emília', 'ena', 'enede', 'ereia', 'erika', 'erise', 'erteca', 'erta',  
    'esmeralda', 'estela', 'estrela', 'eudoxia', 'eulália', 'eunice', 'eva', 'evangelina',  
    'everlúcia', 'exilda', 'fabiana', 'fátima', 'felicidade', 'fermina', 'fiama', 'flora',  
    'florinda', 'fortuna', 'francine', 'francisca', 'frida', 'gabrielle', 'gasparina', 'geneviève',  
    'genilda', 'geovana', 'geovana', 'geovana', 'gilda', 'gina', 'ginger', 'gislaine',  
    'gleice', 'glenda', 'glória', 'goretti', 'graciete', 'gracilene', 'guida', 'haidée',  
    'halina', 'hanae', 'hana', 'hanna', 'helle', 'helma', 'henriqueta', 'herminia',  
    'heveline', 'hilaria', 'hilda', 'homérica', 'hylda', 'ida', 'ileana', 'ilma',  
    'ilza', 'imelda', 'inês', 'iraci', 'irene', 'irislene', 'irlanda', 'ismaela',  
    'itaglêcia', 'ivanete', 'ivone', 'ivoneide', 'ivonilde', 'izabel', 'izabela', 'izildinha',  
    'jada', 'janete', 'janina', 'janine', 'jaqueline', 'jelena', 'jemima', 'jessiane',  
    'joana d’arc', 'jocasta', 'joelia', 'joenilda', 'jole', 'jonas', 'jorgeana', 'joselina',  
    'josiana', 'jovita', 'joyce', 'julia', 'junia', 'justina', 'karine', 'karla',  
    'karol', 'katia', 'kátia', 'kely', 'keyla', 'kimberly', 'kissia', 'kristina',  
    'laraine', 'larissa', 'lau', 'lauraine', 'lea', 'lebina', 'leila', 'leina',  
    'lemara', 'lendite', 'leonor', 'lepida', 'lesbia', 'letícia', 'levina', 'liana',  
    'lidia', 'lidiane', 'liliane', 'lilisa', 'lilja', 'linda', 'linet', 'lionê',  
    'liora', 'lisandra', 'lissa', 'lita', 'lizabeth', 'lorena', 'lorene', 'lority',  
    'lourdes', 'lucia', 'lucinda', 'ludmila', 'luene', 'luise', 'luiza', 'lumena',  
    'luzia', 'lygia', 'lys', 'madalena', 'mafalda', 'maisa', 'malu', 'marcela',  
    'marcelina', 'marcilene', 'marcia', 'marcosina', 'margarida', 'marina', 'maristela', 'marli',  
    'marlene', 'marlise', 'marlita', 'marly', 'maroma', 'marquita', 'marry', 'matilde',  
    'maureen', 'mayana', 'mayumi', 'melina', 'melissa', 'melodia', 'mercedes', 'mirela',  
    'mirian', 'mirna', 'mônica', 'monserrath', 'muriel', 'nadja', 'nadine', 'naide',  
    'nalva', 'nara', 'natacha', 'nathalie', 'nereide', 'nery', 'nicete', 'nicola',  
    'nina', 'noemi', 'norma', 'odonira', 'ofélia', 'olaia', 'olga', 'olinda',  
    'omara', 'ondina', 'onesina', 'oreliana', 'oriana', 'orlanda', 'orlene', 'osana',  
    'óthila', 'pacífica', 'paloma', 'pandora', 'paneia', 'paola', 'parecida', 'parisa',  
    'patrícia', 'paulaine', 'paulina', 'penélope', 'perpétua', 'petra', 'pia', 'piedade',  
    'pigmeia', 'poliana', 'polyana', 'prisca', 'profiría', 'queli', 'quenia', 'quirina',  
    'racquel', 'rafaella', 'raiane', 'raina', 'ralphina', 'ramira', 'rebecca', 'regiane',  
    'regina', 'rejanira', 'remila', 'renata', 'renata', 'renilda', 'renilda', 'renita',  
    'renata', 'renilda', 'renata', 'renilia', 'reny', 'reparatriz', 'resia', 'rete',  
    'ricasol', 'ricasol', 'rígia', 'rita de cássia', 'roberta', 'rosangela', 'rosaria', 'roselane',  
    'rosilda', 'rosineide', 'rosita', 'ruby', 'rute', 'sabrina', 'sagraja', 'salete',  
    'samara', 'samira', 'samuela', 'sandra', 'sandra', 'sandrine', 'sanita', 'sara',  
    'sarah', 'seila', 'selena', 'serena', 'serginia', 'severina', 'silene', 'sílvia',  
    'simara', 'simona', 'sonia', 'sonja', 'sônia', 'soraya', 'stella', 'suzana',  
    'suzette', 'talisa', 'tâmara', 'tamara', 'tâmara', 'tânia', 'teodora', 'teresinha',  
    'thalia', 'thelma', 'thora', 'tina', 'túlia', 'valda', 'valdirene', 'vale',  
    'valéria', 'vânia', 'vania', 'vanda', 'vania', 'vanília', 'vanusa', 'vênus',  
    'verônica', 'vi', 'viana', 'victoria', 'victória', 'victorina', 'vilma', 'vulcana',  
    'wilma', 'yara', 'yasmin', 'zelma', 'zelita', 'zina', 'zion', 'zoé',  
    'zoraide', 'zorina', 'zuleica', 'zulmira', 'zuza', 'dade', 'daliane', 'dalva',  
    'domingas', 'donatella', 'edir', 'edith', 'elea', 'elen', 'eliane', 'elisia',  
    'elma', 'elvira', 'ena', 'enide', 'enue', 'eran', 'eri', 'erica',  
    'erlana', 'ermelinda', 'erneste', 'eryka', 'esperança', 'ethere', 'etina', 'eurídice',  
    'evas', 'evânia', 'evângela', 'ewa', 'exilda', 'fabíola', 'farida', 'fatima',  
    'felicidade', 'fernanda', 'fiorella', 'flor', 'florencia', 'florinda', 'fortuna', 'francieli',  
    'francelina', 'fransisca', 'frida', 'gabriela', 'gail', 'gal', 'galileia', 'garda',  
    'gedda', 'genésia', 'geovana', 'genilda', 'ginete', 'gisela', 'giovana', 'gladys',  
    'gláucia', 'glendha', 'glória', 'gorete', 'guilhermina', 'guta', 'harlene', 'hayley',  
    'heloísa', 'helô', 'hermenegilda', 'herme', 'hermina', 'hildete', 'hilda', 'hildete',  
    'hilde', 'hilka', 'hilka', 'hisa', 'hovana', 'húria', 'illya', 'iracema',  
    'iraísa', 'ireine', 'irenita', 'irina', 'irmã', 'isa', 'isadora', 'isele',  
    'isolda', 'ivane', 'ivanilda', 'ivonete', 'izaura', 'iziara', 'jadira', 'jael',  
    'jane', 'janete', 'janira', 'janise', 'janitta', 'jara', 'jéssica', 'jessyca',  
    'joella', 'joênia', 'jolanda', 'jonathas', 'joselita', 'josiane', 'journelle', 'joyce',  
    'juana', 'judite', 'julieta', 'juline', 'junia', 'justina', 'kaela', 'kaiá',  
    'kalina', 'kássia', 'katiane', 'keicy', 'keila', 'kelly', 'kemily', 'kenia',  
    'kerolayne', 'kessia', 'ketlin', 'khatia', 'kia', 'kim', 'klemens', 'korina',  
    'laetitia', 'laiara', 'laicia', 'laís', 'lailane', 'laine', 'lais', 'lara',  
    'lars', 'larúcia', 'lasia', 'laura', 'leia', 'leila', 'leonor', 'leonora',  
    'lerisa', 'leslie', 'liana', 'liane', 'liliane', 'lilisa', 'linda', 'linna',  
    'lira', 'liuba', 'livia', 'loreta', 'lorine', 'lorrane', 'lourenza', 'lovisa',  
    'luana', 'lubia', 'lucena', 'lucineia', 'lucineia', 'lucrecia', 'luísa', 'luisa',  
    'lumena', 'lúcia', 'lusângela', 'luzia', 'lyara', 'lygia', 'lys', 'maira',  
    'maisa', 'majô', 'malu', 'mamede', 'mane', 'mara', 'marcia', 'marcelina',  
    'marcelly', 'marcia', 'margarete', 'mariana', 'marieta', 'marilene', 'marilia',  
    'marilsa', 'marilu', 'marina', 'marinete', 'maristela', 'mariza', 'marli', 'marlice',  
    'marlene', 'martina', 'maruza', 'mary', 'matilde', 'maura', 'maurine', 'maury',  
    'mayara', 'mayssa', 'meire', 'melina', 'melita', 'mell', 'melody', 'michele',  
    'michelle', 'milena', 'milka', 'miltonia', 'mirela', 'mirella', 'mirian', 'mirna',  
    'mirtes', 'mirthes', 'mônica', 'monse', 'muriel', 'nádia', 'naia', 'naísa',  
    'nailda', 'nália', 'nanda', 'neia', 'neide', 'neli', 'nelma', 'nélida',  
    'neri', 'nessa', 'neta', 'nette', 'nika', 'nilda', 'nilma', 'nilsa',  
    'ninfa', 'nisa', 'nutella', 'oaleska', 'olanda', 'olinda', 'omira', 'ontina',  
    'ophelia', 'otília', 'oterleia', 'ourienes', 'paine', 'paixão', 'paloma', 'pâmela',  
    'patience', 'paulaine', 'paulina', 'paz', 'pénélope', 'petra', 'piças', 'pina',  
    'pira', 'piedade', 'polina', 'priscilla', 'queli', 'queila', 'quezia', 'quina',  
    'raissa', 'ralphina', 'ramira', 'rania', 'raphaela', 'rayssa', 'rebecca', 'regiane',  
    'regina', 'rehia', 'relita', 'remosina', 'renata', 'renata', 'renilda', 'renilde',  
    'renite', 'reola', 'reteme', 'reuza', 'rica', 'ricarda', 'rígia', 'rinata',  
    'rita', 'robina', 'robyn', 'rocela', 'rochelle', 'rodesia', 'rodolina', 'rogéria',  
    'rosa', 'rosalba', 'rosalina', 'rosamaria', 'rosângela', 'roseni', 'rosifer', 'rosilene',  
    'rosimeire', 'rosine', 'rosita', 'roxana', 'ruth', 'sabina', 'sabrina', 'salete',  
    'samanta', 'samira', 'sandra', 'sandy', 'sania', 'sanira', 'sanita', 'saraly',  
    'sara', 'savina', 'seice', 'selia', 'selva', 'senda', 'serafina', 'serena',  
    'sheron', 'shirley', 'sidneia', 'sílvia', 'simara', 'simona', 'sintia', 'siomara',  
    'sirlene', 'sônia', 'sonia', 'soraia', 'soraya', 'sueli', 'súellen', 'suely',  
    'susana', 'susanne', 'sweetie', 'talitha', 'tamara', 'tâmara', 'tamilia', 'tanice',  
    'tarcila', 'tatiane', 'tchabi', 'tecla', 'teodora', 'teresinha', 'theresa', 'thícia',  
    'thiffany', 'thina', 'thomazina', 'timóteo', 'tina', 'tresa', 'troiana', 'túlia',  
    'ulrica', 'unice', 'urânia', 'vanessa', 'vânia', 'vania', 'vanda', 'vangélia',  
    'vanice', 'vanusa', 'vanuza', 'vânia', 'venice', 'venucia', 'verena', 'verônica',  
    'viana', 'victoria', 'victória', 'violeta', 'virginia', 'vislane', 'viviane', 'viviana',  
    'wanda', 'welma', 'xênia', 'ximena', 'yasmin', 'yana', 'yara', 'yasmin',  
    'yone', 'yvana', 'yvone', 'yvone', 'zaíra', 'zanira', 'zelia', 'zelia',  
    'zelma', 'zélia', 'ziralda', 'zirene', 'zlata', 'zoe'
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
