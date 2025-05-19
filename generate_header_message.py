import json
from datetime import datetime

def get_dynamic_header_message():
    today = datetime.now() # Use current date
    today_dd_mm = today.strftime("%d/%m")
    today_dd_mm_yyyy = today.strftime("%d/%m/%Y")

    messages = []

    # 1. Aniversariantes
    try:
        with open("/home/ubuntu/portal_data/aniversariantes.json", "r", encoding="utf-8") as f:
            aniversariantes_data = json.load(f)
        
        hoje_aniversariantes = []
        # Assuming 'genero' field might be added later by the user for more specific messages
        # For now, we don't have genero, so we use a generic message.
        for pessoa in aniversariantes_data:
            if pessoa.get("data") == today_dd_mm:
                hoje_aniversariantes.append(pessoa["nome"])
        
        if hoje_aniversariantes:
            if len(hoje_aniversariantes) == 1:
                # User requested gender-specific: "Hoje é aniversário do NOME!" (male) or "Hoje é aniversário da NOME!" (female)
                # Since 'genero' is not in the JSON, using a generic form.
                # If 'genero' was available, e.g., pessoa.get("genero") == "masculino"
                # messages.append(f"Hoje é aniversário do <strong>{hoje_aniversariantes[0]}</strong>!<br>Deixe sua mensagem de parabéns!")
                messages.append(f"Hoje é aniversário de <strong>{hoje_aniversariantes[0]}</strong>!<br>Deixe sua mensagem de parabéns!")
            else:
                nomes_formatados = [f"<strong>{nome}</strong>" for nome in hoje_aniversariantes]
                if len(nomes_formatados) > 1:
                    # Format as "NOME1 e NOME2" or "NOME1, NOME2 e NOME3"
                    if len(nomes_formatados) == 2:
                        nomes_str = " e ".join(nomes_formatados)
                    else:
                        nomes_str = ", ".join(nomes_formatados[:-1]) + " e " + nomes_formatados[-1]
                else: # Should be caught by len == 1, but as a fallback
                    nomes_str = nomes_formatados[0]
                messages.append(f"Hoje é aniversário de {nomes_str}!<br>Deixe sua mensagem de parabéns!")
    except FileNotFoundError:
        print("Arquivo aniversariantes.json não encontrado.")
    except Exception as e:
        print(f"Erro ao processar aniversariantes: {e}")

    # 2. Retorno de Férias
    try:
        with open("/home/ubuntu/ferias.json", "r", encoding="utf-8") as f:
            ferias_data = json.load(f)
        
        retornando_hoje = []
        for ferias_info in ferias_data:
            if ferias_info.get("retorno") == today_dd_mm_yyyy:
                retornando_hoje.append(ferias_info["colaborador"])
        
        for nome_colaborador in retornando_hoje:
            messages.append(f"Hoje, <strong>{nome_colaborador}</strong> volta de férias! Dê as boas vindas")
    except FileNotFoundError:
        print("Arquivo ferias.json não encontrado.")
    except Exception as e:
        print(f"Erro ao processar férias: {e}")

    # 3. Feriados
    try:
        with open("/home/ubuntu/feriados.json", "r", encoding="utf-8") as f:
            feriados_data = json.load(f)
        
        hoje_feriados = []
        for feriado in feriados_data:
            # Ensure feriado["data"] is in dd/mm format for comparison
            if feriado.get("data") == today_dd_mm:
                hoje_feriados.append(feriado["nome"])
        
        for nome_feriado in hoje_feriados:
            messages.append(f"Feliz Dia de <strong>{nome_feriado}</strong>!")
    except FileNotFoundError:
        print("Arquivo feriados.json não encontrado. Usando mensagem padrão.")
        # No specific error message for header if feriados.json is missing, it just won't show a holiday message.
    except Exception as e:
        print(f"Erro ao processar feriados: {e}")

    if not messages:
        return "Aqui é o <stong>seu espaço</stong>. Aqui é <stong>PSR!</stong>"
    else:
        # Join messages with <br> only if there are multiple messages. The <br> inside anniversary message handles its own line break.
        return "<br>".join(messages)

if __name__ == "__main__":
    header_html = get_dynamic_header_message()
    # Salvar no diretório de upload onde o index.html está localizado
    with open("/home/ubuntu/upload/header_message.html", "w", encoding="utf-8") as f_out:
        f_out.write(header_html)
    print(f"Arquivo header_message.html gerado com a mensagem: {header_html}")
