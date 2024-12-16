from itertools import tour
from typing import List
from Tour import Tour
from pymysql import MySQLError
from DBConnection import DBConnection

class TourRepDB:
    def __init__(self, host, user, password, database, port=3306):
        self.db = DBConnection(host, user, password, database, port).get_connection()

    def get_by_id(self, tour_id: int) -> Tour:
        with self.db.cursor() as cursor:
            sql = "SELECT * FROM tours WHERE tour_id = %s"
            cursor.execute(sql, (tour_id,))
            result = cursor.fetchone()
            if result:
                return Tour(
                    tour_id=result['tour_id'],
                    name=result['name'],
                    description=result['description'],
                    price=result['price'],
                    duration=result['duration'],
                    climat=result['climat'],
                    tour_code=result['tour_code']
                )
            return None

    def get_k_n_short_list(self, k: int, n: int) -> List[Tour]:
        offset = (n - 1) * k
        with self.db.cursor() as cursor:
            sql = "SELECT tour_id, name, price, tour_code FROM tours LIMIT %s OFFSET %s"
            cursor.execute(sql, (k, offset))
            results = cursor.fetchall()
            return [
                Tour(
                    tour_id=row['tour_id'],
                    name=row['name'],
                    price=row['price'],
                    tour_code=row['tour_code']
                ) for row in results
            ]

    def add(self, tour: Tour):
        try:
            query = """
                INSERT INTO tours (name, description, price, duration, climat, tour_code)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (tour.name, tour.description, tour.price, tour.duration,
                      tour.climat, tour.tour_code)

            with self.db.cursor() as cursor:
                cursor.execute(query, values)
                self.db.commit()
        except MySQLError as e:
            if e.args[0] == 1062:
                raise ValueError(f"Tour with code {tour.tour_code} already exists.")
            else:
                raise Exception("An unexpected error occurred while adding the tour.")

    def update_by_id(self, tour_id: int, tour: Tour) -> bool:
        with self.db.cursor() as cursor:
            sql = """
                UPDATE tours
                SET name = %s, description = %s, price = %s, 
                    duration = %s, climat = %s, tour_code = %s
                WHERE tour_id = %s
            """
            cursor.execute(sql, (
                tour.name,
                tour.description,
                tour.price,
                tour.duration,
                tour.climat,
                tour.tour_code,
                tour_id
            ))
            self.db.commit()
            return cursor.rowcount > 0

    def delete_by_id(self, tour_id: int) -> bool:
        with self.db.cursor() as cursor:
            sql = "DELETE FROM tours WHERE tour_id = %s"
            cursor.execute(sql, (tour_id,))
            self.db.commit()
            return cursor.rowcount > 0

    def get_count(self) -> int:
        with self.db.cursor() as cursor:
            sql = "SELECT COUNT(*) AS count FROM tours"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result['count'] if result else 0

    def close(self):
        self.db.close()

tour1 = Tour.create_new_tour(
            name="Золотое кольцо Абхазии",
            description="Однодневная экскурсия по всем достопримечательностям",
            price=2000,
            duration=5,
            climat="Субтропики"
            tour_code="123456"
        )
db = DBConnection(host='localhost', user='root', password='11062003', database='tours', port=3306)
tour_repo = TourRepDB(host="localhost", user="root", password="11062003", database="tours", port=3306)
tour_repo.delete_by_id(1)
