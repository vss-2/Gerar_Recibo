from bottle import route, request, run, template, static_file, get
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
                'basecalc': str(basecalc),
                'icms': str(icms),
                'total': str(total)
        }

        with open(str(nome_arq)+'.json', 'w') as output_json:
                json.dump(output_dados, output_json)
        
        return template('template/concluido', nome_arquivo=nome_arq, valor_total=total)


run(host='localhost', port=8080, debug=True)
