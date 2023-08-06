from elasticsearch import Elasticsearch

# Replace this with your Elasticsearch Cloud ID
#cloud_id = "your-elasticsearch-cloud-id"

# Connect to Elasticsearch
#es = Elasticsearch(['http://localhost:9200'])
es = Elasticsearch(cloud_id=cloud_id, http_auth=('username', 'password'))


def create_recipe_database():
    # Define the index mapping
    index_name = 'recipes'
    index_mapping = {
        'mappings': {
            'properties': {
                'title': {'type': 'text'},
                'ingredients': {'type': 'text'},
                'method': {'type': 'text'}
            }
        }
    }

    # Create the index with the specified mapping
    es.indices.create(index=index_name, body=index_mapping, ignore=400)

    # Sample recipe data
    sample_recipes = [
        {
            'title': 'Pasta Carbonara',
            'ingredients': 'Spaghetti, eggs, pancetta, Parmesan cheese, black pepper, salt',
            'method': '1. Cook spaghetti al dente. 2. Whisk eggs, cheese, and pepper. 3. Fry pancetta. 4. Combine all.'
        },
        {
            'title': 'Chocolate Brownies',
            'ingredients': 'Butter, sugar, eggs, vanilla extract, cocoa powder, flour, nuts',
            'method': '1. Melt butter and mix with sugar. 2. Add eggs and vanilla. 3. Mix cocoa, flour, and nuts. 4. Bake.'
        },
        {
            'title': 'Caesar Salad',
            'ingredients': 'Romaine lettuce, croutons, Parmesan cheese, Caesar dressing',
            'method': '1. Toss lettuce, croutons, and cheese. 2. Drizzle with Caesar dressing. 3. Mix well.'
        }
    ]

    # Insert sample recipes into Elasticsearch
    for idx, recipe in enumerate(sample_recipes):
        es.index(index=index_name, id=idx, body=recipe)

def search_recipes(search_term):
    # Define the index name
    index_name = 'recipes'

    # Example search query: Search recipes containing the given search term in the title
    search_query = {
        "query": {
            "match": {
                "title": search_term
            }
        }
    }

    # Perform the search
    search_results = es.search(index=index_name, body=search_query)

    # Process and display the search results
    if search_results['hits']['total']['value'] > 0:
        print()
        print(f"Recipes containing '{search_term}' in the title:")
        print()
        for hit in search_results['hits']['hits']:
            recipe = hit['_source']
            print()
            print(f"Title: {recipe['title']}")
            print()
            print(f"Ingredients: {recipe['ingredients']}")
            print()
            print(f"Method: {recipe['method']}")
            print()
    else:
        print("No recipes found.")

if __name__ == "__main__":
    # Create the recipe database
    create_recipe_database()

    # Search for recipes based on user input
    while True:
        print()
        search_term = input("Enter a search term (type 'exit' to quit): ")
        print()
        if search_term.lower() == 'exit':
            break
        search_recipes(search_term)
