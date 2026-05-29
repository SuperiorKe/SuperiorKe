#!/usr/bin/env python3
"""
Interactive GitHub Profile - Kenn Macharia
------------------------------------------
A functional demonstration of programming skills that provides
useful information and project recommendations.

Usage:
  - Run directly: python github_profile.py
  - With arguments: python github_profile.py --interest "Cloud Architecture" --name "Visitor"
  - Chat with AI: python github_profile.py --chat

Dependencies:
  - rich: pip install rich
  - anthropic: pip install anthropic  (for --chat)
  - requests: pip install requests    (for --stats)
"""

import random
import json
import argparse
import os
import time
from datetime import datetime
from typing import List, Dict, Optional, Union, Any

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.columns import Columns
from rich.rule import Rule
from rich import box

console = Console()

try:
    import requests
    REQUESTS_ENABLED = True
except ImportError:
    REQUESTS_ENABLED = False

try:
    import anthropic
    ANTHROPIC_ENABLED = True
except ImportError:
    ANTHROPIC_ENABLED = False


def typewrite(text: str, delay: float = 0.018, style: str = "") -> None:
    """Print text character by character for a live-typing effect."""
    for char in text:
        console.print(char, end="", style=style)
        time.sleep(delay)
    console.print()


class AIBuilder:
    """
    Interactive profile class that showcases skills and generates project recommendations
    based on visitor's interests. Can be run locally after cloning.
    """
    def __init__(self):
        self.name = "Kenn Macharia"
        self.role = "AI Builder"
        self.location = "Nairobi, Kenya"
        self.mission = "Directing AI agents to ship real products for Africa's informal economy"
        self.github_username = "SuperiorKe"
        self.languages = {
            "Python": {
                "level": "Expert",
                "years": 5,
                "frameworks": ["FastAPI", "Flask", "Google ADK"],
                "strengths": ["AI Agent Pipelines", "API Development", "Automation"]
            },
            "TypeScript": {
                "level": "Advanced",
                "years": 3,
                "frameworks": ["Next.js", "React", "Express"],
                "strengths": ["Full-stack product shipping", "Serverless", "E2E testing"]
            },
            "JavaScript": {
                "level": "Advanced",
                "years": 4,
                "frameworks": ["Node.js", "Express", "Payload CMS"],
                "strengths": ["Server-side Applications", "RESTful APIs"]
            }
        }
        self.cloud_skills = [
            {"name": "AWS", "level": "Certified", "services": ["Lambda", "ECS", "S3", "DynamoDB"]},
            {"name": "Google Cloud", "level": "Advanced", "services": ["Cloud Run", "Vertex AI", "ADK"]},
            {"name": "Vercel", "level": "Advanced", "focus": "Serverless product deployments"},
            {"name": "CI/CD", "level": "Advanced", "tools": ["GitHub Actions"]}
        ]
        self.interests = ["AI Agents", "Informal Economy", "Africa Tech", "Building in Public"]
        self.github = f"https://github.com/{self.github_username}"
        self.availability = self._check_availability()

        self.projects = sorted([
            {
                "name": "Sauti ya Mwananchi",
                "url": f"{self.github}/sauti-ya-mwananchi",
                "live": "https://sauti-ya-mwananchi-mu44pr45ha-uc.a.run.app",
                "tech_stack": ["Python", "FastAPI", "Google ADK", "Gemini 2.0", "Cloud Run"],
                "category": "Civic AI",
                "priority": 1,
                "description": "Cite-or-refuse civic accountability AI agent for Kenyan voters",
                "key_features": [
                    "Answers in English, Swahili, or Sheng",
                    "Custom middleware rejects uncited model responses",
                    "Grounded in Constitution of Kenya 2010 and IEBC Voter Guide"
                ]
            },
            {
                "name": "Agent Governance Platform",
                "url": f"{self.github}/AgentGovernance",
                "tech_stack": ["Node.js", "Express", "SQLite", "Socket.io", "React"],
                "category": "AI Infrastructure",
                "priority": 2,
                "description": "Zero-trust HITL infrastructure layer between AI agents and production systems",
                "key_features": [
                    "Deterministic rule engine with auto-approve/block/human routing",
                    "Real-time approval dashboard via Socket.io",
                    "Full audit log on every agent decision"
                ]
            },
            {
                "name": "RentPay",
                "url": f"{self.github}/RentPay",
                "tech_stack": ["Python", "Flask", "M-Pesa Daraja API", "Africa's Talking", "SQLite"],
                "category": "FinTech / Telco",
                "priority": 3,
                "description": "USSD rent collection with M-Pesa STK Push — no app, no data plan required",
                "key_features": [
                    "Tenants pay via feature phones over USSD",
                    "M-Pesa STK Push payment initiation",
                    "SMS invoicing and landlord dashboard"
                ]
            },
            {
                "name": "Eliana Textiles",
                "url": f"{self.github}/eliana-textiles",
                "live": "https://eliana-textiles.vercel.app",
                "tech_stack": ["React 19", "TypeScript", "Vite", "Tailwind 4", "Vercel", "Playwright"],
                "category": "E-commerce",
                "priority": 4,
                "description": "Luxury bedding storefront for a Nairobi SMB at OTC Wholesale Mall",
                "key_features": [
                    "Built in 2 days with AI Studio + Claude Code",
                    "Playwright E2E + Vitest unit test coverage",
                    "Vercel serverless backend"
                ]
            },
        ], key=lambda p: p["priority"])

        self.starter_repos = {
            "ai_agents": f"{self.github}/sauti-ya-mwananchi",
            "ecommerce": f"{self.github}/eliana-textiles",
            "governance": f"{self.github}/AgentGovernance",
            "ussd": f"{self.github}/RentPay"
        }

    def _check_availability(self) -> Dict[str, Any]:
        current_month = datetime.now().month
        current_year = datetime.now().year

        if current_month in [4, 8, 12]:
            status = "Limited Availability"
            availability_percentage = 25
        elif current_month in [1, 5, 9]:
            status = "Partial Availability"
            availability_percentage = 50
        else:
            status = "Open to Opportunities"
            availability_percentage = 90

        if availability_percentage < 30:
            project_types = ["Technical Consulting (limited hours)"]
        elif availability_percentage < 60:
            project_types = ["AI Engineering", "Founding Engineer", "Developer Relations"]
        else:
            project_types = [
                "AI Engineering",
                "Founding Engineer",
                "Developer Relations",
                "Building in Public",
                "Mentorship"
            ]

        if availability_percentage > 75:
            start_date = "Immediately"
        elif availability_percentage > 40:
            start_date = "In 2-3 weeks"
        else:
            next_month = current_month + 1 if current_month < 12 else 1
            next_year = current_year if current_month < 12 else current_year + 1
            start_date = f"{datetime(next_year, next_month, 1).strftime('%B %Y')}"

        return {
            "status": status,
            "percentage": availability_percentage,
            "project_types": project_types,
            "start_date": start_date
        }

    def recommend_project(self, interest: str) -> Dict[str, Any]:
        interest = interest.lower()
        recommendation = {
            "project_idea": "",
            "difficulty": "",
            "estimated_time": "",
            "resources": [],
            "starter_repo": "",
            "technologies": []
        }

        if any(keyword in interest for keyword in ["ai", "agents", "llm", "gemini", "claude", "machine learning", "artificial intelligence"]):
            recommendation.update({
                "project_idea": "Civic accountability AI agent with cite-or-refuse middleware",
                "difficulty": "Intermediate",
                "estimated_time": "1 day (with AI tooling)",
                "resources": [
                    "Google ADK documentation",
                    "Gemini on Vertex AI",
                    "FastAPI + Cloud Run deployment guide"
                ],
                "starter_repo": self.starter_repos["ai_agents"],
                "technologies": ["Python", "FastAPI", "Google ADK", "Gemini", "Cloud Run"]
            })
        elif any(keyword in interest for keyword in ["ecommerce", "storefront", "shop", "react", "vercel", "frontend"]):
            recommendation.update({
                "project_idea": "SMB storefront with serverless backend and full test coverage",
                "difficulty": "Beginner to Intermediate",
                "estimated_time": "2 days (with Claude Code)",
                "resources": [
                    "React 19 + Vite docs",
                    "Vercel serverless functions",
                    "Playwright E2E testing guide"
                ],
                "starter_repo": self.starter_repos["ecommerce"],
                "technologies": ["React 19", "TypeScript", "Vite", "Tailwind 4", "Vercel", "Playwright"]
            })
        elif any(keyword in interest for keyword in ["ussd", "mpesa", "sms", "africa", "kenya", "telco", "feature phone"]):
            recommendation.update({
                "project_idea": "USSD rent collection with M-Pesa STK Push",
                "difficulty": "Intermediate",
                "estimated_time": "1-2 weeks",
                "resources": [
                    "Africa's Talking USSD docs",
                    "M-Pesa Daraja API guide",
                    "Flask + SQLite quickstart"
                ],
                "starter_repo": self.starter_repos["ussd"],
                "technologies": ["Python", "Flask", "M-Pesa Daraja API", "Africa's Talking", "SQLite"]
            })
        else:
            recommendation.update({
                "project_idea": "Zero-trust HITL governance layer for AI agents",
                "difficulty": "Intermediate",
                "estimated_time": "1-2 weeks",
                "resources": [
                    "Socket.io real-time docs",
                    "Knex query builder guide",
                    "React + Vite dashboard setup"
                ],
                "starter_repo": self.starter_repos["governance"],
                "technologies": ["Node.js", "Express", "Knex", "SQLite", "Socket.io", "React"]
            })

        return recommendation

    def get_skills_by_category(self, category: str) -> List[Any]:
        categories = {
            "language": list(self.languages.keys()),
            "cloud": self.cloud_skills,
            "interests": self.interests,
            "frameworks": [
                framework
                for language in self.languages.values()
                for framework in language["frameworks"]
            ]
        }
        return categories.get(category.lower(), [])

    def get_repository_stats(self) -> Dict[str, Any]:
        if not REQUESTS_ENABLED:
            return {
                "status": "error",
                "message": "Requests library not installed. Install with 'pip install requests'"
            }

        try:
            response = requests.get(f"https://api.github.com/users/{self.github_username}/repos")
            if response.status_code == 200:
                repos = response.json()
                repos_sorted = sorted(repos, key=lambda x: x["stargazers_count"], reverse=True)
                return {
                    "status": "success",
                    "total_repos": len(repos),
                    "stars": sum(repo["stargazers_count"] for repo in repos),
                    "forks": sum(repo["forks_count"] for repo in repos),
                    "most_popular": repos_sorted[0]["name"] if repos_sorted else None,
                    "repos_by_stars": [
                        {"name": r["name"], "stars": r["stargazers_count"], "forks": r["forks_count"]}
                        for r in repos_sorted
                    ],
                    "languages": list(set(repo["language"] for repo in repos if repo["language"]))
                }
            return {
                "status": "error",
                "message": f"Could not fetch repository data. Status code: {response.status_code}"
            }
        except Exception as e:
            return {"status": "error", "message": f"Error fetching repository data: {str(e)}"}

    def _build_system_prompt(self) -> str:
        projects_text = "\n".join(
            f"- {p['name']} ({p['category']}): {p['description']}. Stack: {', '.join(p['tech_stack'])}. URL: {p['url']}"
            + (f". Live: {p['live']}" if p.get('live') else "")
            for p in self.projects
        )
        langs_text = "\n".join(
            f"- {lang}: {details['level']}, {details['years']} years, frameworks: {', '.join(details['frameworks'])}"
            for lang, details in self.languages.items()
        )
        cloud_text = "\n".join(f"- {s['name']}: {s['level']}" for s in self.cloud_skills)
        availability = self.availability

        return f"""You are an AI assistant representing Kenn Macharia's GitHub profile. Answer questions about Kenn in first person, as if you are Kenn. Be concise, direct, and confident. Reflect Kenn's personality: pragmatic builder who ships fast, focused on Africa's informal economy.

ABOUT KENN:
Name: {self.name}
Role: {self.role}
Location: {self.location}
Mission: {self.mission}
GitHub: {self.github}
Email: superiorwech@gmail.com
Company: SuperiaTech (https://superiatech.vercel.app/)

LANGUAGES:
{langs_text}

CLOUD & AI:
{cloud_text}

PROJECTS (priority order):
{projects_text}

AVAILABILITY:
Status: {availability['status']}
Open to: {', '.join(availability['project_types'])}
Can start: {availability['start_date']}

CERTIFICATIONS:
- AWS Certified Cloud Practitioner (Oct 2024)
- AWS Academy Graduate, Cloud Foundations (Dec 2024)
- Africa's Talking × Google AI Program (Oct 2025)
- KCNA in progress

Keep answers short (2-4 sentences unless more detail is asked for). If asked something you don't know about Kenn, say so honestly rather than making things up."""

    def chat(self) -> None:
        """Start an interactive AI-powered chat session about this profile."""
        if not ANTHROPIC_ENABLED:
            console.print(Panel(
                "[red]anthropic package not installed.[/red]\nRun: [bold]pip install anthropic[/bold]",
                title="Chat Unavailable", border_style="red"
            ))
            return

        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            console.print(Panel(
                "[red]ANTHROPIC_API_KEY environment variable not set.[/red]\n"
                "Export your key: [bold]export ANTHROPIC_API_KEY=your_key_here[/bold]",
                title="Chat Unavailable", border_style="red"
            ))
            return

        client = anthropic.Anthropic(api_key=api_key)
        system_prompt = self._build_system_prompt()
        history: List[Dict[str, str]] = []

        console.print(Rule("[bold cyan]Chat with Kenn's AI[/bold cyan]"))
        console.print("[dim]Ask me anything about my work, stack, availability, or projects.[/dim]")
        console.print("[dim]Type [bold]exit[/bold] or [bold]quit[/bold] to leave.\n[/dim]")

        while True:
            try:
                user_input = console.input("[bold green]You:[/bold green] ").strip()
            except (KeyboardInterrupt, EOFError):
                console.print("\n[dim]Goodbye![/dim]")
                break

            if not user_input:
                continue
            if user_input.lower() in ("exit", "quit", "bye"):
                console.print("[dim]Goodbye![/dim]")
                break

            history.append({"role": "user", "content": user_input})

            try:
                console.print("[bold cyan]Kenn:[/bold cyan] ", end="")
                full_response = ""
                with client.messages.stream(
                    model="claude-haiku-4-5-20251001",
                    max_tokens=512,
                    system=system_prompt,
                    messages=history,
                ) as stream:
                    for text in stream.text_stream:
                        console.print(text, end="")
                        full_response += text
                console.print()
                history.append({"role": "assistant", "content": full_response})
            except Exception as e:
                console.print(f"\n[red]Error: {e}[/red]")

    def print_greeting(self, visitor_name: Optional[str] = None) -> None:
        """Print a rich-formatted greeting panel."""
        current_time = datetime.now()
        if current_time.hour < 12:
            time_greeting = "Good morning"
        elif current_time.hour < 18:
            time_greeting = "Good afternoon"
        else:
            time_greeting = "Good evening"

        if visitor_name:
            greeting_line = f"{time_greeting}, [bold]{visitor_name}[/bold]. I'm Kenn — AI Builder in Nairobi."
        else:
            greeting_line = f"{time_greeting}. I'm [bold cyan]Kenn Macharia[/bold cyan] — AI Builder in Nairobi, founder of SuperiaTech."

        avail_pct = self.availability["percentage"]
        avail_color = "green" if avail_pct > 60 else ("yellow" if avail_pct > 30 else "red")
        avail_text = (
            f"[{avail_color}]{self.availability['status']}[/{avail_color}]  ·  "
            f"Can start: [bold]{self.availability['start_date']}[/bold]\n"
            f"Open to: {', '.join(self.availability['project_types'])}"
        )

        random_project = random.choice(self.projects)
        live_line = f"\n  [dim]Live →[/dim] {random_project['live']}" if random_project.get("live") else ""
        project_text = (
            f"[bold]{random_project['name']}[/bold]  [dim]({random_project['category']})[/dim]\n"
            f"  {random_project['description']}\n"
            f"  [dim]Stack:[/dim] {', '.join(random_project['tech_stack'])}\n"
            f"  [dim]GitHub →[/dim] {random_project['url']}{live_line}"
        )

        console.print()
        console.print(Panel(greeting_line, subtitle=self.mission, border_style="cyan", padding=(0, 2)))
        console.print()

        cols = Columns([
            Panel(project_text, title="[bold]Featured Project[/bold]", border_style="blue", padding=(0, 2)),
            Panel(avail_text, title="[bold]Availability[/bold]", border_style=avail_color, padding=(0, 2)),
        ], equal=True)
        console.print(cols)
        console.print()

    def print_recommendation(self, interest: str) -> None:
        """Print a rich-formatted project recommendation."""
        rec = self.recommend_project(interest)

        table = Table(box=box.ROUNDED, border_style="blue", show_header=False, padding=(0, 1))
        table.add_column("Field", style="dim", width=18)
        table.add_column("Value", style="white")

        table.add_row("Project idea", f"[bold]{rec['project_idea']}[/bold]")
        table.add_row("Difficulty", rec["difficulty"])
        table.add_row("Estimated time", rec["estimated_time"])
        table.add_row("Technologies", ", ".join(rec["technologies"]))
        table.add_row("Starter repo", f"[cyan]{rec['starter_repo']}[/cyan]")
        table.add_row("Resources", "\n".join(f"· {r}" for r in rec["resources"]))

        console.print(Panel(
            table,
            title=f"[bold cyan]Recommendation for: {interest}[/bold cyan]",
            border_style="cyan"
        ))

    def print_stats(self) -> None:
        """Print a rich-formatted GitHub stats panel."""
        with console.status("[cyan]Fetching GitHub stats...[/cyan]"):
            stats = self.get_repository_stats()

        if stats.get("status") != "success":
            console.print(Panel(f"[red]{stats.get('message')}[/red]", title="GitHub Stats", border_style="red"))
            return

        summary = Table(box=box.SIMPLE, show_header=False, padding=(0, 2))
        summary.add_column("Metric", style="dim")
        summary.add_column("Value", style="bold cyan")
        summary.add_row("Total repos", str(stats["total_repos"]))
        summary.add_row("Total stars", str(stats["stars"]))
        summary.add_row("Total forks", str(stats["forks"]))
        summary.add_row("Most popular", stats["most_popular"] or "—")
        summary.add_row("Languages", ", ".join(stats["languages"]))

        repo_table = Table(box=box.ROUNDED, border_style="blue", padding=(0, 1))
        repo_table.add_column("Repository", style="bold")
        repo_table.add_column("Stars", justify="right", style="yellow")
        repo_table.add_column("Forks", justify="right", style="cyan")
        for repo in stats["repos_by_stars"]:
            repo_table.add_row(repo["name"], str(repo["stars"]), str(repo["forks"]))

        console.print(Panel(summary, title="[bold]GitHub Overview[/bold]", border_style="cyan"))
        console.print(Panel(repo_table, title="[bold]Repositories (sorted by stars)[/bold]", border_style="blue"))

    def print_report(self) -> None:
        """Print a rich-formatted full profile report."""
        console.print(Rule(f"[bold cyan]{self.name} — {self.role}[/bold cyan]"))
        console.print(f"[dim]{self.location}  ·  {self.github}[/dim]\n")

        # Languages table
        lang_table = Table(box=box.ROUNDED, border_style="blue", padding=(0, 1))
        lang_table.add_column("Language", style="bold")
        lang_table.add_column("Level")
        lang_table.add_column("Years", justify="right")
        lang_table.add_column("Frameworks", style="dim")
        for lang, d in self.languages.items():
            lang_table.add_row(lang, d["level"], str(d["years"]), ", ".join(d["frameworks"]))

        # Cloud table
        cloud_table = Table(box=box.ROUNDED, border_style="blue", padding=(0, 1))
        cloud_table.add_column("Platform", style="bold")
        cloud_table.add_column("Level")
        for s in self.cloud_skills:
            cloud_table.add_row(s["name"], s["level"])

        console.print(Columns([
            Panel(lang_table, title="[bold]Languages[/bold]", border_style="cyan"),
            Panel(cloud_table, title="[bold]Cloud & AI[/bold]", border_style="cyan"),
        ], equal=True))

        # Projects
        console.print()
        console.print(Rule("[bold]Selected Work[/bold]"))
        for p in self.projects:
            live_line = f"\n  [dim]Live →[/dim] [cyan]{p['live']}[/cyan]" if p.get("live") else ""
            features = "\n".join(f"  [dim]·[/dim] {f}" for f in p["key_features"])
            console.print(Panel(
                f"[bold]{p['name']}[/bold]  [dim]({p['category']})[/dim]\n"
                f"{p['description']}\n\n"
                f"[dim]Stack:[/dim] {', '.join(p['tech_stack'])}\n"
                f"[dim]GitHub →[/dim] [cyan]{p['url']}[/cyan]{live_line}\n\n"
                f"{features}",
                border_style="blue",
                padding=(0, 2)
            ))

        # Availability
        avail_pct = self.availability["percentage"]
        avail_color = "green" if avail_pct > 60 else ("yellow" if avail_pct > 30 else "red")
        console.print(Panel(
            f"[{avail_color}]{self.availability['status']}[/{avail_color}]  ·  "
            f"Can start: [bold]{self.availability['start_date']}[/bold]\n"
            f"Open to: {', '.join(self.availability['project_types'])}\n\n"
            f"[dim]Contact:[/dim] superiorwech@gmail.com  ·  {self.github}",
            title="[bold]Availability & Contact[/bold]",
            border_style=avail_color
        ))

    def to_json(self) -> str:
        profile_dict = {k: v for k, v in self.__dict__.items() if not k.startswith('_') and not callable(v)}
        return json.dumps(profile_dict, indent=2)

    def save_profile(self, format_type: str = "json", filename: Optional[str] = None) -> str:
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            ext = "json" if format_type.lower() == "json" else "txt"
            filename = f"kenn_profile_{timestamp}.{ext}"

        with open(filename, 'w') as f:
            if format_type.lower() == "json":
                f.write(self.to_json())
            else:
                # Plain text fallback for save
                console.print(f"[dim]Saving text report to {filename}...[/dim]")
                lines = [
                    f"{self.name} — {self.role}",
                    f"{self.location}",
                    "",
                    f"Mission: {self.mission}",
                    "",
                    "Projects:",
                ]
                for p in self.projects:
                    lines.append(f"  {p['name']} — {p['description']}")
                    lines.append(f"    Stack: {', '.join(p['tech_stack'])}")
                    lines.append(f"    {p['url']}")
                    if p.get("live"):
                        lines.append(f"    Live: {p['live']}")
                    lines.append("")
                lines.append(f"Availability: {self.availability['status']}")
                lines.append(f"Contact: superiorwech@gmail.com")
                f.write("\n".join(lines))

        return os.path.abspath(filename)


def main():
    parser = argparse.ArgumentParser(description='Interactive developer profile for Kenn Macharia')
    parser.add_argument('--interest', type=str, help='Get project recommendations for your interest')
    parser.add_argument('--name', type=str, help='Your name for a personalized greeting')
    parser.add_argument('--stats', action='store_true', help='Show GitHub repository statistics')
    parser.add_argument('--save', choices=['json', 'text'], help='Save profile to file in specified format')
    parser.add_argument('--report', action='store_true', help='Generate a formatted profile report')
    parser.add_argument('--chat', action='store_true', help='Chat with an AI that knows this profile (requires ANTHROPIC_API_KEY)')
    args = parser.parse_args()

    me = AIBuilder()

    if args.chat:
        me.chat()
        return

    me.print_greeting(args.name)

    if args.interest:
        me.print_recommendation(args.interest)

    if args.stats:
        me.print_stats()

    if args.report:
        me.print_report()

    if args.save:
        filepath = me.save_profile(format_type=args.save)
        console.print(f"\n[green]Profile saved to:[/green] {filepath}")

    if not any([args.interest, args.stats, args.report, args.save]):
        console.print("[dim]Try these commands:[/dim]")
        tips = Table(box=box.SIMPLE, show_header=False, padding=(0, 1))
        tips.add_column("Command", style="cyan")
        tips.add_column("Description", style="dim")
        tips.add_row("python github_profile.py --interest 'AI agents'", "Get a project recommendation")
        tips.add_row("python github_profile.py --name 'Your Name'", "Personalized greeting")
        tips.add_row("python github_profile.py --stats", "Live GitHub repo stats")
        tips.add_row("python github_profile.py --report", "Full profile report")
        tips.add_row("python github_profile.py --chat", "Chat with Kenn's AI (needs ANTHROPIC_API_KEY)")
        console.print(tips)


if __name__ == '__main__':
    main()
