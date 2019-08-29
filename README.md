I'm such a newbie that I created this project from scratch in a local computer and when it crashed, I had only stored this version here. I'm not even sure it works, but I'm currently onto other things so I can't start all over again.

It has an excel sheet with a financial model of a bitcoin mining operation, and then several modules do lots of calculations daily on that financial model, using the openpyxl python library, to calculate the profitability of several mining operations depending on several mining devices. It retrieves the data mostly from a bitcoin full node and a couple of other websites that it parses.

The text below is an explanation (unfortunately in Spanish only for now, with what each of the modules is doing)

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
