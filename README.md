# Гена, вот тот самый API, который ты просил
По пути **/categories_and_products/** возвращается следующий [json](out.json):
```json
{
  "categories": [
    {
      "id": 1,
      "name": "food",
      "parent_id": null,
      "subcategories": [3, 4, 5],
      "product_ids": []
    },
    {
      "id": 3,
      "name": "vegetables",
      "parent_id": 1,
      "subcategories": [],
      "product_ids": [3, 4]
    },
    {
      "id": 4,
      "name": "fruits",
      "parent_id": 1,
      "subcategories": [],
      "product_ids": [1, 2]
    },
    {
      "id": 5,
      "name": "sweets and candies",
      "parent_id": 1,
      "subcategories": [6, 7],
      "product_ids": []
    },
    {
      "id": 6,
      "name": "chocolate",
      "parent_id": 5,
      "subcategories": [],
      "product_ids": [5, 6]
    },
    {
      "id": 7,
      "name": "cookies",
      "parent_id": 5,
      "subcategories": [],
      "product_ids": [7, 8]
    }
  ],
  "products": [
    {
      "id": 1,
      "name": "apple",
      "category_id": 4,
      "cost": 322.0,
      "description": "яблоко"
    },
    {
      "id": 2,
      "name": "pear",
      "category_id": 4,
      "cost": 228.0,
      "description": "груша"
    },
    {
      "id": 3,
      "name": "potato",
      "category_id": 3,
      "cost": 123.0,
      "description": "картошка"
    },
    {
      "id": 4,
      "name": "tomato",
      "category_id": 3,
      "cost": 651.0,
      "description": "помидоры"
    },
    {
      "id": 5,
      "name": "alpen gold",
      "category_id": 6,
      "cost": 100.0,
      "description": "С орешками"
    },
    {
      "id": 6,
      "name": "milka",
      "category_id": 6,
      "cost": 150.0,
      "description": "с карамелью"
    },
    {
      "id": 7,
      "name": "oreo",
      "category_id": 7,
      "cost": 150.0,
      "description": "mmmm"
    },
    {
      "id": 8,
      "name": "ginger cookie",
      "category_id": 7,
      "cost": 111.0,
      "description": "Hashire sori yo\r\nKaze no you ni\r\nTsukimihara wo\r\nPadoru Padoru"
    }
  ]
}
```
