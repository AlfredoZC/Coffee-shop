#DEFENSA DE NICOLAS EMANUEL OLY SANCHEZ

def verificar_palindromos(nombres, index=0):
        if index == len(nombres):  
            return []
        
        
        nombre = nombres[index]
        
        
        es_palindromo = "True"  
        for i in range(len(nombre) // 2):  
            if nombre[i] != nombre[len(nombre)-1-i]:
                es_palindromo = "False" 
                break  
        
       
        return [es_palindromo] + verificar_palindromos(nombres, index + 1)
