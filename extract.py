import pymysql


def extract_data(db_config, last_migrated_id, batch_size=100):
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    query = f"SELECT * FROM users WHERE id > {last_migrated_id} ORDER BY id LIMIT {batch_size};"

    cursor.execute(query)
    data = cursor.fetchall()

    conn.close()
    return data
