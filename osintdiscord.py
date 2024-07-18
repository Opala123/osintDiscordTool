#   !!!!!!!!!!!!!!!!           WARNING              !!!!!!!!!!!!!!!!!!!!!!
#   NÃO ESQUEÇA DE USAR O PIP PARA INSTALAR AS BIBLIOTECAS NECESSÁRIAS!!!!

import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
import pyperclip
import os
from bs4 import BeautifulSoup
import webbrowser
import time
from tkinter import PhotoImage

# Funções:

def abrir_discord():
    url = "https://discord.gg/6EP4EUsDwg"
    webbrowser.open(url)


def analizaDados():
    diretorio = input_name1.get()
    caminho_arquivo_saida = f'{input_name2.get()}/resultado.txt'  # Mude essa campo caso queira que o arquivo txt de saída tenha outro nome

    if not os.path.isdir(diretorio) or not os.path.isdir(os.path.dirname(caminho_arquivo_saida)):
        print(f'Diretório inválido: {diretorio} ou {os.path.dirname(caminho_arquivo_saida)}')
        sucesso_label.configure(text="Diretório inválido", text_color="red")
        window.after(3000, lambda: sucesso_label.configure(text=""))  # Limpar mensagem após 3 segundos
        return

    if not os.path.exists(os.path.dirname(caminho_arquivo_saida)):
        os.makedirs(os.path.dirname(caminho_arquivo_saida))

    arquivos = os.listdir(diretorio)
    arquivos_logs = [arquivo for arquivo in arquivos if arquivo.startswith('log') and arquivo.endswith('.html')]

    nomes_contagem = {}


    with open(caminho_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
        
        for arquivo in arquivos_logs:
            arquivo_saida.write(f'Lendo arquivo: {arquivo}\n')
            with open(os.path.join(diretorio, arquivo), 'r', encoding='utf-8') as file:
                data = file.read()

            soup = BeautifulSoup(data, 'html.parser')

            conteudos = soup.find_all(class_="usernameFont_cdc675 username_cdc675")
            nome_server = soup.find(class_="defaultColor_a595eb lineClamp1_a595eb text-md/semibold_dc00ef defaultColor_e9e35f name_fd6364")

            contador = 0
            for conteudo in conteudos:
                contador += 1
                nome = conteudo.text.strip()  
                arquivo_saida.write(nome + '\n')

                if nome in nomes_contagem:
                    nomes_contagem[nome] += 1
                else:
                    nomes_contagem[nome] = 1

            arquivo_saida.write(f"Contador: {contador}\n")
            arquivo_saida.write(f"Server: {nome_server.text}\n")
            arquivo_saida.write("------------------------\n")


        arquivo_saida.write("Nomes repetidos:\n")
        for nome, quantidade in nomes_contagem.items():
            if quantidade > 1:
                arquivo_saida.write(f"{nome}: {quantidade} vezes  Segundos totais: {quantidade * 20} Minutos totais{round((quantidade * 20) / 60, 2)}\n")

    print(f'Os resultados foram salvos em: {caminho_arquivo_saida}')

    sucesso_label.configure(text="salvo com sucesso!!!", text_color="green")
    window.after(3000, lambda: sucesso_label.configure(text=""))


def gerarjs():
    timejs = input_name3.get()

    result = int(timejs) * 1000

    javascript_code = f"""
    let intervalo = {result};

    let contador = 1;

    let timer = setInterval(() => {{
        let elementsAbove = document.querySelectorAll('.header_fd6364');
        let elementsBelow = document.querySelectorAll('.scroller_c43953.thin_eed6a8.scrollerBase_eed6a8.fade_eed6a8.customTheme_eed6a8');

        let filteredHTML = '';

        elementsAbove.forEach(element => {{
            filteredHTML += element.outerHTML;
        }});

        elementsBelow.forEach(element => {{
            filteredHTML += element.outerHTML;
        }});

        let now = new Date();
        let timestamp = now.toISOString().replace(/:/g, '-').replace(/\..+/, '');
        let filename = `log_${{contador}}_${{timestamp}}.html`;

        let blob = new Blob([filteredHTML], {{type: "text/html"}});
        let url = URL.createObjectURL(blob);
        let a = document.createElement('a');
        a.href = url;
        a.download = filename;
        a.click();

        contador++;

    }}, intervalo);
    """

    pyperclip.copy(javascript_code)
    print("Código JavaScript copiado para o clipboard!")

    btn3_gerar.configure(text="COPIADO COM SUCESSO!!!")
    window.after(2000, lambda: btn3_gerar.configure(text="GERAR"))


def selecionar_pasta():
    pasta_selecionada = filedialog.askdirectory()
    if pasta_selecionada:
        print("Pasta selecionada:", pasta_selecionada)
        input_name1.delete(0, 'end')
        input_name1.insert(0, pasta_selecionada)
        


def selecionar_pasta2():
    pasta_selecionada = filedialog.askdirectory()
    if pasta_selecionada:
        print("Pasta selecionada:", pasta_selecionada)
        input_name2.delete(0, 'end')
        input_name2.insert(0, pasta_selecionada)
        


# Janela configurações: ########################################################################################


window = ctk.CTk()
window.title("Discord OSINT")  
window.geometry("500x700")
window.maxsize(width=600, height=700)  
window.minsize(width=300, height=200)
ctk.set_appearance_mode('dark')  


# Imagens #####################################################################
imagem = Image.open("icopasta.ico")
imagem = imagem.resize((40, 45))  
imagem = ImageTk.PhotoImage(imagem)

# Botões PARTE 1: ##########################################################################

btn_manual = ctk.CTkButton(window, text="MANUAL", command=selecionar_pasta, width=5, bg_color="#2a2121", fg_color='#2a2121', hover_color='#2a2121', border_width=-1, text_color="#105ddd")  # Criando botao
btn_manual.place(relx=0.8, rely=0.040, anchor="center")  

btn_info = ctk.CTkButton(window, text="INFO", command=abrir_discord, width=5, bg_color="#2a2121", fg_color='#2a2121', hover_color='#2a2121', border_width=-1, text_color="#105ddd")  # Criando botao
btn_info.place(relx=0.92, rely=0.040, anchor="center")  

btn_caminho1 = ctk.CTkButton(window, image=imagem, text=None, command=selecionar_pasta, width=5, bg_color="#2a2121", fg_color='#2a2121', hover_color='#2a2121', border_width=-1)  # Criando botao
btn_caminho1.place(relx=0.8, rely=0.2, anchor="center")  

input_name1 = ctk.CTkEntry(window, placeholder_text="                SELECIONE CAMINHO --->", width=250)
input_name1.place(relx=0.5, rely=0.2, anchor="center")

label1 = ctk.CTkLabel(window, text="PASTA EM ANÁLISE:", font=("Arial", 20))
label1.place(relx=0.5, rely=0.1, anchor="center")

# BOTOES PARTE 2 ############################################################################

btn_caminho2 = ctk.CTkButton(window, image=imagem, text=None, command=selecionar_pasta2, width=5, bg_color="#2a2121", fg_color='#2a2121', hover_color='#2a2121', border_width=-1)  # Criando botao
btn_caminho2.place(relx=0.8, rely=0.4, anchor="center")  

input_name2 = ctk.CTkEntry(window, placeholder_text="                SELECIONE CAMINHO --->", width=250)
input_name2.place(relx=0.5, rely=0.4, anchor="center")

label2 = ctk.CTkLabel(window, text="RESULTADOS ANÁLISE:", font=("Arial", 20))
label2.place(relx=0.5, rely=0.3, anchor="center")

# BOTOES ANÁLISE ###############################################################################################

btn_analise = ctk.CTkButton(window, text="ANALIZAR", command=analizaDados, width=200, font=("Arial", 35), bg_color="#107826", fg_color="#107826")  # Criando botao
btn_analise.place(relx=0.5, rely=0.55, anchor="center") 

# BOTOES PARTE 3 ###################################################################################

label3 = ctk.CTkLabel(window, text="GERAR JAVASCRIPT:", font=("Arial", 20))
label3.place(relx=0.5, rely=0.75, anchor="center")

label3_2 = ctk.CTkLabel(window, text="DELAY:", font=("Arial", 14))
label3_2.place(relx=0.8, rely=0.75, anchor="center")

input_name3 = ctk.CTkEntry(window, placeholder_text="    20", width=50, height=40)
input_name3.place(relx=0.8, rely=0.82, anchor="center")
input_name3.insert(0, 20)

btn3_gerar = ctk.CTkButton(window, text="GERAR", command=gerarjs, width=200)  
btn3_gerar.place(relx=0.5, rely=0.83, anchor="center")  

sucesso_label = ctk.CTkLabel(window, text="", text_color="green", font=("Arial", 20))
sucesso_label.place(relx=0.5, rely=0.63, anchor="center")

window.mainloop()
