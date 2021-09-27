from conn import coneccion, closeConn
import random

class FraseMod():

    def buscaFrases():
        frases = []
        conn = coneccion()
        cursor = conn.cursor()
        
        query = 'SELECT fraseId, frase, personaje.persNombre FROM frase LEFT JOIN personaje ON frase.persId = personaje.persId'

        cursor.execute(query)
        rows = cursor.fetchall()
        closeConn(conn)

        for row in rows:
            frases.append({'id': row[0], 'frase': row[1], 'personaje': row[2]})
        
        return frases
    
    def buscaFraseRandom():
        frase = []
        conn = coneccion()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM frase')
        cant = len(cursor.fetchall())
        
        query = 'SELECT fraseId, frase, personaje.persNombre FROM frase LEFT JOIN personaje ON frase.persId = personaje.persId WHERE fraseId = {}'.format(random.randrange(cant))

        cursor.execute(query)
        rows = cursor.fetchall()
        closeConn(conn)

        for row in rows:
            # print(row)
            imagenURL = 'localhost:3000/imagen/{}'.format(row[2].replace(' ','-'))
            frase.append({'id': row[0], 'frase': row[1], 'personaje': row[2], 'imagen': imagenURL})
        
        return frase

    def buscaFraseId(id):
        frase = []
        conn = coneccion()
        cursor = conn.cursor()
        
        query = 'SELECT fraseId, frase, personaje.persNombre FROM frase LEFT JOIN personaje ON frase.persId = personaje.persId WHERE fraseId = {}'.format(id)

        cursor.execute(query)
        rows = cursor.fetchall()
        closeConn(conn)

        for row in rows:
            # print(row)
            imagenURL = 'localhost:3000/imagen/{}'.format(row[2].replace(' ','-'))
            frase.append({'id': row[0], 'frase': row[1], 'personaje': row[2], 'imagen': imagenURL})
        
        return frase

    def buscaFrasePersonaje(id):
        frase = []
        conn = coneccion()
        cursor = conn.cursor()
        
        query = 'SELECT fraseId, frase, personaje.persNombre FROM frase LEFT JOIN personaje ON frase.persId = personaje.persId WHERE personaje.persId = {}'.format(id)

        cursor.execute(query)
        rows = cursor.fetchall()
        closeConn(conn)

        for row in rows:
            # print(row)
            imagenURL = 'localhost:3000/imagen/{}'.format(row[2].replace(' ','-'))
            frase.append({'id': row[0], 'frase': row[1], 'personaje': row[2], 'imagen': imagenURL})
        
        return frase

    # def buscarPerosnajes():
    #     personajes = []
    #     conn = coneccion()
    #     cursor = conn.cursor()
        
    #     query = 'SELECT fraseId, frase, personaje.persNombre FROM frase LEFT JOIN personaje ON frase.persId = personaje.persId WHERE personaje.persId = {}'.format(id)

    #     cursor.execute(query)
    #     rows = cursor.fetchall()
    #     closeConn(conn)

    #     for row in rows:
    #         # print(row)
    #         imagenURL = 'localhost:3000/imagen/{}'.format(row[2].replace(' ',''))
    #         personajes.append({'id': row[0], 'nombre': row[1], 'imagen': imagenURL})
        
    #     return personajes
        


class Frase():
    fraseId   : int     
    frase     : str
    personaje : str

    def __init__(self, fraseId, frase, personaje):
        self.fraseId   = fraseId
        self.frase     = frase
        self.personaje = personaje


# frase = FraseMod()

# fr = frase.buscaFrases()

# for f in fr:
#     print(f.frase)