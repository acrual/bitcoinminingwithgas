Si you ejecuto el fichero ejecuta en este ordenador, la otra máquina debería
estar con el nodo de bitcoin corriendo y actualizado.

RunProceso de Windows debería llamar en ubuntu a:

- LecturaPrecios
- LecturaNet_Hash_Rate
- Asegurarme de que csvcomputer está bien relleno
- en python-bitcoinlib llamar a prueba2.py
- Con todo esto ejecutar rellenarExcel.py
- Con todo ello ejecutar apirun de ubuntu

En Windows:

- A continuación, en este ordenador hay que ejecutar rellenarExcel2
- Con la tabla excel_hash_rate rellena, vamos al fichero de excel y actualizamos la hoja net_hash_rate
- Otro fichero de python debería ejecutar las dos macros dentro de la hoja
- Luego apirun debería ejecutar panditas y sacar los datos de $/mmbtu de la hoja
- Deberíamos con esto poder sacarlos en pantalla o imprimirlos en twitter 