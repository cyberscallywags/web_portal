from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/practice")
async def read_practice(request: Request):
    return templates.TemplateResponse("practice.html", {"request": request})


@app.get("/intro")
async def read_videos(request: Request, ):
    return templates.TemplateResponse("intro.html", {"request": request})


@app.get("/about")
async def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})


@app.get("/specialisms")
async def read_specialisms(request: Request):
    return templates.TemplateResponse("specialisms.html", {"request": request})

@app.get("/blogs")
async def read_blogs(request: Request):
    items = "BLOGS"
    return templates.TemplateResponse("blogs.html", {"request": request, "blogs": items})

@app.get("/team")
async def read_team(request: Request):
    items = TEAM
    return templates.TemplateResponse("team.html", {"request": request, "team": items})


@app.get("/mission")
async def read_mission(request: Request):
    return templates.TemplateResponse("mission.html", {"request": request})


@app.get("/projects")
async def read_projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})


@app.get("/signup")
async def read_signup(request: Request):
    return templates.TemplateResponse("/auth/signup.html", {"request": request})


@app.get("/signin")
async def read_signin(request: Request):
    return templates.TemplateResponse("/auth/signin.html", {"request": request})


@app.get("/signout")
async def read_signout(request: Request):
    return templates.TemplateResponse("/auth/signout.html", {"request": request})


@app.get("/forgotten-password")
async def read_forgot_password(request: Request):
    return templates.TemplateResponse("/auth/forgot-password.html", {"request": request})


@app.get("/contact")
async def read_contact(request: Request):
    return templates.TemplateResponse("/contact.html", {"request": request})

@app.get("/support")
async def read_support(request: Request):
    return templates.TemplateResponse("/support.html", {"request": request})

@app.get("/blog/{slug}")
async def read_blog_detail(request: Request, slug: str):
    # In a real app, you'd fetch the blog post by slug from your database
    # For now, we'll pass the slug to the template
    return templates.TemplateResponse("blog-detail.html", {
        "request": request, 
        "slug": slug,
        "blog": None  # Replace with actual blog data
    })

@app.get("/project/{slug}")
async def read_project_detail(request: Request, slug: str):
    # In a real app, you'd fetch the project by slug from your database
    # For now, we'll pass the slug to the template
    return templates.TemplateResponse("project-detail.html", {
        "request": request, 
        "slug": slug,
        "project": None  # Replace with actual project data
    })




# --- Replace this with your real team data ---
TEAM: list[dict] = [
    {
        "name": "Colin Moore-Hill",
        "role": "Founder & Chief Gopher",
        "bio": "Graph enthusiast and long-time DSF collaborator. Loves turning open data archives into living knowledge.",
        "cartoon": "/static/images/team/colin/team.png",
        "photo": "/static/images/team/colin/pic.jpeg",
        "links": {
            "LinkedIn": "https://www.linkedin.com/in/colinmoorehill/",
            "GitHub": "https://github.com/Spanarchian",
            "X/Twitter": "https://x.com/CyberScallywags"
        }
    },
    {
        "name": "Kishion Layne",
        "role": "CEO",
        "bio": "Data management & governance. Advocate for open knowledge and community learning.",
        "cartoon": "/static/images/team/kishion/team.png",
        "photo": "/static/images/team/kishion/pic.jpeg",
        "links": {
            "LinkedIn": "https://www.linkedin.com/in/kishion-layne-b6b2a81b1/",
            "GitHub": "https://github.com/klayne02",
            "X/Twitter": "https://twitter.com"
        }
    },
    {
        "name": "Dean Foulds",
        "role": "Chief Scientic Technologist",
        "bio": "Bridges product vision with technical knowledge. Makes the magic happen!",
        "cartoon": "/static/images/team/dean/team.png",
        "photo": "/static/images/team/dean/pic.jpeg",
        "links": {
            "LinkedIn": "https://www.linkedin.com/in/dean-foulds/",
            "GitHub": "https://github.com/Dean-Foulds",
            "X/Twitter": "https://twitter.com"
        }
    },
    {
        "name": "Fran Moore-Hill",
        "role": "Chief Operations Officer",
        "bio": "Bridges product vision with community needs. Keeps the experience welcoming and useful.",
        "cartoon": "/static/images/team/fran/HairyCoo.jpeg",
        "photo": "/static/images/team/fran/HairyCoo.jpeg",
        "links": {
            "LinkedIn": "https://www.linkedin.com",
            "GitHub": "https://github.com",
            "X/Twitter": "https://twitter.com"
        }
    },
    {
        "name": "Amit Kumar",
        "role": "ML/AI Associate",
        "bio": "Excellent Digital magician helping turn Data into Insights",
        "cartoon": "/static/images/team/amit/team.png",
        "photo": "/static/images/team/amit/pic.jpeg",
        "links": {
            "LinkedIn": "https://www.linkedin.com/in/amitkumar1454/",
            "GitHub": "https://github.com/Phoenix1454",
            "Website": "https://www.amit-kumar.tech/"
        }
    },
    {
        "name": "Edward Bensa",
        "role": "ML/AI Associate",
        "bio": "A magical prompter and excellent Data Storyteller",
        "cartoon": "/static/images/team/edward/team.png",
        "photo": "/static/images/team/edward/pic.jpeg",
        "links": {
            "LinkedIn": "https://www.linkedin.com/in/edwardbensa/",
            "GitHub": "https://github.com/edwardbensa",
            "Website": "https://github.com/edwardbensa"
        }
    },
]