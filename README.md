# esCUITValida

Esta aplicacion escrita en Python sirve para verificar la valides de una CUIT

Recuerde que usted es libre de compartir, copiar, distribuir y modificar esta aplicacion mientras sus obras derivadas así como sus copias se reconozcan los créditos a los autores de la misma y se comparta bajo la misma licencia.

Cualquier aporte o comentario siempre son bienvenidos y pueden hacerlo a través del foro
[(http://foro.codigopython.com.ar/forum-6.html)](http://foro.codigopython.com.ar/forum-6.html) o mandándome un correo a
<contacto@codigopython.com.ar>, también es posible que me encuentren a través de Gtalk y MSN desde ese correo.

Esta aplicacion esta elaborada por Código Python (http://www.codigopython.com.ar) y todos sus
colaboradores.

## El porque del nombre:
El nombre lo tome del nombre de la funcion implementada en JavaScript en la pagina de la AFIP para verificar la validez de una CUIT y como resulta muy intuitivo y facil de recordar decidi utilizarlo y espero que esto no genere conflictos los programadores de la AFIP :).

## Instrucciones:
A continuacion ire explicando a modo de tutorial como es que funciona esCUITValida, solo a modo narrativo ya que el codigo resulta muy simple e intuitivo con lo facilmente podran seguirlo y entender su funcionamiento.
Lo primero que haremos sera convertir el argumento pasado a la funcion a string (Cadena) para poder utilizar los metodos de este como 'len', 'replace' o iterar sobre sus caracteres, una vez hecho esto a traves del metodo 'str' borramos cualquier adicional que haya ingresado el usuario ya que es muy comun usar dos guiones medios para escribir una CUIT o usar los puntos para los DNI, asi que la tarea que sigue es llamar al metodo 'replace' tres veces para quitar tanto guiones, puntos y espacios extras que pudiesen haber ingresado. Una vez que se haya pasado por estos dos pasos deberian haber solo 11 caracteres para esto utilizamos 'len' para comprobarlo en caso de no cumplir con este validacion devolmemos False y el valor que ingreso el usuario para que le demos la oportunidad al usuario de corregir cualquier error que haya tenido al tipear. Si pasa la prueba lo que sigue seria saber si los 11 caracteres que tenemos son numeros o caracteres alfanumericos cosa que no seria algo valido, esto es algo muy sensillo de comprobar utilizando el metodo isdigit() el cual devolvera True si se trata de una cadena compuesta solamente de numeros, asi que con un simple condicional 'if' podremos ver si esta condicion evalua a True o no, es decir si es verdadero o falso, despues de estas exhaustivas validaciones podemos afirmar que contamos con 11 numeros el cual es el requisito basico para continuar.
A partir de ahora comienza la parte tecnica de como se puede verificar si un numero cumple el algoritmo que impone la AFIP, este detalle no lo explicare aqui y queda como tarea para la casa.
Para obtener informacion mas detallada sobre el tema pueden visitar la Wikipedia (http://es.wikipedia.org/wiki/C%C3%B3digo_%C3%9Anico_de_Identificaci%C3%B3n_Tributaria)

## Consultas:
Para cualquier consulta no dudes en plantearla en nuestro foro
[(http://foro.codigopython.com.ar/forum-6.html)](http://foro.codigopython.com.ar/forum-6.html)

## Licencia:
Esta aplicacion esta licenciada bajo licencia GNU GPL v3


## Autor:
Alejandro Alvarez (eliluminado) <contacto@codigopython.com.ar>

## Colaboradores:
