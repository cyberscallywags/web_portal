# Cyber Scallywags UK — Web Portal

Web presence for **Cyber Scallywags UK** — a friendly, supportive community for clean, consistent, and technical practices in cybersecurity and technology.

> *"Empowering individuals to Play, Learn, Share and Grow together."*

This repo serves the public-facing site: the landing page, mission and team, the projects gallery, blogs and vlogs, events, and the contact form that feeds the Cyber Scallywags Neo4j graph.

## Ethos

Cyber Scallywags is community-first. The site reflects that:

- **Accessible** — plain language, big friendly typography, content aimed at newcomers and seasoned practitioners alike.
- **Playful** — vibrant gradients, animated logo, scallywag/pirate energy throughout the copy.
- **Hands-on** — content centres on real projects (DSF Companion, Python Code Nanny, Data Mining Wales, Practical Pythonista Club) rather than abstract theory.
- **Inclusive** — explicit focus on democratising access to programming and tech, especially in under-served regions (e.g. the Welsh valleys via Data Mining Wales).

The pillars on the site are **Play · Learn · Share · Grow**, and every page is meant to nudge a visitor toward one of those.

## Tech Stack

| Layer        | Choice                                              |
|--------------|-----------------------------------------------------|
| Web framework| [FastAPI](https://fastapi.tiangolo.com/) on Uvicorn |
| Templating   | Jinja2                                              |
| Frontend     | Bootstrap 5.3.3 + custom CSS (gradients, keyframes) |
| Graph DB     | Neo4j (via the official `neo4j` Python driver)      |
| Validation   | Pydantic                                            |
| Observability| Logfire (recently wired in)                         |
| Container    | Docker + docker-compose, Python 3.12-slim base      |
| Tests        | pytest, pytest-asyncio, httpx; Selenium for E2E     |

## Project Structure

```
web_portal/
├── app/
│   ├── main.py                # FastAPI app + all route handlers
│   ├── services/
│   │   ├── graphDB.py         # Neo4j driver factory
│   │   ├── service_projects.py
│   │   ├── service_events.py
│   │   └── models/            # Pydantic schemas (Project, Event, Blog)
│   ├── static/
│   │   ├── data/              # Python modules holding blog/vlog/team/project data
│   │   ├── css/, js/, images/
│   │   └── ...
│   └── templates/
│       ├── base.html          # Shared layout
│       ├── index.html         # Landing page
│       ├── auth/              # signin / signup / forgot-password (scaffolding)
│       ├── blogs/, events/, projects/
│       └── comms/forms/       # Contact form + schema
├── tests/
│   ├── unit/                  # pytest unit tests
│   └── E2E/                   # End-to-end suite (separate requirements.txt)
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env                       # Not committed — see "Configuration"
```

### Where data lives

- **Static content** (blogs, vlogs, team, projects) — Python modules under [app/static/data/](app/static/data/). Easy to edit, version-controlled, no DB round-trip.
- **Contact submissions** — written to **Neo4j** as `:Contact` nodes from `POST /api/contact` ([app/main.py:187-231](app/main.py#L187-L231)).
- **Events / projects** — currently served from in-process services; the `/api/projects` and `/api/events` endpoints are wired so the data source can be swapped to Neo4j without route changes.

## Quick Start

### Run with Docker (recommended)

```bash
cp .env.example .env   # then fill in NEO4J_* values
docker compose up --build
```

Site is served at **http://localhost:8055**.

The `app/` directory is bind-mounted into the container, and Uvicorn runs with `--reload`, so edits to templates/Python are picked up live.

### Run locally without Docker

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8055 --reload
```

## Configuration

The app expects a `.env` file at the repo root, loaded by docker-compose via `env_file:`:

| Variable        | Required | Purpose                              |
|-----------------|----------|--------------------------------------|
| `NEO4J_URI`     | yes      | e.g. `neo4j+ssc://xxxxxxxx.databases.neo4j.io` |
| `NEO4J_USER`    | yes      | Neo4j username                       |
| `NEO4J_PASSWORD`| yes      | Neo4j password                       |
| `NEO4J_DATABASE`| optional | Database name (defaults to `neo4j`)  |
| `LOGFIRE_TOKEN` | optional | Pydantic Logfire write token         |

**Format note:** docker-compose's `env_file` parser is strict — `KEY=value` only. Don't put spaces around `=`, or the variable is silently dropped and the app will crash with `KeyError` on startup.

A Logfire token leaked in commit `620c38c` should be **revoked** before reusing — generate a fresh one at <https://logfire.pydantic.dev> → Settings → Write tokens.

## Routes

### Pages

| Path                       | Template                              |
|----------------------------|---------------------------------------|
| `/`                        | `index.html` — landing                |
| `/intro`                   | `intro.html` — videos / introduction  |
| `/about`, `/mission`       | About + mission                       |
| `/specialisms`             | Skills / focus areas                  |
| `/practice`                | Practice guide                        |
| `/team`                    | Team roster                           |
| `/projects`, `/project/{slug}` | Project gallery + detail          |
| `/blogs`, `/blog/{slug}`   | Blog listing + post                   |
| `/vlogs`, `/vlogs/{slug}`  | Video listing + detail                |
| `/events`, `/event/{id}`   | Event listing + detail                |
| `/contact`                 | Contact form                          |
| `/support`                 | Support / donations                   |
| `/signup`, `/signin`, `/signout`, `/forgotten-password` | Auth scaffolding (no backend yet) |

### JSON API

| Method | Path                          | Returns                         |
|--------|-------------------------------|---------------------------------|
| GET    | `/api/projects`               | `ProjectsResponse` (paginated)  |
| GET    | `/api/projects/{slug}`        | Single project                  |
| GET    | `/api/events`                 | All events                      |
| GET    | `/api/events/{event_id}`      | Single event                    |
| POST   | `/api/contact`                | Persists a `:Contact` node in Neo4j |

## Testing

```bash
pytest tests/unit              # unit suite
pip install -r tests/E2E/requirements.txt
pytest tests/E2E               # browser-driven end-to-end checks
```

[tests/conftest.py](tests/conftest.py) is intentionally minimal — add fixtures there as the suite grows.

## Deployment

The [docker-compose.yml](docker-compose.yml) builds and runs the image `cyberscallywags/cyber-scallywags-uk:v0.2.0` on port `8055`, restarting unless explicitly stopped. The compose file mounts `./app` into the container so a hot-reload Uvicorn picks up edits — fine for staging, swap the volume out for production.

## Status & Roadmap

- Public site, projects, events, blogs, vlogs, team — **live**
- Contact form persists to Neo4j — **live**
- Logfire observability — **wired up**
- Auth (signup/signin pages exist, backend not yet implemented) — **in progress**
- Migration of static project/event data into Neo4j — **planned**
- Email notifications on contact form submissions — **planned**

## License

MIT — see [LICENSE](LICENSE).

---

*Powered by Cyber Scallywags. Building communities through technology and innovation.*
