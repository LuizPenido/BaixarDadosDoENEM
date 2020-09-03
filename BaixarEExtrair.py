import urllib.request
import os
import zipfile

class GerenciadorDeDownloadEExtracao:
    _urlBase = "http://download.inep.gov.br/microdados/microdados_enem"

    #FUNÇÕES EXTERNAS
    def __init__(self):
        self._ano = 0
        self._urlFinal = ""
        self._DownloadDir = ""
        self._ExtractDir = ""
        
    def start(self, ano):
        self.definirAnoECaminhos(ano)
        print("Criando diretórios...")
        self.assegurarAExistenciaDosDiretorios()
        print("Baixando arquivos...")
        self.baixarArquivo()
        print('Extraindo Arquivos...')
        self.extrairArquivo()    
    
    #FUNÇÕES INTERNAS
    #Define o ano de Download e o nome do arquivo que será baixado
    def definirAnoECaminhos(self, ano):
        self._ano = ano
        self._DownloadDir = "./Arquivos/Zip/" + str(self._ano) + ".zip"
        self._ExtractDir = "./Arquivos/DadosBrutos/" + str(self._ano)
        
    #Verifica se os diretorios de download e extração existem e,
    #caso não existam, cria-os.
    def assegurarAExistenciaDosDiretorios(self):
        try:
            if not os.path.exists(self._DownloadDir):
                os.makedirs(self._DownloadDir)
            if not os.path.exists(self._ExtractDir):
                os.makedirs(self._ExtractDir)
        except Exception as e:
            print("Erro ao criar diretórios.")
            print("Por favor, tente novamente.")
            raise(e)
        
    #Este metódo é necessário, pois, os links para download no site do governo
    #não possuem apenas uma única forma. São 3 as formas de link do ENEM 2009
    #até o ENEM 2019
    def definirURL(self, formatoDaURL):
        if(formatoDaURL == 0):
            self._urlFinal = self._urlBase + str(self._ano) + ".zip"
        else:
            if(formatoDaURL == 1):
                self._urlFinal = self._urlBase + "_" + str(self._ano) + ".zip"
            else:
                self._urlFinal = self._urlBase + str(self._ano) + "_.zip"
            
    
    #Tenta baixar o arquivo
    def baixarArquivo(self):
        formatoDaURL = 0
        while(True):
            try:
                self.definirURL(formatoDaURL)
                urllib.request.urlretrieve(self._urlFinal, self._DownloadDir)
                break
            except Exception as e:
                if(formatoDaURL < 2):
                    formatoDaURL += 1
                else:
                    print("Erro ao baixar arquivo.")
                    print("Por favor, tente novamente.")
                    raise(e)
                
    #Tenta extrair o arquivo
    def extrairArquivo(self):
        try:
            arquivoZip = zipfile.ZipFile(self._DownloadDir)
            arquivoZip.extractall(self._ExtractDir)
        except Exception as e:
            print("Erro ao extrair arquivo.")
            print("Por favor, tente novamente.")
            raise(e)
