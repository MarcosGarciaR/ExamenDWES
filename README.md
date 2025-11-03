# EXAMEN 1 DWES


### Parámetros Utilizados para la creación de los Modelos
- `max_length`: Limita la longitud del texto.
- `unique`: Asegura que el valor sea único y no se repita.
- `default`: Establece un valor por defecto.
- `max_digits`: Indica un numero máximo de digitos en un campo.
- `decimal_places`: Ajusta los decimales de un número.
- `choices`: Selector entre valores establecidos .
- `validators`: Permite definir reglas personalizadas en los valores de un campo.
- `blank`: Define si el campo puede estar vacío.
- `null`: Indica si el campo puede ser nulo.
- `timezone.now`: Devuelve la fecha/hora actual.
- `models.PROTECT`: Impide que se elimine el campo si está relacionado con otro registro.
- `help_text`: Nos permite agregar un texto de ayuda.

### Parámetros Utilizados para la creación de las vistas
- `select_related`: Sirve para obtener los datos de las relaciones OneToOne, ManytoOne.
- `prefetch_related`: Sirve para obtener los datos de las relaciones ManytoMany.
- `order_by`: Nos permite ordenar los resultados de una consulta.
- `get`: Recibe cómo parámetro, la columna que desea buscar y el valor de esa columna, para obtener el registro concreto.
- `filter`: Sirve para filtrar por un campo en la base de datos, podemos usar “,” para hacer "AND".
- `Prefetch`: Permite realizar Inner Join en las relaciones inversas mediante el uso del atributo related_name.
- `__isnull=True`: Igual que el None, pero para relaciones MtM. En mi caso, la relación es MtM por lo que None no valdría, debe utilizarse 'isnull'.

### SÍMBOLOS MATEMÁTICOS DE DJANGO
- `__gt`: Nos permite buscar valores superiores al parámetro recibido (Mayor que ESTRICTO) - greater than
- `__lt`: Nos permite buscar valores inferiores al parámetro recibido (Menor que ESTRICTO) - less than
- `__gte`: Valores superiores/iguales al parámetro recibido (Mayor o igual) - greater than or equals
- `__lte`: Valores menores/iguales al parámetro recibido (Menor o igual) - greater than or equals


- `raw()`: Nos permite hacer las consultas como en SQL normal, aunque no están optimizadas.