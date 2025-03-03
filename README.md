# 🚀 FastAPI Template

An opinionated template for a FastAPI project with PostgreSQL, SQLAlchemy, and `uv` as the package manager.

## 🎉 Demo Project

This project implements a basic link shortener API. It allows you to create a short link for a given URL and redirect to the original URL using the short link.

Optionally, you can add an expiration date to the short link, which will make it invalid after the given date.

## 🛠️ Setup

This project can be started using Docker Compose or by starting PostgreSQL and the controller locally.

### 🐳 Docker Compose

A general build starts first the PostgreSQL container, then it applies the Alembic migrations, and finally starts the FastAPI Controller.

```shell
docker-compose up --build