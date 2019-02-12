# -*- coding: utf-8

# Isso ai em cima é pra caso esteja ASCII

from reportlab.pdfgen import canvas
from textwrap import wrap
import traceback

# O textwrap vai repartir linhas
# O traceback vai mostrar onde está o erro

def gerarRecibo():
    try:
        nomeOutput = input('Insira o nome do arquivo a ser exportado: ')
        pdf = canvas.Canvas('{}.pdf'.format(nomeOutput))
        # Pega o nome do arquivo, e gera o pdf base, o qual usamos abaixo
        
        pdf.setTitle(nomeOutput) # Título
        pdf.setFont('Arial', 14) # Formatação no padrão: Fonte, tamanho
        pdf.setFont('Arial-Bold', 12) # Formatação de negrito
        
        # Jeitos de gravar o texto:
        X = 150 
        Y = 150
        texto = 'Textinho padrão para testes'
        texto = "\n".join(wrap(texto, 5)) # Quebra o texto a cada 5 chars
        # Posicoes relativas e texto
        
        # Jeito 1
        pdf.setTextOrigin(X, Y)
        pdf.textLine(texto)
        
        # Jeito 2
        pdf.drawString(X, Y, texto)
        
        pdf.save()
        # Encerra o arquivo e o salva no 
        # diretório que o main.py está
    except:
        traceback.print_exc()
        print('Deu ruim')
        
gerarRecibo()
