# Blog API

This project is a simple blog API built with FastAPI.

## Features

- Retrieve the full list of blog articles.
- Add a new blog article.
- Delete a blog article by ID.

## Requirements

- FastAPI
- Uvicorn

## Installation

Use `uv` to install the required packages with the following command:
```
uv install
```

## Running the Application

To run the application, use the following command:
```
uvicorn main:app --reload
```
The `--reload` flag enables auto-reloading so the server will restart after code changes.

## Linting with Ruff

To lint the application code, run:
```
ruff src/
```
To automatically fix linting issues, run:
```
ruff src/ --fix
```
Replace `src/` with the actual path to your source code if it's different.

## Endpoints

`GET /articles/` - Returns a list of all blog articles.
`POST /articles/` - Adds a new blog article. Requires a JSON body with `id`, `title`, and `content`.
`DELETE /articles/{article_id}` - Deletes the blog article with the specified `id`.

## Testing

Run tests using pytest:
```
pytest
```

## Development Notes

This API uses a simple in-memory list to store articles. In a production environment, you would typically integrate a database to persist data.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
