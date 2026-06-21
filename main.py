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