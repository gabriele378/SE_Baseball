from database.DB_connect import DBConnect
from model.squadra import Squadra


class DAO:
    @staticmethod
    def read_anni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select  distinct t.year
                    from team t
                    where year >= 1980 """

        cursor.execute(query)

        for row in cursor:
            result.append(row['year'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_squadre(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select name, team_code
                    from team 
                    where year = %s """

        cursor.execute(query,(anno,))

        for row in cursor:
            result.append(Squadra(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_stipendi(anno):
        conn = DBConnect.get_connection()

        result = {}

        cursor = conn.cursor(dictionary=True)
        query = """ select team_code, SUM(salary) as stipendio_tot
                    from salary
                    where year = %s
                    group by team_code """

        cursor.execute(query, (anno,))

        for row in cursor:
            result[row['team_code']] = row['stipendio_tot']  # ho un dizionario che ha come chiave il team_code e come valore lo stipendio totale della squadra

        cursor.close()
        conn.close()
        return result