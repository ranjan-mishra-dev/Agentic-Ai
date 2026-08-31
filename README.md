## Problem Statement 1

Build an automated movie information processing pipeline that parses raw, unstructured movie descriptions, converts them into validated structured JSON (extracting title, director, cast, release year, genre, and ratings), and stores the records directly into a database.

![Movie Pipeline Workflow](./screenshots/pipeline_overview.png)

> **Overview**: The pipeline takes free-form text input, enforces schema validation with Pydantic, and stores persistent documents in MongoDB.