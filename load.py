import psycopg2
import json


def load_data(db_config, data, state_file):
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    for row in data:
        cursor.execute("INSERT INTO users (id, name, age, city) VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO NOTHING",
                       (row['id'], row['name'], row['age'], row['city']))

    # Update migration state
    with open(state_file, 'w') as state:
        json.dump({"last_migrated_id": data[-1]['id']}, state)

    conn.commit()
    cursor.close()
    conn.close()
