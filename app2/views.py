from django.shortcuts import render
from django.http import HttpResponse

def vistaDos(request):
   html=""" <!DOCTYPE html>
    <html>
    <head>
        <title>Vista DOS 222222222222222222</title>
    </head>
    <body>
        <h1>Vista DOSSS 222222</h1>
        <p>Este es un párrafo de texto de la vista 2</p>
        <ul>
            <li>Elemento de lista 1</li>
            <li>Elemento de lista 2</li>
            <li>Elemento de lista 3</li>
        </ul>
        <ol>
            <li>Elemento numerado 1</li>
            <li>Elemento numerado 2</li>
            <li>Elemento numerado 3</li>
        </ol>
        <a href="https://www.inacap.cl/">Enlace al sitio web de INACAP</a>
        
        <br>
        <br>
        <form action="procesar_formulario" method="POST">
            <input type="text" name="nombre" placeholder="Nombre">
            <input type="email" name="correo" placeholder="Correo electrónico">
            <button type="submit">Enviar</button>
        </form>
        <br>
        <br>
        <p>Natalia Navarrete</p>
    </body>
    </html>
   """
   return HttpResponse(html)