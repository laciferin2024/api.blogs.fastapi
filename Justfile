set shell := ["sh", "-c"]
set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]
#set allow-duplicate-recipe
#set positional-arguments
#set dotenv-load
set dotenv-filename := ".env"
# set dotenv-filename := ".env.intel"
set export

setup:
  uv 

dev:
  uvx uvicorn main:app --reload

deps:
  uv pip freeze > requirements.txt