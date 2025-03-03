# FastAPI Template

An opinionated template for a FastAPI project wit PostgreSQL, SQLAlchemy and uv as the package manager.
This projects implements a basic link shortener API.

## ENV File

Create a `.env` file in the root of the project and add the following 
(values also defined in `docker-compose.yml`):

```bash
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=template_db
DATABASE_USER=template_user
DATABASE_PASSWORD=TemplateDeveloperPassword
```