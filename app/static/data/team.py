

def get_team_data() -> list[dict]:
    return [
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


def get_team_data_by_name(req_name: str = "Colin Moore-Hill") -> dict:
    team_data = get_team_data()
    return next((member for member in team_data if member["name"] == req_name), {})


def get_team_data_by_slug(req_slug: str = "colin-moore-hill") -> dict:
    team_data = get_team_data()
    return next((member for member in team_data if member["slug"] == req_slug), {})
