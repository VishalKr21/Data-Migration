Features:

Batch Processing: The migration extracts and loads data in batches to handle large datasets without overwhelming memory.

State Management: The migration process is stateful, meaning it remembers where it left off and can be resumed if interrupted.

Validation: Ensures data quality before loading it into the target database.

Logging: Captures migration progress and errors for troubleshooting.

Error Handling: The project includes error handling at each stage to ensure robustness.

Scheduling: Automates the process using schedule (or replace this with Airflow for more complex pipelines).
