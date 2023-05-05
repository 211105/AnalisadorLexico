import re
import tkinter as tk

reservadas = ["for", "do", "while", "if", "else"]

def analizar_linea(linea):
    tokens = []
    for token in reservadas:
        matches = re.findall(r"\b{}\b".format(token), linea)
        for match in matches:
            tokens.append(f"<Reservada     {token}>   Simbolo     {token}")
            linea = linea.replace(match, " ", 1)
    matches = re.findall(r"(?<!\()(\()(?!\()", linea)
    for match in matches:
        tokens.append(f"<Parentesis apertura {match}>")
        linea = linea.replace(match, " ", 1)
    matches = re.findall(r"(?<!\))(\))(?!\))", linea)
    for match in matches:
        tokens.append(f"<Parentesis cierre {match}>")
        linea = linea.replace(match, " ", 1)
    linea = linea.strip()
    if len(linea) > 0:
        tokens.append("<No definido> {}".format(linea))
    return tokens


def analizar_codigo():
    
    codigo = entrada_texto.get("1.0", tk.END)
    lineas = codigo.split()
    tokens_totales = []
    for i, linea in enumerate(lineas):
        tokens_linea = analizar_linea(linea)
        for token in tokens_linea:
            tokens_totales.append((i+1, token))

        resultado_texto.delete("1.0", tk.END)
    for numero_linea, token in tokens_totales:
        resultado_texto.insert(tk.END, f"Linea {numero_linea}\n {token}\n")
        contador_reservadas = len([token for numero_linea, token in tokens_totales if token.startswith("<Reservada")])
        contador_Parentesis_apertura = len([token for numero_linea, token in tokens_totales if token.startswith("<Parentesis apertura")])
        contador_Parentesis_cierre = len([token for numero_linea, token in tokens_totales if token.startswith("<Parentesis cierre")])

    resultado_texto.insert(tk.END, f"Reservadas: {contador_reservadas}\n")
    resultado_texto.insert(tk.END, f"Parentesis de apertura: {contador_Parentesis_apertura}\n")
    resultado_texto.insert(tk.END, f"Parentesis de cierre: {contador_Parentesis_cierre}\n")
    





ventana = tk.Tk()
ventana.geometry("700x400")
ventana.title("Analizador de código")
ventana.config(bg="#FFFFFF")


entrada_texto = tk.Text(ventana, font=("Arial", 12), bg="#808080", fg="white", height=10, width=30)
entrada_texto.place(x=50, y=50)
entrada_texto.configure(insertbackground="#FF0000")
resultado_texto = tk.Text(ventana, font=("Arial", 12), bg="#808080", fg="white", height=10, width=35)
resultado_texto.place(x=350, y=50)

boton_analizar = tk.Button(ventana, text="Analizar", font=("Arial", 12), bg="#808080", fg="white", command=analizar_codigo)
boton_analizar.place(x=100, y=300)

boton_borrar = tk.Button(ventana, text="Limpiar", font=("Arial", 12), bg="#808080", fg="white", command=lambda: entrada_texto.delete("1.0", tk.END))
boton_borrar.place(x=500, y=300)

ventana.mainloop()
