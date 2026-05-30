from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from app.static.data import team, newsletter
from app.services.models.project_schema import Project, ProjectsResponse
from app.services import service_projects
from app.services import service_events
from app.services import service_blogs
from app.services import service_vlogs
from app.services.auth_service import authenticate_user, LoginRequest, AuthServiceError
from app.templates.comms.forms.schema.contact_form import ContactFormData
from app.services import graphDB as gdb
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.static.data.newsletter import get_all_newsletter_data
from app.static.data.newsletter import get_newsletter_data_by_slug
from app.static.data.projects import get_all_project_data
from app.static.data.projects import get_project_data_by_slug
from typing import List, Optional
from pydantic import BaseModel
import logging
import logfire


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s :: %(message)s',
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def read_root(request: Request):
    logfire.info('TRIGGERED: read_root !')  
    return templates.TemplateResponse(request, "index.html", {})


@app.get("/practice")
async def read_practice(request: Request):
    logfire.info('TRIGGERED: read_practice !')  
    return templates.TemplateResponse(request, "practice.html", {})


@app.get("/intro")
async def read_videos(request: Request, ):
    logfire.info('TRIGGERED: read_videos !')  
    return templates.TemplateResponse(request, "intro.html", {})


@app.get("/about")
async def read_about(request: Request):
    logfire.info('TRIGGERED: read_about !')  
    return templates.TemplateResponse(request, "about.html", {})


@app.get("/specialisms")
async def read_specialisms(request: Request):
    logfire.info('TRIGGERED: read_specialisms !')  
    return templates.TemplateResponse(request, "specialisms.html", {})



@app.get("/team")
async def read_team(request: Request):
    items = team.get_team_data()
    logfire.info('TRIGGERED: read_team !')  
    return templates.TemplateResponse(request, "team.html", {"team": items})


@app.get("/mission")
async def read_mission(request: Request):
    logfire.info('TRIGGERED: read_mission !')  
    return templates.TemplateResponse(request, "mission.html", {})


@app.get("/projects")
async def read_projects(request: Request):
    items = service_projects.get_all_projects()
    logfire.info('TRIGGERED: read_projects !')  
    return templates.TemplateResponse(request, "projects/projects.html", {"projects": items})


@app.get("/signup")
async def read_signup(request: Request):
    logfire.info('TRIGGERED: read_signup !')  
    return templates.TemplateResponse(request, "/auth/signup.html", {})


@app.get("/signin")
async def read_signin(request: Request):
    logfire.info('TRIGGERED: read_signin !')  
    return templates.TemplateResponse(request, "/auth/signin.html", {})


@app.get("/landing")
async def read_landing(request: Request):
    logfire.info('TRIGGERED: read_landing !')
    membership_tier = request.query_params.get("tier", "User")
    return templates.TemplateResponse(request, "landing.html", {"membership_tier": membership_tier})


@app.post("/auth/login")
async def login(login_request: LoginRequest):
    """
    Handle user login by authenticating against the auth service
    and returning access token to store in session/localStorage
    """
    try:
        logfire.info(f'TRIGGERED: login attempt for {login_request.email}')
        
        response = await authenticate_user(login_request.email, login_request.password)
        
        logfire.info(f'LOGIN SUCCESS: {login_request.email}')
        
        return {
            "access_token": response.access_token,
            "refresh_token": response.refresh_token,
            "token_type": response.token_type,
            "success": True
        }
        
    except AuthServiceError as e:
        logfire.error(f'LOGIN FAILED: {login_request.email} - {str(e)}')
        return JSONResponse(
            status_code=401,
            content={
                "success": False,
                "detail": str(e)
            }
        )
    except Exception as e:
        logfire.error(f'UNEXPECTED LOGIN ERROR: {str(e)}')
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "detail": "An unexpected error occurred during login"
            }
        )


@app.get("/signout")
async def read_signout(request: Request):
    logfire.info('TRIGGERED: read_signout !')
    return templates.TemplateResponse(request, "/auth/signout.html", {})


@app.get("/profile")
async def read_profile(request: Request):
    logfire.info('TRIGGERED: read_profile !')
    return templates.TemplateResponse(request, "auth/profile.html", {})


@app.get("/dashboard")
async def read_dashboard(request: Request):
    logfire.info('TRIGGERED: read_dashboard !')
    return templates.TemplateResponse(request, "auth/dashboard.html", {})


@app.get("/forgot-password")
async def read_forgot_password(request: Request):
    logfire.info('TRIGGERED: read_forgot_password !')  
    return templates.TemplateResponse(request, "/auth/forgot-password.html", {})


@app.get("/contact")
async def read_contact(request: Request):
    logfire.info('TRIGGERED: read_contact !')  
    return templates.TemplateResponse(request, "comms/forms/contact.html", {})


@app.get("/events")
async def read_events(request: Request):
    events = service_events.get_all_events()
    logfire.info('TRIGGERED: read_ALL_events !')  
    return templates.TemplateResponse(request, "/events/events.html", {"events": events})


@app.get("/event/{event_id}")
async def read_event_detail(request: Request, event_id: int):
    """Render event detail page"""
    logger.info(f'TRIGGERED: read_event_detail :: {event_id} !')
    event = service_events.get_event_by_id(event_id)

    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    return templates.TemplateResponse(request, "/events/event-detail.html", {
        "event": event
    })


@app.get("/support")
async def read_support(request: Request):
    logfire.info('TRIGGERED: read_support !')
    return templates.TemplateResponse(request, "/support.html", {})


@app.get("/blogs")
async def read_blogs(request: Request):
    blogs_data = service_blogs.get_all_blogs()
    logfire.info('TRIGGERED: read_ALL_blogs !')
    return templates.TemplateResponse(request, "blogs/blogs.html", {"blogs": blogs_data})


@app.get("/blog/{slug}")
async def read_blog_detail(request: Request, slug: str):
    """Render blog detail page."""
    logger.info(f'TRIGGERED: read_blog_detail :: {slug} !')
    blog = service_blogs.get_blog_by_slug(slug)

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    related = service_blogs.get_related_blogs(slug)
    return templates.TemplateResponse(request, "blogs/blog-detail.html", {
        "slug": slug,
        "blog": blog,
        "related": related,
    })


@app.get("/vlogs")
async def read_vlogs(request: Request):
    vlogs_data = service_vlogs.get_all_vlogs()
    logfire.info('TRIGGERED: read_ALL_vlogs !')
    return templates.TemplateResponse(request, "blogs/vlogs.html", {"vlogs": vlogs_data})


@app.get("/vlogs/{slug}")
async def read_vlogs_detail(request: Request, slug: str):
    """Render vlog detail page."""
    logger.info(f'TRIGGERED: read_vlogs_detail :: {slug} !')
    vlog = service_vlogs.get_vlog_by_slug(slug)

    if not vlog:
        raise HTTPException(status_code=404, detail="Vlog not found")

    related = service_vlogs.get_related_vlogs(slug)
    return templates.TemplateResponse(request, "blogs/vlog-detail.html", {
        "slug": slug,
        "vlog": vlog,
        "related": related,
    })


@app.get("/newsletter")
async def read_newsletter(request: Request):
    items = newsletter.get_all_newsletter_data()
    logfire.info('TRIGGERED: read_ALL_newsletter !')
    return templates.TemplateResponse(request, "newsletter/newsletter.html", {"newsletter": items})



@app.get("/newsletter/{slug}")
async def read_newsletter_detail(request: Request, slug: str):
    resp = get_newsletter_data_by_slug(slug)
    current = resp[0] if resp else None
    related = [n for n in get_all_newsletter_data() if n["slug"] != slug][:3]
    logger.info(f'TRIGGERED: read_newsletter_detail  :: {slug}!')
    return templates.TemplateResponse(request, "newsletter/newsletter-detail.html", {
        "slug": slug,
        "newsletter": current,
        "related": related,
    })


@app.post("/api/contact")
async def submit_contact_form(form_data: ContactFormData):
    """Handle contact form submissions and store in Neo4j"""
    try:
        driver = gdb.get_driver()
        logger.info('TRIGGERED: submit_contact_form !')

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

     
        return {
            "success": True,
            "message": "Contact form submitted successfully",
            "contact_id": contact_id
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to submit contact form: {str(e)}")





# API Endpoints for PROJECTS

@app.get("/project/{slug}")
async def read_project_detail(request: Request, slug: str):
    # Get the specific project (should return a dict, not a list)
    project_data = get_project_data_by_slug(slug)
    # Get all projects for the ProjectList in JavaScript
    all_projects = get_all_project_data()
    
    # Debug: Check what you're getting
    print(f"Project data type: {type(project_data)}")
    print(f"Project data: {project_data}")
    
    return templates.TemplateResponse(request, "projects/project-detail.html", {
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
            "demo_url": "https://mobile.dsfcompanion.uk",
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
        }, 
        {
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
        }, 
        {
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
        },
        {
            "id": 6,
            "logoRect": 'images/logo/cqc_logo.png',
            "style": 'alt="Project Emoji" style="height: 1000px; width: 100px; object-fit: cover;" class="img-fluid"',
            "title": "CQC Intelligence platform",
            "slug": "cqc-intelligence-platform",
            "description": "A platform for collaborative intelligence gathering and analysis of CQC (Care Quality Commission).",
            "emoji": "🧠",
            "status": "Planned",
            "technologies": ["python", "AI", "ML", "data-science", "Graph Neural Networks"],
            "github_url": "https://github.com/cyberscallywags/",
            "demo_url": "https://cqc.cyberscallywags.uk/",
            "contributors": [
                
                {
                    "name": "Edward Bensa - Lead",
                    "emoji": "🎨",
                    "team_slug": "edward-bensa"
                },
                {
                    "name": "Tiana Bettinson",
                    "emoji": "🌐",
                    "team_slug": "tiana-bettinson"
                }
            ],            
            "created_date": "2025-11-15",
            "last_updated": "2025-11-15",
        },
        {
            "id": 7,
            "logoRect": 'images/logo/cqc_logo.png',
            "style": 'alt="Project Emoji" style="height: 1000px; width: 100px; object-fit: cover;" class="img-fluid"',
            "title": "Disused Coal Tip Safety Monitoring",
            "slug": "disused-coal-tip-safety",
            "description": "A platform for collaborative Citizen Science intelligence gathering and analysis in support of the Welsh Assembly.",
            "emoji": "🧠",
            "status": "Planned",
            "technologies": ["python", "AI",  "data-science", "Geospatial Analysis"],
            "github_url": "https://github.com/cyberscallywags/",
            "demo_url": "https://coaltips.cyberscallywags.uk/",
            "contributors": [
                
                {
                    "name": "Colin Moore-Hill - Lead",
                    "emoji": "🌐",
                    "team_slug": "colin-moore-hill"
                }
            ],            
            "created_date": "2025-03-27",
            "last_updated": "2025-03-27",
            
        },
        {
            "id": 8,
            "logoRect": 'images/logo/cqc_logo.png',
            "style": 'alt="Project Emoji" style="height: 1000px; width: 100px; object-fit: cover;" class="img-fluid"',
            "title": "AuraDB Buddy",
            "slug": "auradb-buddy",
            "description": "A tool for managing and validating auraDB txt credentials for AuraDB.",
            "emoji": "🧠",
            "status": "Planned",
            "technologies": ["streamlit",  "AuraDB", "Credentials Management"],
            "github_url": "https://github.com/cyberscallywags/",
            "demo_url": "https://auradbuddy.cyberscallywags.uk/",
            "contributors": [
                
                {
                    "name": "Colin Moore-Hill - Lead",
                    "emoji": "🌐",
                    "team_slug": "colin-moore-hill"
                }
            ],            
            "created_date": "2025-05-01",
            "last_updated": "2025-05-01",
            
        },
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


# @app.get("/api/projects")
# async def get_all_projects_api():
#     """API endpoint to get all projects"""
#     projects = get_all_project_data()
#     return {"projects": projects}


@app.get("/api/projects/{project_slug}")
async def get_project_by_slug(project_slug: str):
    """Get a specific project by slug"""
    
    project = get_project_data_by_slug(project_slug)
    logger.info(f'TRIGGERED: get_project_by_slug (project_slug={project_slug}) !')
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    return project

# API Endpoints for EVENTS

@app.get("/api/events")
async def get_all_events_api():
    """API endpoint to get all events"""
    events = service_events.get_all_events()
    logger.info('TRIGGERED: get_ALL_events !')
    return events


@app.get("/api/events/{event_id}")
async def get_event_by_id(event_id: int):
    """Get a specific event by ID"""
    logger.info('TRIGGERED: get_event_by_id !')
    event = service_events.get_event_by_id(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


# API Endpoints for BLOGS

@app.get("/api/blogs")
async def get_all_blogs_api():
    """Return all blogs."""
    logger.info('TRIGGERED: get_ALL_blogs !')
    return service_blogs.get_all_blogs()


@app.get("/api/blogs/{slug}")
async def get_blog_by_slug_api(slug: str):
    """Return a single blog by slug."""
    logger.info(f'TRIGGERED: get_blog_by_slug :: {slug} !')
    blog = service_blogs.get_blog_by_slug(slug)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog


# API Endpoints for VLOGS

@app.get("/api/vlogs")
async def get_all_vlogs_api():
    """Return all vlogs."""
    logger.info('TRIGGERED: get_ALL_vlogs !')
    return service_vlogs.get_all_vlogs()


@app.get("/api/vlogs/{slug}")
async def get_vlog_by_slug_api(slug: str):
    """Return a single vlog by slug."""
    logger.info(f'TRIGGERED: get_vlog_by_slug :: {slug} !')
    vlog = service_vlogs.get_vlog_by_slug(slug)
    if not vlog:
        raise HTTPException(status_code=404, detail="Vlog not found")
    return vlog
