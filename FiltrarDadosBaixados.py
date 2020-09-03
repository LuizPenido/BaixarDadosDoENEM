import csv
import tkinter
import os

class Janela:
    def __init__(self, cabecalho):
        self._janela = tkinter.Tk()
        self._janela.title("Quais informações deseja filtrar?")
        tkinter.Label(self._janela, text="FECHE A JANELA QUANDO TERMINAR DE SELECIONAR OS ITENS DESEJADOS").pack(anchor='w')
        self._vBarraDeRolagem = tkinter.Scrollbar(self._janela)
        self._canvas = tkinter.Canvas(self._janela, yscrollcommand=self._vBarraDeRolagem.set)
        
        self._vBarraDeRolagem.config(command=self._canvas.yview)
        self._vBarraDeRolagem.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        
        self._frame = tkinter.Frame(self._canvas)
        self._canvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        self._canvas.create_window(0, 0, window=self._frame, anchor='nw')
        self._informacoes = []
        c = 0
        for key in cabecalho:
            self._informacoes.append(tkinter.IntVar())
            tkinter.Checkbutton(self._frame, text=key, variable=self._informacoes[c]).pack(anchor='w')
            c += 1
        self._janela.update()
        self._canvas.config(scrollregio=self._canvas.bbox("all"))
        self._janela.mainloop()
    
    def obterValoresDoCheckbutton(self):
        return self._informacoes
    
class ArquivoCSV:
    #FUNÇÕES EXTERNAS
    def __init__(self):
        self._ano = 0
        self._diretorioDosDadosBrutos = ""
        self._diretorioDosDadosFiltrados = ""
        
    def start(self, ano):
        self.definirAnoEDiretorioDoArquivo(ano)
        self.assegurarAExistenciaDosDiretorios()
        with open(self._diretorioDosDadosBrutos, 'r', newline='') as csvfileLeitura:
            dicionarioComDadosBrutos = csv.DictReader(csvfileLeitura, delimiter=';')
            print("Iniciando janela para seleção dos dados")
            janelaParaEscolhaDeInformacoes = Janela(dicionarioComDadosBrutos.fieldnames)
            valoresCheckbutton = janelaParaEscolhaDeInformacoes.obterValoresDoCheckbutton()
            with open(self._diretorioDosDadosFiltrados, 'w', newline='') as csvfileEscrita:
                cabecalhoDosDadosFiltrados = []
                print("Filtrando dados...")
                for i in range(0, len(valoresCheckbutton)):
                    if(valoresCheckbutton[i].get() == 1):
                        cabecalhoDosDadosFiltrados.append(dicionarioComDadosBrutos.fieldnames[i])
                arquivoParaEscrita = csv.DictWriter(csvfileEscrita, fieldnames=cabecalhoDosDadosFiltrados, delimiter=';')
                arquivoParaEscrita.writeheader()
                for row in dicionarioComDadosBrutos:
                    dicionario = {}
                    for key in cabecalhoDosDadosFiltrados:
                        dicionario[key] = row[key]
                    arquivoParaEscrita.writerow(dicionario)
        print("Dados filtrados com sucesso!")
    
    #FUNÇÕES INTERNAS
    #Define o diretório e o ano do arquivo que passará pelo filtro
    def definirAnoEDiretorioDoArquivo(self, ano):
        self._ano = ano
        self._diretorioDosDadosBrutos = './Arquivos/DadosBrutos/' + str(ano) + '/DADOS/MICRODADOS_ENEM_' + str(ano) + '.csv'
        self._diretorioDosDadosFiltrados = './Arquivos/DadosFiltrados/' + str(ano) + '.csv'

    def assegurarAExistenciaDosDiretorios(self):
        try:
            if not os.path.exists('./Arquivos/DadosFiltrados/'):
                os.makedirs('./Arquivos/DadosFiltrados/')
        except Exception as e:
            print("Erro ao criar diretórios.")
            print("Por favor, tente novamente.")
            raise(e)
