import shutil
from tkinter import *
from tkinter import messagebox
import os


def Excluir_Temps():

    nome_usuario = os.getlogin()

    # caminho do diretorio
    caminho = rf"C:\Users\{nome_usuario}\AppData\Local\Temp"

    # sai apagando as pastas e arquivos nesse diretorio
    for caminho, pastas, arquivos in os.walk(caminho):
        for pasta in pastas[:]:
            try:
                pastas.remove(pasta)
                shutil.rmtree(os.path.join(caminho, pasta))
            except PermissionError:
                continue

        for arquivo in arquivos[:]:
            try:
                arq = os.path.join(caminho, arquivo)
                os.remove(arq)
            except PermissionError:
                continue

    # verifica se o fui tudo apagado
    if os.listdir(caminho) == []:
        messagebox.showinfo(
            title="Mensagem", message="Todos os arquivos foram apagados com sucesso")
    else:
        messagebox.showwarning(
            title="Mensagem", message="Conseguimos apagar tudo que foi possivel mas talvez ainda tenha alguns arquivos bloqueados para exclusão")


def Sair():
    try:
        quit()
    except:
        os.system("taskkill /im deleta-arquivos-temporarios.exe")


janela = Tk()

janela.title("Deleta Temps")

botao_deleta = Button(
    janela, text="Deletar Arquivos Temporários", command=Excluir_Temps)
botao_deleta.grid(column=0, row=0, padx=10, pady=10)

botao_sair = Button(janela, text="Sair", command=Sair)
botao_sair.grid(column=0, row=1, padx=10, pady=10)


janela.mainloop()
