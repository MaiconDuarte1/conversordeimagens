#INCLUSÃO DE BIBLIOTECAS
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, askopenfile, asksaveasfile, asksaveasfilename
import customtkinter as ct
import os
from IMGCONVERTER import funcoes as f


# CONFIGURAÇÕES INICIAIS
ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")
janela = ct.CTk()
janela.title("APP CONVERSOR DE IMAGENS")
janela.resizable(False, False)
janela.geometry("640x480")
janela.iconbitmap(os.path.dirname(os.path.abspath(__file__))+"/converter.ico")
janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

tabview = ct.CTkTabview(janela, width=633, height=473)
tabview.grid()
tabview.add("CONVERTER")
tabview.tab("CONVERTER").grid_columnconfigure(0, weight=1)
tabview.add("OPÇÕES")
tabview.tab("OPÇÕES").grid_columnconfigure(0, weight=1)

#CONFIGURAÇÃO DA JANELA DE CONVERSÃO


values = ['webp', 'png', 'jpeg']

label_textomensagem = ct.CTkLabel(tabview.tab("CONVERTER"), text="SELECIONE A EXTENSÃO QUE DESEJA CONVERTER:")
label_textomensagem.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

combobox_conversao = ct.CTkComboBox(tabview.tab("CONVERTER"), values=values)
combobox_conversao.grid(row=2, column=0, padx=10, pady=10, columnspan=3)

label_localsalvar = ct.CTkLabel(tabview.tab("CONVERTER"), text="SALVAR EM:")
label_localsalvar.grid(row=3, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)

botao_localsalvar = ct.CTkButton(tabview.tab("CONVERTER"), text="DIRETÓRIO", command=f.botaodiretorio)
botao_localsalvar.grid(row=4, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)

label_direscolhido = ct.CTkLabel(tabview.tab("CONVERTER"), text="")
label_direscolhido.grid(row=5, column=0, padx=10, pady=10, sticky='nsew', columnspan=3)

botao_paramp3 = ct.CTkButton(tabview.tab("CONVERTER"), text="CONVERTER", command=f.converter)
botao_paramp3.grid(row=6, column=0, sticky='nsew', columnspan=3)

#JANELA DE OPÇÕES

label_textmensagemOP = ct.CTkLabel(tabview.tab("OPÇÕES"), text="ALTERAR APARENCIA DO APLICATIVO:")
label_textmensagemOP.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

menu_opcoes = ct.CTkOptionMenu(tabview.tab("OPÇÕES"), values=["Dark", "Light", "System"], command=f.change_appearance_mode_event)
menu_opcoes.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

label_textsobreOP = ct.CTkLabel(tabview.tab("OPÇÕES"), text="Aplicativo Desenvolvido Por Python Júnior (Paikin)")
label_textsobreOP.grid(row=2, column=0, padx=10, pady=10, columnspan=3)

label_textsobreOP2 = ct.CTkLabel(tabview.tab("OPÇÕES"), text="Versão Beta 1.0")
label_textsobreOP2.grid(row=3, column=0, padx=10, pady=10, columnspan=3)


