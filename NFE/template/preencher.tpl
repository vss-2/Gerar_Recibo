<!DOCTYPE html>
<html>
        <head>
                <title>Preenchendo arquivo</title>
                <link type="text/css" href="/static/styles.css" rel="stylesheet">
        </head>
        <body>
                <div class="dados">
        	<form action='/concluido' method='post'>
                	<div class="formulario">Nome do arquivo:        <input name="nome_arq" type="text" /><br> </div>
                        <div class="formulario">Nome do comprador:      <input name="nome" type="text" /><br> </div>
                        <div class="formulario">CPF / CNPJ:             <input name="cp" type="text" /><br> </div>
                        <div class="formulario">Endereço:               <input name="endereco" type="text" /><br> </div>
                        <div class="formulario">Número:                 <input name="numero" type="text" /><br> </div>
                        <div class="formulario">Bairro:                 <input name="bairro" type="text" /><br> </div>
                        <div class="formulario">Complemento:            <input name="complemento" type="text" /><br> </div>
                        <div class="formulario">Cidade:                 <input name="cidade" type="text" /><br> </div>
                        <div class="formulario">Número da nota:         <input name="nota" type="text" /><br> </div>
                        <div class="formulario">Série da nota:          <input name="serie" type="text" /><br> </div>
                        <div class="formulario">Data da venda:          <input name="data" type="text" /><br> </div>
                        <div class="formulario">Código de Barras        <input name="cbarras" type="text" /><br> </div>
                        <div class="formulario">Base de cálculo:        <input name="basecalc" type="text" /><br> </div>
                        <div class="formulario">ICMS:                   <input name="icms" type="text" /><br> </div>
                        <div class="formulario">Valor total da nota:    <input name="total" type="text" /><br> </div>
                        <div class="formulario">Output:                 <input name="output" type="text" /><br> </div>
                	<input class="salvar" value="Salvar" type="submit" />
		</form>
                </div>
        </body>
</html>