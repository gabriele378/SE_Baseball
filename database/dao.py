from database.DB_connect import DBConnect
from model.salary import Salary
from model.team import Team


class DAO:
    @staticmethod
    def get_team(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT id, name, year,
                    (SELECT count(*) 
                     FROM team t2
                     WHERE t2.year >= 1980 and t2.year = %s) AS NumeroSquadre
                    FROM team t1
                    WHERE t1.year >= 1980 and t1.year = %s"""

        cursor.execute(query,(year,))

        for row in cursor:
            result.append(Team(row['id'], row['name'], row['year'], row['NumeroSquadre']))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_salary():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT team_code SUM(salary) AS somma_stipendi
                    FROM salary
                    GROUP BY team_code"""


        cursor.execute(query)

        for row in cursor:
            result.append((row['team_code'], row['somma_stipendi']))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_year():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT DISTINCT year
                FROM team
                WHERE year >= 1980
                ORDER BY year
            """
        cursor.execute(query)
        for row in cursor:
            result.append(row['year'])
        cursor.close()
        conn.close()
        return result

