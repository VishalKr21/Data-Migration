import yaml
import json
from extract import extract_data
from transform import transform_data
from validate import validate_data
from load import load_data
from logger import logger

# Load config
with open('config/db_config.yaml', 'r') as f:
    config = yaml.safe_load(f)


def run_migration():
    with open('migrations/migration_state.json', 'r') as state_file:
        state = json.load(state_file)
        last_migrated_id = state.get('last_migrated_id', 0)

    try:
        # Step 1: Extract data
        data = extract_data(config['source_db'], last_migrated_id)

        # Step 2: Transform data
        transformed_data = transform_data(data)

        # Step 3: Validate data
        validate_data(transformed_data)

        # Step 4: Load data into the target database
        load_data(config['target_db'], transformed_data, 'migrations/migration_state.json')

        logger.info(f"Successfully migrated {len(transformed_data)} records starting from ID {last_migrated_id}.")

    except Exception as e:
        logger.error(f"Error during migration: {str(e)}")


if __name__ == "__main__":
    run_migration()
