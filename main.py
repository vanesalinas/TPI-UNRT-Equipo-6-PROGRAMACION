from catalogo import catalogo

def preguntas ():
    respuestas=[]
    
while True:
    r1 = input("¿Prefiere tomar su cafe solo, con leche o ambos? ").lower()
    if r1 in ["solo", "con leche", "ambos"]:
    respuestas.append(r1)
    break
    print("  Opción no válida. Elegí entre: solo / con leche / ambos\n")

while True:
    r2 = input("¿Que notas de sabor prefere o le gustara probar? Vainilla / Chocolate / Frutilla / Frutos secos / Pasas / Dulzor marcado / Ninguno ").lower()
    if r2 in ["vainilla", "chocolate", "frutilla", "frutos secos", "pasas", "dulzor marcado"]:

    respuestas.append(r2)
    break
    print("  Opción no válida. Revisá las opciones disponibles.\n")

while True:
    r3 = input("¿Que intensidad prefiere? Suave / Medio / Intenso ").lower()
    if r3 in ["suave", "medio", "intenso"]:

    respuestas.append(r3)
    break
    print("  Opción no válida. Elegí entre: suave / medio / intenso\n")
    
    return respuestas
    
cafe, coincidencias = recomendador(respuestas)

if cafe:
    if len(coincidencias) == 3:
        print(f"☕ Tu café ideal: {cafe['Nombre cafe']}")
        print(f"Tostadería : {cafe['Tostaderia']}")
        print(f"Origen     : {cafe['Origen']}")
        print(f"Proceso    : {cafe['Proceso']}")
        print(f"Intensidad : {cafe['Intensidad']}")
        print(f"Notas      : {cafe['Notas de sabor']}")
    else:
        print(f"No encontramos coincidencia exacta.")
        print(f"☕ Pero te recomendamos probar: {cafe['Nombre cafe']}")
        print(f"   Notas: {cafe['Notas de sabor']}")
        print(f"Coincide con tu preferencia de: {', '.join(coincidencias)}")
else:
    print("No encontramos ningún café para tu perfil.")

