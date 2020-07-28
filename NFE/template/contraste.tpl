<!DOCTYPE html>
<html>
        <head>
                <title>{{title or 'Sem título'}}</title>
                <link type="text/css" href="/static/styles.css" rel="stylesheet">
        </head>
        <body style="display:grid; place-items:center;" >
                <form action="/contraste" method="post" enctype="multipart/form-data">
                        <input type="file" name="imagem_arquivo" accept="image/*" /> <br><br>
                        Nome do arquivo: <input type="text" name="nome_arquivo" /> <br><br>
                        <input value="Corrigir" type="submit" />
                </form>
        </body>
</html>