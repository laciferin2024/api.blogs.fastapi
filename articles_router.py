from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Article(BaseModel):
    id: int
    title: str
    content: str

articles = []

@router.get("/", response_model=List[Article])
async def get_articles():
    return articles

@router.post("/", response_model=Article)
async def add_article(article: Article):
    articles.append(article)
    return article

@router.delete("/{article_id}", status_code=204)
async def delete_article(article_id: int):
    global articles
    articles = [article for article in articles if article.id != article_id]
    return
