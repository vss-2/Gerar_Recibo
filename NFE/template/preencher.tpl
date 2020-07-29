<!DOCTYPE html>
<html>
        <head>
                <title>Preenchendo arquivo</title>
                <link type="text/css" href="/static/styles.css" rel="stylesheet">
        </head>
        <body>
                <div class="dados">
        	<form action='/concluido' method='post'>
                	<div class="formulario"><p> Nome do arquivo:        <input name="nome_arq" type="text" /><br> </p> </div>
                        <div class="formulario"><p> Nome do comprador:      <input name="nome" type="text" /><br> </p> </div>
                        <div class="formulario"><p> CPF / CNPJ:             <input name="cp" type="text" /><br> </p> </div>
                        <div class="formulario"><p> Endereço:               <input name="endereco" type="text" /><br> </p> </div>
                        <div class="formulario"><p> Número:                 <input name="numero" type="text" /><br> </p> </div>
                        <div class="formulario"><p> Bairro:                 <input name="bairro" type="text" /><br> </p> </div>
                        <div class="formulario"><p> Complemento:            <input name="complemento" type="text" /><br> </p> </div>
                        <div class="formulario"><p> Cidade:                 <input name="cidade" type="text" /><br> </p> </div>
                        <div class="formulario"><p> Número da nota:         <input name="nota" type="text" /><br> </p> </div>
                        <div class="formulario"><p> Série da nota:          <input name="serie" type="text" /><br> </p> </div>
                        <div class="formulario"><p> Data da venda:          <input name="data" type="text" /><br> </p> </div>
                        <div class="formulario"><p> Código de Barras        <input name="cbarras" type="text" /><br> </p> </div>
                        <div class="formulario"><p> Base de cálculo:        <input name="basecalc" type="text" /><br> </p> </div>
                        <div class="formulario"><p> ICMS:                   <input name="icms" type="text" /><br> </p> </div>
                        <div class="formulario"><p> Valor total da nota:    <input name="total" type="text" /><br> </p> </div>
                        <div class="formulario"><p> Output:                 <input name="output" type="text" /><br> </p> </div>
                	<input class="salvar" value="Salvar" type="submit" />
		</form>
                </div>
        </body>
</html>