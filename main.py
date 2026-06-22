from catalogo import catalogo
def recomendador(respuestas):
    leche = respuestas[0]
    notas = respuestas[1]
    intensidad = respuestas[2]

    mejor_cafe      = None
    mejor_puntaje   = 0          

    for cafe in catalogo:
        coincide_leche = cafe["Con leche"] == leche or cafe["Con leche"] == "ambos"
        coincide_notas = notas in cafe["Notas de sabor"]
        coincide_intesidad = cafe["Intensidad"] == intensidad

        puntaje = sum([coincide_leche, coincide_notas, coincide_intesidad]) #cuenta cuantos son TRRUE

        if puntaje == 3:
            return cafe, [leche, notas, intensidad]
        
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_cafe = cafe
            mejor_coincidencias = []
            if coincide_leche:
                mejor_coincidencias.append(leche)
            if coincide_notas:
                mejor_coincidencias.append(notas)
            if coincide_intesidad:
                mejor_coincidencias.append(intensidad)
              
                respuestas = preguntas()
cafes_recomendados, coincidencias = recomendador(respuestas)

if cafes_recomendados:

    if len(coincidencias) == 3:
        cafe = cafes_recomendados[0]

        print(f"\n☕ Tu café ideal: {cafe['Nombre cafe']}")
        print(f"Tostadería : {cafe['Tostaderia']}")
        print(f"Origen     : {cafe['Origen']}")
        print(f"Proceso    : {cafe['Proceso']}")
        print(f"Intensidad : {cafe['Intensidad']}")
        print(f"Notas      : {cafe['Notas de sabor']}")

    else:
        print("\nNo encontramos una coincidencia exacta.")
        print("☕ Te recomendamos estas opciones:\n")

        for cafe in cafes_recomendados[:3]:  # muestra hasta 3 cafés
            print(f"➡ {cafe['Nombre cafe']}")
            print(f"   Tostadería: {cafe['Tostaderia']}")
            print(f"   Origen: {cafe['Origen']}")
            print(f"   Notas: {cafe['Notas de sabor']}")
            print()

        print(f"Coincidencias encontradas: {', '.join(coincidencias)}")

else:
    print("No encontramos ningún café para tu perfil.")
