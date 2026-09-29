from dataclasses import dataclass, asdict

import oracledb as db

@dataclass
class BoardVO:
    ID: int
    TITLE: str
    CONTENT: str

def get_connection():
    DB_USER = 'C##KH'
    DB_PASSWORD = '1234'
    DB_DSN = 'localhost:1521/xe'
    return db.connect(user = DB_USER, password = DB_PASSWORD, dsn = DB_DSN)


def print_menu():
    print('menu'.center(20, '='))
    print('0. exit')
    print('1. insert_board')
    print('2. insert_board_title')
    print('3. insert_board_by_id')
    print('4. insert_board_one')
    print('5. insert_board_list')


def choose_menu():
    print_menu()
    num = int(input('Enter a number: '))
    match num:
        case 0:
            return True
        case 1:
            insert_board()
            return False
        case 2:
            insert_board_title()
            return False
        case 3:
            insert_board_by_id()
            return False
        case 4:
            insert_board_one()
            return False
        case 5:
            insert_board_list()
            return False
        case _:
            print('wrong number')
            return False

def insert_board():
    print('게시물 작성'.center(20, '-'))
    t = input('title: ')
    c = input('content: ')
    conn = get_connection()
    cursor = conn.cursor()
    sql = 'INSERT INTO BOARD (ID, TITLE, CONTENT) VALUES (SEQ_BOARD.NEXTVAL, :title, :content)'
    sql_param = {
        'title' : t
        , 'content' : c
    }
    cursor.execute(sql, sql_param)
    conn.commit()
    print('게시물 작성 성공!')
    cursor.close()
    conn.close()

def insert_board_title():
    print('insert_board_title')

def insert_board_by_id():
    print('insert_board_by_id')

def insert_board_one():
    print('게시글 상세조회'.center(20, '-'))
    id = int(input('조회할 게시글 번호: '))
    conn = get_connection()
    cursor = conn.cursor()
    sql = 'SELECT * FROM BOARD WHERE ID = :id'
    sql_param = {
        'id' : id
    }
    cursor.execute(sql, sql_param)
    row = cursor.fetchone()
    print(row)
    print(type(row))
    conn.commit()
    cursor.close()
    conn.close()

def insert_board_list():
    print('게시물 목록 조회'.center(20, '-'))
    conn = get_connection()
    cursor = conn.cursor()
    sql = 'SELECT * FROM BOARD ORDER BY ID DESC'
    cursor.execute(sql)
    col_name_list = []
    for x in cursor.description:
        col_name = x[0]
        col_name_list.append(col_name)

    row_list = cursor.fetchall()

    vo_list = []
    for row in row_list:
        # vo = BoardVO(*row) #html 화면에 보여줄 수도 있기 때문에 틀을 만들어서 보여주는 게 좋음. 콘솔에만 띄어주면 저렇게 안해도 됨.
        # vo_list.append(vo)
        d = dict(zip(col_name_list, row))
        vo = BoardVO(**d)
        vo_list.append(vo)

    # print(vo_list)
    result= []
    for vo in vo_list:
        result.append(asdict(vo))


    print(result)

    conn.commit()
    cursor.close()
    conn.close()

    return result


if __name__ == '__main__':
    while True:
        is_finish = choose_menu()
        if is_finish == True:
            break

