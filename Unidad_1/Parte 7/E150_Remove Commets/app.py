def quitar_comentarios(entrada_archivoPY, salida_archivoPY):
    try:
        with open(entrada_archivoPY, 'r') as infile:
            lineas = infile.readlines()

            # Quitando comentarios
            lineas = (linea.split('#')[0] for linea in lineas)

        #Asignadole la extencion propia de Python al asrchivo de salida
        extension_salida=f"{salida_archivoPY}.py"    

        with open(extension_salida, 'w') as outfile:
            # Modificando archivo y guardandolo
            outfile.writelines(lineas)
        
        print(f"Lo comentarios han sido removido exitosamente. El nuevo archivo ha sido guardado como {
              salida_archivoPY}")

    except FileNotFoundError:
        print(f"Error. Lectura del archivo {entrada_archivoPY} no exitosa.")
    except Exception as e:
        print(f"Ha ocurrido un error {e}")


# Datos de entrada del archivo
entrada = input("Ingresa nombre o ruta del archivo: ")
salida = input("Ingresa el nombre del archivo a exportar: ")

#Pasando los parametros de entrada y salida del archivo
quitar_comentarios(entrada,salida)