from fastapi import FastAPI, Request, HTTPException
from app.static.data import team, blogs
from app.services.models.project_schema import Project, ProjectsResponse
from app.services import service_projects
from app.templates.comms.forms.schema.contact_form import ContactFormData
from app.services import graphDB as gdb 
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.static.data.blogs import get_all_blog_data 
from app.static.data.blogs import get_blog_data_by_slug 
from app.static.data.vlogs import get_all_vlog_data 
from app.static.data.vlogs import get_vlog_data_by_slug 
from app.static.data.projects import get_all_project_data
from app.static.data.projects import get_project_data_by_slug
from typing import List, Optional
from pydantic import BaseModel


app = FastAPI()

# Mount static files directory
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



@app.get("/team")
async def read_team(request: Request):
    items = team.get_team_data()
    return templates.TemplateResponse("team.html", {"request": request, "team": items})


@app.get("/mission")
async def read_mission(request: Request):
    return templates.TemplateResponse("mission.html", {"request": request})


@app.get("/projects")
async def read_projects(request: Request):
    items = service_projects.get_all_projects()
    return templates.TemplateResponse("projects/projects.html", {"request": request, "projects": items})


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
    return templates.TemplateResponse("comms/forms/contact.html", {"request": request})


@app.get("/events")
async def read_events(request: Request):
    return templates.TemplateResponse("/events.html", {"request": request})


@app.get("/support")
async def read_support(request: Request):
    return templates.TemplateResponse("/support.html", {"request": request})


@app.get("/blogs")
async def read_blogs(request: Request):
    items = blogs.get_all_blog_data()
    return templates.TemplateResponse("blogs/blogs.html", {"request": request, "blogs": items})


@app.get("/blog/{slug}")
async def read_blog_detail(request: Request, slug: str):
    # In a real app, you'd fetch the blog post by slug from your database
    resp = get_blog_data_by_slug(slug)
    # For now, we'll pass the slug to the template
    return templates.TemplateResponse("blogs/blog-detail.html", {
        "request": request,
        "slug": slug,
        "blog": resp  # Replace with actual blog data
    })



@app.get("/vlogs")
async def read_vlogs(request: Request):
    items = blogs.get_all_blog_data()
    return templates.TemplateResponse("blogs/vlogs.html", {"request": request, "blogs": items})

@app.get("/vlogs/{slug}")
async def read_vlogs_detail(request: Request, slug: str):
    resp = get_vlog_data_by_slug(slug)
    # For now, we'll pass the slug to the template
    return templates.TemplateResponse("blogs/vlogs-detail.html", {
        "request": request,
        "slug": slug,
        "vlog": resp  # Replace with actual vlog data
    })


@app.post("/api/contact")
async def submit_contact_form(form_data: ContactFormData):
    """Handle contact form submissions and store in Neo4j"""
    try:
        driver = gdb.get_driver()

        with driver.session() as session:
            # Create a contact node in Neo4j
            result = session.run("""
                CREATE (c:Contact {
                    id: randomUUID(),
                    formType: $formType,
                    name: $name,
                    email: $email,
                    role: $role,
                    message: $message,
                    consent: $consent,
                    submitted_at: datetime($submitted_at),
                    created_at: datetime()
                })
                SET c:$(c.formType)
                RETURN c.id as contact_id
            """, {
                "formType": form_data.formType,
                "name": form_data.name,
                "email": form_data.email,
                "role": form_data.role,
                "message": form_data.message,
                "consent": form_data.consent,
                "submitted_at": form_data.submitted_at
            })

            contact_record = result.single()
            contact_id = contact_record["contact_id"] if contact_record else None

        driver.close()

        return {
            "success": True,
            "message": "Contact form submitted successfully",
            "contact_id": contact_id
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to submit contact form: {str(e)}")





# API Endpoints for Projects

@app.get("/project/{slug}")
async def read_project_detail(request: Request, slug: str):
    # Get the specific project (should return a dict, not a list)
    project_data = get_project_data_by_slug(slug)
    # Get all projects for the ProjectList in JavaScript
    all_projects = get_all_project_data()
    
    # Debug: Check what you're getting
    print(f"Project data type: {type(project_data)}")
    print(f"Project data: {project_data}")
    
    return templates.TemplateResponse("projects/project-detail.html", {
        "request": request, 
        "slug": slug,
        "project": project_data,  # This should be a dict, not a list
        "all_projects": all_projects
    })


@app.get("/api/projects", response_model=ProjectsResponse)
async def get_projects():
    """Get all projects - replace this with your actual data source"""
    # This would typically fetch from your database/Neo4j
    sample_projects = [
        {
            "id": 1,
            "logo": 'images/logo/dsf_Companion_logo.png',
            "title": "DSF Companion",
            "slug": "dsf-companion",
            "description": "A digital companion for individuals to connect with the resources, support, and community in general.",
            "emoji": "🦾",
            "status": "Active",
            "technologies": ["python", "FastAPI", "Jinja2", "TypeScript", "HTML", "SCSS", "Dockerfile", "JavaScript"],
            "github_url": "https://github.com/cyberscallywags/ai-ethics-toolkit",
            "demo_url": "https://dsf.cyberscallywags.uk",
            "contributors": [
                {
                    "name": "Colin Moore-Hill",
                    "emoji": "🌐",
                    "team_slug": "colin-moore-hill"
                },
                {
                    "name": "Dean Foulds",
                    "emoji": "🎨",
                    "team_slug": "dean-foulds"
                },
                {
                    "name": "Amit ",
                    "emoji": "🎨",
                    "team_slug": "dean-foulds"
                },
                {
                    "name": "Edward Bensa",
                    "emoji": "🎨",
                    "team_slug": "dean-foulds"
                }
            ],
            "created_date": "2024-08-20",
            "last_updated": "2025-02-14"
        }, {
            "id": 2,
            "logo": 'images/logo/dsf_Companion_logo.png',
            "title": "Python Code Nanny",
            "slug": "python-code-nanny",
            "description": "An open-source platform for community-driven learning with interactive coding challenges, peer mentoring, and collaborative projects. Built to democratize access to quality programming education.",
            "emoji": "👨‍🎓",
            "status": "Planned",
            "technologies": ["python", "web-dev"],
            "github_url": "https://github.com/cyberscallywags/learning-platform",
            "demo_url": "https://pcn.cyberscallywags.uk",
            "contributors": [
                {
                    "name": "Colin Moore-Hill",
                    "emoji": ["🐍", "👩‍💻","🧠"],
                    "team_slug": "colin-moore-hill"
                },
                {
                    "name": "Kishion Layne",
                    "emoji": ["🧠"],
                    "team_slug": "kishion-layne"
                }
            ],
            "created_date": "2025-01-15",
            "last_updated": "2025-10-28"
        },
        {
            "id": 3,
            "logo": 'images/logo/dsf_Companion_logo.png',
            "title": "Data Mining Wales",
            "slug": "data-mining-wales",
            "description": "A community-driven project focused on data mining techniques and applications. And to bring technology to the valleys of Wales.",
            "emoji": "⛏️",
            "status": "Planned",
            "technologies": ["python", "ai-ml", "data-science"],
            "github_url": "https://github.com/cyberscallywags/",
            "demo_url": "https://data-mining.uk",
            "contributors": [
            ],
            "created_date": "2025-03-01",
            "last_updated": "2025-11-15"
        }, {
            "id": 4,
            "logo": 'images/logo/dsf_Companion_logo.png',
            "title": "Cyber Scallywags Community",
            "slug": "cyber-scallywags-community",
            "description": "An open-source platform for community-driven learning with interactive coding challenges and collaborative projects. Built to democratize access to quality programming education and foster inclusive learning environments.",
            "emoji": "⛏️",
            "status": "Planned",
            "technologies": ["python", "ai-ml", "data-science"],
            "github_url": "https://github.com/cyberscallywags/",
            "contributors": [
            ],
            "created_date": "2025-03-01",
            "last_updated": "2025-11-15"
        }, {
            "id": 5,
            "logo": 'images/logo/dsf_Companion_logo.png',
            "title": "Practical Pythonista Club",
            "slug": "practical-pythonista-club",
            "description": "A community-driven platform for Python enthusiasts to collaborate, learn, and share knowledge through interactive coding challenges and projects.",
            "emoji": "🐍",
            "status": "Planned",
            "technologies": ["python", "AI", "ML", "data-science", "Graph &Network Theory"],
            "github_url": "https://github.com/cyberscallywags/",
            "contributors": [
            ],
            "created_date": "2025-03-01",
            "last_updated": "2025-11-15"
        }
    ]
    
    return {
        "projects": sample_projects,
        "pagination": {
            "current_page": 1,
            "total_pages": 1,
            "total_projects": len(sample_projects),
            "projects_per_page": 9
        }
    }


@app.get("/api/projects")
async def get_all_projects_api():
    """API endpoint to get all projects"""
    projects = get_all_project_data()
    return {"projects": projects}


@app.get("/api/projects/{project_slug}")
async def get_project_by_slug(project_slug: str):
    """Get a specific project by slug"""
    
    project = get_project_data_by_slug(project_slug)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    return project

@app.get("/project/{project_slug}")
async def read_project_detail(request: Request, project_slug: str):
    """Render project detail page"""
    try:
        # Get project data from the API endpoint
        project_data = await get_project_by_slug(project_slug)
        
        return templates.TemplateResponse("projects/project-detail.html", {
            "request": request,
            "project": project_data
        })
        
    except HTTPException as e:
        if e.status_code == 404:
            return templates.TemplateResponse("projects/project-detail.html", {
                "request": request,
                "project": None,
                "error": "Project not found"
            })
        raise

