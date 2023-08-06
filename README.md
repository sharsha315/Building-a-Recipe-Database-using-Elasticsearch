# Building a Recipe Database using Elasticsearch

This repository contains a Python program to build a recipe database using Elasticsearch. The program allows users to create an Elasticsearch index to store recipes and search for recipes based on specific criteria.

## Requirements

- Python 3.x
- Elasticsearch server running on http://localhost:9200

## Setup

1. Install the required Python libraries using pip:

```
pip install elasticsearch
```

2. Start your Elasticsearch server on http://localhost:9200. Make sure it is up and running before running the Python program.

## How to Use

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/recipe-database.git
cd recipe-database
```

12. Run the Python program to create the recipe database and insert sample recipes:

```python
python recipes.py
```

- Once the database is created, the program will prompt you to enter a search term. You can enter a search term to find recipes that match the criteria.

- Type 'exit' to quit the search and exit the program.