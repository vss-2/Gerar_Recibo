from bottle import route, request, run, template, static_file, get
from PIL import Image, ImageEnhance
from pathlib import Path
from os.path import splitext
from pyzbar.pyzbar import decode
import cv2 as cv
import json

@route('/')
def index():
        return template('template/inicio.tpl', title='NFE: Criador de Arquivo')

@route('/preencher')
def index():
        return template('template/preencher.tpl')

@route('/copiar')
def index():
        return static_file('NFE_parser.html', root='static/')

@route('/static/styles.css', method='GET')
def index():
        return static_file('styles.css', root='static/')

@route('/concluido', method='POST')
def post_nome():
        nome_arq        = request.forms.get('nome_arq')
        nome            = request.forms.get('nome')
        cp              = request.forms.get('cp')
        endereco        = request.forms.get('endereco')
        numero          = request.forms.get('numero')
        bairro          = request.forms.get('bairro')
        complemento     = request.forms.get('complemento')
        cidade          = request.forms.get('cidade')
        nota            = request.forms.get('nota')
        serie           = request.forms.get('serie')
        data            = request.forms.get('data')
        cbarras         = request.forms.get('cbarras')
        basecalc        = request.forms.get('basecalc')
        icms            = request.forms.get('icms')
        total           = request.forms.get('total')
        output          = request.forms.get('output')
        output_dados = {}
        
        output_dados = {
                'nome': str(nome),
                'cp': str(cp),
                'endereco': str(endereco),
                'numero': str(numero),
                'bairro': str(bairro),
                'complemento': str(complemento),
                'cidade': str(cidade),
                'nota': str(nota),
                'serie': str(serie),
                'data': str(data),
                'cbarras': str(cbarras),
                'basecalc': str(basecalc),
                'icms': str(icms),
                'total': str(total),
                'output': str(output)
        }

        with open(str(nome_arq)+'.json', 'w') as output_json:
                json.dump(output_dados, output_json)
        
        return template('template/concluido', nome_arquivo="Nome do arquivo gerado: {}".format(nome_arq), valor_total="Valor do total da nota: {}".format(total))

@route('/contraste', method='GET')
def index():
        return template('template/contraste.tpl', title='Correção de constraste')

@route('/contraste', method='POST')
def index():
        abrir_img = request.files.get('imagem_arquivo')
        nome_img  = request.forms.get('nome_arquivo')

        novo_arquivo = Path(str(Path.cwd())+'/'+str(abrir_img.filename))

        if(novo_arquivo.is_file() == True):
                novo_arquivo.rename(novo_arquivo.name[:-len(novo_arquivo.suffix)]+'_old'+str(novo_arquivo.suffix))
        abrir_img.save(novo_arquivo.name)
        
        abre_img  = Image.open(novo_arquivo.name)
        edit_img  = ImageEnhance.Brightness(abre_img)
        contraste = edit_img.enhance(2.0)
        contraste.save(str(Path.cwd())+'/images/{}{}'.format(nome_img, splitext(abrir_img.filename)[1]))

        opencv_img = cv.imread(str(Path.cwd())+'/images/{}{}'.format(nome_img, splitext(abrir_img.filename)[1]))
        
        cdg_barras = None

        for cdg_barras in decode(opencv_img):
                if(cdg_barras.type.lower() == 'code128'):
                        print("Sucesso!")

        abre_img.close()
        contraste.close()
        abrir_img = None
        edit_img = None
        contraste = None
        return template('template/concluido', nome_arquivo=str('O aumento de contraste foi concluído com sucesso, salvo em: '+str(nome_img)), valor_total=str('Código de barras: '+str(cdg_barras)))

run(host='localhost', port=8080, debug=True)
