# 🚀 FastAPI Template

An opinionated template for a FastAPI project with PostgreSQL, async SQLAlchemy, and `uv` as the package manager.

## 🎉 Demo Project

This project implements a basic link shortener API. It allows you to create a short link for a given URL and redirect to
the original URL using the short link.

Optionally, you can add an expiration date to the short link, making it invalid after the specified date.

### Decisions

#### Controller

I prefer using FastAPI for its ease of use and neat features, such as automatic OpenAPI documentation generation,
dependency injection, and Pydantic integration.

#### Database

I chose PostgreSQL because it is a powerful and reliable database system. It also supports arrays and JSON fields,
which can be useful for certain use cases.

For the ORM, I use SQLAlchemy in async mode to leverage Python's asyncio capabilities.
This improves scalability by allowing efficient handling of database connections in high-concurrency environments.

With SQLAlchemy 2.0, the new asynchronous API integrates well with FastAPI. Migrations are managed using Alembic,
which also supports async operations.

If the team is more comfortable with raw SQL, I would use asyncpg or psycopg directly.

#### Testing

Pytest provides useful features for testing, such as fixtures and parameterized tests, and it has a rich ecosystem of
plugins.

Since I am not using PostgreSQL-specific features, I use an in-memory SQLite with `aiosqlite` database for testing.
Otherwise, I would use Testcontainers to replicate the production environment. While Testcontainers ensure accuracy,
they introduce a performance penalty and require proper setup.

## 🛠️ Setup

This project can be started using Docker Compose or by starting PostgreSQL and the controller locally.

### 🐳 Docker Compose

A general build process first starts the PostgreSQL container, then applies the Alembic migrations, and finally starts
the FastAPI controller.

```shell
docker-compose up --build
```