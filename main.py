from catalogo import catalogo

def preguntas ():
    respuestas=[]

    r1 = input("¿Prefiere tomar su cafe solo, con leche o ambos? ").lower()
    respuestas.append(r1)

    r2 = input("¿Que notas de sabor prefere o le gustara probar? Vainilla / Chocolate / Frutilla / Frutos secos / Pasas / Dulzor marcado / Ninguno ").lower()
    respuestas.append(r2)

    r3 = input("¿Que intensidad prefiere? Suave / Medio / Intenso ").lower()
    respuestas.append(r3)
    
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

