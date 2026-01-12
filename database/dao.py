from database.DB_connect import DBConnect
from model.squadra import Squadra


class DAO:
    @staticmethod
    def get_squadre(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select t.id, t.year, t.team_code, t.name, sum(s.salary ) as salario
                    from team t, salary s 
                    where t.year=%s and t.year=s.year and s.team_code=t.team_code
                    group by t.id, t.year, t.team_code, t.name """

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(Squadra(**row))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def get_anno():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct t.year
                    from team t
                    where t.year >= 1980 """

        cursor.execute(query)

        for row in cursor:
            result.append(row["year"])

        cursor.close()
        conn.close()
        return result






