import BaixarEExtrair
import FiltrarDadosBaixados

anoDesejado = input("De qual ano deseja as informações do ENEM? ")

#manipulador = BaixarEExtrair.GerenciadorDeDownloadEExtracao()
#manipulador.start(anoDesejado)

filtrador = FiltrarDadosBaixados.ArquivoCSV()
filtrador.start(anoDesejado)
