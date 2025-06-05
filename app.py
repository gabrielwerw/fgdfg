
import streamlit as st
import time

st.set_page_config(page_title="Assistente: GMAC", layout="wide")

st.markdown(""" 
    <style>
    body {
        background-color: #f7f8fa;
    }
    .chatbox {
        max-width: 1080px;
        margin: auto;
        padding: 20px;
    }
    .bubble {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 14px;
        padding: 16px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
        font-family: 'Segoe UI', sans-serif;
        animation: fadein 0.5s ease-in;
    }
    .author {
        font-weight: 600;
        color: #1F3645;
        margin-bottom: 12px;
        font-size: 17px;
    }
    .tabela {
        width: 100%;
        border-collapse: collapse;
        font-size: 14px;
    }
    .tabela th, .tabela td {
        border: 1px solid #e6e6e6;
        padding: 8px 10px;
        text-align: center;
    }
    .tabela th {
        background-color: #f0f2f6;
        color: #1F3645;
        font-weight: 600;
    }
    .destaque {
        background-color: #fff4f0 !important;
        font-weight: bold;
        color: #9C0000;
    }
    @keyframes fadein {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
""", unsafe_allow_html=True)

aba = st.selectbox("Escolha o painel:", ["Frentes de Trabalho", "Atividades", "Resumo IA GMAC"], index=0)

if aba == "Frentes de Trabalho":
    headers = ["Frente", "Área", "Equipamentos principais", "Turno", "Supervisor", "Tec. Doc", "Qtd. Inspetores"]
    linhas = [
        ["1", "Caldeiras/Condensado", "B1-2230A, B1-2230B", "DIA", "Huggo Mello - 01", "Isabella - 01", "2"],
        ["1", "Caldeiras/Condensado", "B1-2230A, B1-2230B", "NOITE", "Adeildo - 01", "Miqueias - 01", "2"],
        ["2", "Oxidação", "Vasos e Trocadores", "DIA", "Expedito Souza - 02", "Adriano - 02", "5"],
        ["2", "Oxidação", "Vasos e Trocadores", "NOITE", "Serginho - 02", "Cristiano - 02", "5"],
        ["3", "Purificação/Tancagem", "Vasos, Trocador", "DIA", "Adalberto Saturno - 03", "Dayvson - 03", "5"],
        ["3", "Purificação/Tancagem", "Vasos, Trocador", "NOITE", "Gutemberg Rolim - 03", "Cristiano - 03", "5"],
        ["4", "ETA / Off Gás / Armazenamento PTA", "Tanques, Torres", "DIA", "Thiago - 04", "Rosemary - 04", "4"],
        ["4", "ETA / Off Gás / Armazenamento PTA", "Tanques, Torres", "NOITE", "Bruno Marques - 04", "Miqueias - 04", "4"]
    ]

    if 'highlight_frente' not in st.session_state:
        st.session_state.highlight_frente = 0
    st.session_state.highlight_frente = (st.session_state.highlight_frente + 1) % len(linhas)

    st.markdown("<div class='chatbox'><div class='bubble'><div class='author'>Assistente: GMAC</div>", unsafe_allow_html=True)

    tabela_html = "<table class='tabela'><tr>"
    tabela_html += "".join([f"<th>{col}</th>" for col in headers]) + "</tr>"

    for i, row in enumerate(linhas):
        row_class = "destaque" if i == st.session_state.highlight_frente else ""
        tabela_html += f"<tr>{''.join([f'<td class="{row_class}">{cell}</td>' for cell in row])}</tr>"

    tabela_html += "</table></div></div>"
    st.markdown(tabela_html, unsafe_allow_html=True)

    time.sleep(3)
    st.rerun()

elif aba == "Atividades":
    headers = ["ATIVIDADE", "Total Previsto", "Concluído", "Avanço"]
    atividades = [
        ["INSPEÇÃO VISUAL INTERNA", 44, 9, "20.45%"],
        ["ESPAÇO CONFINADO", 32, 8, "25.00%"],
        ["INSPEÇÃO VISUAL EXTERNA", 31, 6, "19.35%"],
        ["ME", 29, 7, "24.14%"],
        ["PREPARAÇÃO DE PONTOS ME", 28, 7, "25.00%"],
        ["LP", 27, 10, "37.04%"],
        ["IRIS/CP", 17, "", ""],
        ["REPLICA METALOGRAFICA", 14, "", ""],
        ["PM", 13, "", ""]
    ]

    if 'highlight_atividade' not in st.session_state:
        st.session_state.highlight_atividade = 0
    st.session_state.highlight_atividade = (st.session_state.highlight_atividade + 1) % len(atividades)

    st.markdown("<div class='chatbox'><div class='bubble'><div class='author'>Painel de Atividades</div>", unsafe_allow_html=True)

    tabela_html = "<table class='tabela'><tr>"
    tabela_html += "".join([f"<th>{col}</th>" for col in headers]) + "</tr>"

    for i, row in enumerate(atividades):
        row_class = "destaque" if i == st.session_state.highlight_atividade else ""
        tabela_html += f"<tr>{''.join([f'<td class="{row_class}">{cell}</td>' for cell in row])}</tr>"

    tabela_html += "</table></div></div>"
    st.markdown(tabela_html, unsafe_allow_html=True)

    time.sleep(3)
    st.rerun()

elif aba == "Resumo IA GMAC":
    headers = ["Tipo de Atividade", "Nº de Registros", "Observações Técnicas"]
    resumo = [
        ["INSPEÇÃO VISUAL INTERNA", 53, "Alta incidência em componentes acessíveis apenas com desmontagem. Fundamental para avaliação qualitativa."],
        ["RELATÓRIO INTEGRIDADE", 48, "Demonstra foco em consolidação analítica de dados pós-inspeção. Essencial para tomada de decisão gerencial."],
        ["ESPAÇO CONFINADO", 40, "Indica grande volume de intervenções em ambientes com restrição operacional severa. Envolve alto risco."],
        ["RELATÓRIO LP", 39, "Resultado de ensaios líquidos penetrantes. Alta demanda por controle de trincas superficiais."],
        ["INSPEÇÃO VISUAL EXTERNA", 37, "Parte da rotina básica de integridade externa. Complementa inspeções internas."],
        ["LP (Líquido Penetrante)", 37, "END amplamente utilizado para detecção de descontinuidades superficiais. Alta repetição."],
        ["PREPARAÇÃO DE PONTOS ME", 35, "Etapa prévia à metalografia. Envolve lixamento/polimento em campo."],
        ["RELATÓRIO ME", 35, "Consolidado técnico de réplicas metalográficas. Gera evidência estrutural."],
        ["ME (Metalografia)", 35, "Análise microestrutural. Evidencia degradação térmica, creep e alterações metalúrgicas."],
        ["IRIS/CP", 17, "Técnica automatizada para medição de perda de espessura interna por ultrassom. Usado em trocadores."],
        ["RÉPLICA METALOGRÁFICA", 14, "Extração de réplica em campo. Técnica invasiva, mas altamente precisa."],
        ["PM (Partículas Magnéticas)", 13, "Aplicado em peças ferromagnéticas para detecção de trincas superficiais e subsuperficiais."],
        ["RELATÓRIO PM", 13, "Documento técnico de laudos por partículas magnéticas. Evidencia trincas, inclusões e porosidades."]
    ]

    if 'highlight_resumo' not in st.session_state:
        st.session_state.highlight_resumo = 0
    st.session_state.highlight_resumo = (st.session_state.highlight_resumo + 1) % len(resumo)

    st.markdown("<div class='chatbox'><div class='bubble'><div class='author'>Resumo IA GMAC</div>", unsafe_allow_html=True)

    tabela_html = "<table class='tabela'><tr>"
    tabela_html += "".join([f"<th>{col}</th>" for col in headers]) + "</tr>"

    for i, row in enumerate(resumo):
        row_class = "destaque" if i == st.session_state.highlight_resumo else ""
        tabela_html += f"<tr>{''.join([f'<td class="{row_class}">{cell}</td>' for cell in row])}</tr>"

    tabela_html += "</table></div></div>"
    st.markdown(tabela_html, unsafe_allow_html=True)

    st.markdown("<br><div class='bubble'><b>🧠 Insights Técnicos Relevantes</b><br><br>"
                "O alto volume de inspeções visuais internas e externas, combinado com ensaios LP e relatórios integrados, evidencia uma abordagem robusta de controle visual e superficial.<br><br>"
                "A significativa presença de ensaios metalográficos (ME, preparação, réplicas) demonstra foco em avaliação de mecanismos de degradação por microestrutura – comum em ativos sujeitos a altas temperaturas e pressões (ex: caldeiras, vasos de pressão, trocadores de calor).<br><br>"
                "Espaço confinado aparece com frequência expressiva, indicando a necessidade constante de protocolos de segurança específicos, ventilação forçada e suporte de emergência.<br><br>"
                "Técnicas como IRIS e PM complementam o portfólio de END, assegurando abrangência tanto em detecção de corrosão interna quanto falhas estruturais superficiais.</div>", unsafe_allow_html=True)

    time.sleep(3)
    st.rerun()
