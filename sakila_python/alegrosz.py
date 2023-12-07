from psycopg3 import connect, OperationalError

try:
    cnx = connect(
        user='postgres',
        password='coderslab',
        host='localhost',
        port='5433',
        database='postgres'
    )

    cursor = cnx.cursor()
    print('Connected')
except OperationalError as err:
    print('Connection error')
    raise ValueError(f'Connection error: {err}')

query_create_tb_user = sql.SQL("""
    CREATE TABLE IF NOT EXISTS {table_name} (
    id SERIAL,
    name VARCHAR(45),
    email VARCHAR(45) UNIQUE,
    password VARCHAR(60) DEFAULT 'ala',
    PRIMARY KEY (id)
""").format(table_name=sql.Identifier('User'))


query_create_tb_adress = sql.SQL("""
    CREATE TABLE IF NOT EXISTS {table_name} (
    id SERIAL PRIMARY KEY,
    street VARCHAR(45),
    city VARCHAR(45),
    notes TEXT,
    user_id SMALLINT,
    FOREIGN KEY (user_id) REFERENCES {table_name_foreign} (id)
""").format(table_name=sql.Identifier('Adress'),
            table_name_foreign=sql.Identifier('User'),
)

query_insert_user_tb = sql.SQL("""
    INSERT INTO {table_name}(name, email, password)
    VALUES (%s, %s, %s)
""").format(table_name=sql.Identifier('USER'))

query_update_user_tb = sql.SQL("""
    UPDATE {table_name} SET password=%s WHERE id=%s
""").forma(table_name=sql.Identifier('User'))

query_update_user_tb = sql.SQL("""
    DELETE FROM {table_name} WHERE name=%s
""").forma(table_name=sql.Identifier('User'))

query_alter = sql.SQL("""
    ALTER TABLE (table_name) ADD COLUMN price(7,2) DEFAULT 0
""").format(table_name=sql.Identifier('User'))

query_alter2 = sql.SQL("""
    ALTER TABLE {table_name} ADD COLUMN date_of_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
""").format(table_name=sql.Identifier('Adress'))

query_select = sql.SQL("""
    SELECT * FROM {table_name}
""").format(table_name+sql.Identifier(table_name))



with cnx:
    # try:
    #     cursor.execue(query_insert_user_tb), ('Ala', 'a@a.pl', 'michal_dworczyk2024'))
    # except DatabaseError as error:
    #     print(Error)
    # try:
    #     cursor.execute(query_delete_user_tb, ('Ala'))
    # except: DatabaseError as err:
    #     prin('Error')
    # try:
    #     cursor.execute(query_alter)
    # except DatabaseError as err:
    #     print('Error')
    # try:
    #      cursor.execute(query_create_tb_adress)
    # except DatabaseError as error:
    #     print(error)
    # try:
    #     cursor.execute(query_alter2)
    # except DatabaseError as error:
    #     print(error)
    try:
        cursor.exectue(query_select)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

    except DatabaseError as error:
        print(error)