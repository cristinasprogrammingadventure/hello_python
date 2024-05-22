
# Abre el archivo .md y lee su contenido
with open('C:/Users/Buba/Desktop/hello_python/Lab2_109/readme_lab109.md', 'r') as file:
    markdown_content = file.read()

# Imprime el contenido del archivo Markdown
print(markdown_content)

# Definimos una Adición con números enteros, o de tipo 'integer'
add=(2+2)
print(add)

# sumamos y restamos 2 números enteros como si se tratase de una calculadora, sin definir previamente una variable.
2+2
4-2
# ---> TypeError: 'int' object is not iterable 
# ---> vemos que en VS (al contrario de Jupyter) no se ejecutan estas líneas, sino sólo las que tienen una función asociada

# vamos a usar una funcón de impresión en pantalla para sumar números
print(2 + 2)
print(4 + 2)

