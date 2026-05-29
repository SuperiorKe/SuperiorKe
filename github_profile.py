#!/usr/bin/env python3
"""
Interactive GitHub Profile - Kenn Macharia
------------------------------------------
A functional demonstration of programming skills that provides
useful information and project recommendations.

Usage:
  - Run directly: python github_profile.py
  - With arguments: python github_profile.py --interest "Cloud Architecture" --name "Visitor"
  
Dependencies:
  - termcolor: pip install termcolor
  - requests: pip install requests (for GitHub API integration)
"""

import random
import json
import argparse
import os
from datetime import datetime
from typing import List, Dict, Optional, Union, Any

try:
    from termcolor import colored
    COLORS_ENABLED = True
except ImportError:
    # Fallback if termcolor isn't installed
    def colored(text, color=None, **kwargs):
        return text
    COLORS_ENABLED = False

try:
    import requests
    REQUESTS_ENABLED = True
except ImportError:
    REQUESTS_ENABLED = False


class AIBuilder:
    """
    Interactive profile class that showcases skills and generates project recommendations
    based on visitor's interests. Can be run locally after cloning.
    """
    def __init__(self):
        """Initialize with personal and professional information."""
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
        
        # Projects information with tech stacks and descriptions
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

        # Repositories for starter projects
        self.starter_repos = {
            "ai_agents": f"{self.github}/sauti-ya-mwananchi",
            "ecommerce": f"{self.github}/eliana-textiles",
            "governance": f"{self.github}/AgentGovernance",
            "ussd": f"{self.github}/RentPay"
        }
    
    def _check_availability(self) -> Dict[str, Any]:
        """
        Check current availability for new projects based on current date.
        This simulates real-world availability that changes throughout the year.
        
        Returns:
            Dict containing availability status and project types
        """
        current_month = datetime.now().month
        current_year = datetime.now().year
        
        # Simulate varying availability throughout the year
        if current_month in [4, 8, 12]:  # Busy months
            status = "Limited Availability"
            availability_percentage = 25
        elif current_month in [1, 5, 9]:  # Moderately busy
            status = "Partial Availability"
            availability_percentage = 50
        else:  # Open months
            status = "Open to Opportunities"
            availability_percentage = 90
            
        # Project types I'm currently accepting
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
            
        # Calculate an approximate start date
        if availability_percentage > 75:
            start_date = "Immediately"
        elif availability_percentage > 40:
            start_date = f"In 2-3 weeks"
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
        """
        Recommend a starter project based on visitor's interest.
        
        Args:
            interest: The visitor's area of interest
            
        Returns:
            Dict with project recommendation details
        """
        interest = interest.lower()
        
        # Base recommendation structure
        recommendation = {
            "project_idea": "",
            "difficulty": "",
            "estimated_time": "",
            "resources": [],
            "starter_repo": "",
            "technologies": []
        }
        
        # AI agent recommendations
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

        # E-commerce / storefront recommendations
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

        # USSD / telco / Africa-specific recommendations
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

        # Default: agent governance / infrastructure
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
        """
        Return skills by category (language, cloud, database, etc).
        
        Args:
            category: The skill category to retrieve
            
        Returns:
            List of skills in the requested category
        """
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
        """
        Fetch real-time stats about GitHub repositories if requests is available.
        
        Returns:
            Dict with repository statistics or error message
        """
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
    
    def say_hi(self, visitor_name: Optional[str] = None) -> str:
        """
        Generate a personalized greeting with current availability.
        
        Args:
            visitor_name: Optional name of the visitor for personalization
            
        Returns:
            Formatted greeting string
        """
        current_time = datetime.now()
        
        # Determine time-appropriate greeting
        if current_time.hour < 12:
            time_greeting = "Good morning"
        elif current_time.hour < 18:
            time_greeting = "Good afternoon"
        else:
            time_greeting = "Good evening"
            
        if visitor_name:
            greeting = f"{time_greeting}, {visitor_name}. I'm Kenn — AI Builder in Nairobi."
        else:
            greeting = f"{time_greeting}. I'm Kenn — AI Builder in Nairobi, founder of SuperiaTech."

        random_project = random.choice(self.projects)
        live = f" · Live: {random_project['live']}" if random_project.get('live') else ""
        highlight = (
            f"Latest: {random_project['name']} — {random_project['description']}\n"
            f"  Stack: {', '.join(random_project['tech_stack'])}\n"
            f"  GitHub: {random_project['url']}{live}"
        )

        availability_info = (
            f"Status: {colored(self.availability['status'], 'green' if self.availability['percentage'] > 60 else 'yellow')}\n"
            f"Open to: {', '.join(self.availability['project_types'])}\n"
            f"Can start: {self.availability['start_date']}"
        )

        return f"{greeting}\n\n{highlight}\n\n{availability_info}"

    def to_json(self) -> str:
        """
        Return a JSON representation of this profile.
        
        Returns:
            JSON string of the profile
        """
        # Create a clean dict without methods for JSON serialization
        profile_dict = {k: v for k, v in self.__dict__.items() if not k.startswith('_') and not callable(v)}
        return json.dumps(profile_dict, indent=2)
    
    def generate_report(self) -> str:
        """
        Generate a formatted text report about this profile.
        
        Returns:
            Formatted text report
        """
        report = [
            f"{'=' * 50}",
            f"{self.name} — {self.role}".center(50),
            f"{self.location}".center(50),
            f"{'=' * 50}",
            f"",
            f"WHAT I DO:",
            f"  {self.mission}",
            f"",
            f"STACK:",
            f"  Languages:",
        ]

        for lang, details in self.languages.items():
            report.append(f"    - {lang}: {details['level']} · {', '.join(details['frameworks'])}")

        report.extend([
            f"",
            f"  Cloud & AI:",
        ])

        for skill in self.cloud_skills:
            report.append(f"    - {skill['name']}: {skill['level']}")

        report.extend([
            f"",
            f"SELECTED WORK:",
        ])

        for project in self.projects:
            live = f" · {project['live']}" if project.get('live') else ""
            report.append(f"  {project['name']} — {project['description']}")
            report.append(f"    Stack: {', '.join(project['tech_stack'])}")
            report.append(f"    {project['url']}{live}")
            report.append(f"")

        report.extend([
            f"AVAILABILITY:",
            f"  {self.availability['status']} — {', '.join(self.availability['project_types'])}",
            f"  Can start: {self.availability['start_date']}",
            f"",
            f"CONTACT:",
            f"  {self.github}",
            f"  superiorwech@gmail.com",
            f"",
            f"{'=' * 50}",
            f"Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            f"{'=' * 50}",
        ])
        
        return "\n".join(report)
    
    def save_profile(self, format_type: str = "json", filename: Optional[str] = None) -> str:
        """
        Save profile information to a file.
        
        Args:
            format_type: 'json' or 'text'
            filename: Optional custom filename
            
        Returns:
            Path to the saved file
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            if format_type.lower() == "json":
                filename = f"kenn_profile_{timestamp}.json"
            else:
                filename = f"kenn_profile_{timestamp}.txt"
                
        with open(filename, 'w') as f:
            if format_type.lower() == "json":
                f.write(self.to_json())
            else:
                f.write(self.generate_report())
                
        return os.path.abspath(filename)


def main():
    """Command line interface for the profile."""
    parser = argparse.ArgumentParser(description='Interactive developer profile for Kenn Macharia')
    parser.add_argument('--interest', type=str, help='Get project recommendations for your interest')
    parser.add_argument('--name', type=str, help='Your name for a personalized greeting')
    parser.add_argument('--stats', action='store_true', help='Show GitHub repository statistics')
    parser.add_argument('--save', choices=['json', 'text'], help='Save profile to file in specified format')
    parser.add_argument('--report', action='store_true', help='Generate a formatted text report')
    args = parser.parse_args()
    
    me = AIBuilder()
    
    # Print greeting
    print(me.say_hi(args.name))
    
    # Show project recommendation if interest is provided
    if args.interest:
        print(f"\n{colored('PROJECT RECOMMENDATION', 'cyan', attrs=['bold'])}")
        print(f"Based on your interest in {args.interest}:")
        recommendation = me.recommend_project(args.interest)
        
        print(f"  Project idea: {colored(recommendation['project_idea'], 'green')}")
        print(f"  Difficulty: {recommendation['difficulty']}")
        print(f"  Estimated time: {recommendation['estimated_time']}")
        print(f"  Technologies: {', '.join(recommendation['technologies'])}")
        print(f"  Starter repository: {recommendation['starter_repo']}")
        print(f"  Helpful resources:")
        for resource in recommendation['resources']:
            print(f"    - {resource}")
    
    # Show GitHub stats if requested
    if args.stats:
        print(f"\n{colored('GITHUB STATISTICS', 'cyan', attrs=['bold'])}")
        stats = me.get_repository_stats()
        
        if stats.get('status') == 'success':
            print(f"  Total repositories: {stats['total_repos']}")
            print(f"  Total stars: {stats['stars']}")
            print(f"  Total forks: {stats['forks']}")
            print(f"  Most popular repository: {stats['most_popular']}")
            print(f"  Languages used: {', '.join(stats['languages'])}")
            print(f"  Repositories (sorted by stars):")
            for repo in stats.get('repos_by_stars', []):
                print(f"    - {repo['name']}: {repo['stars']} stars, {repo['forks']} forks")
        else:
            print(f"  {stats.get('message', 'Could not retrieve GitHub statistics')}")
    
    # Generate report if requested
    if args.report:
        print(f"\n{me.generate_report()}")
    
    # Save profile if requested
    if args.save:
        filepath = me.save_profile(format_type=args.save)
        print(f"\nProfile saved to: {filepath}")
    
    # Show instructions if no specific action was requested
    if not any([args.interest, args.stats, args.report, args.save]):
        print("\nFor more information, try these commands:")
        print("  python github_profile.py --interest 'Cloud Architecture'")
        print("  python github_profile.py --name 'Your Name'")
        print("  python github_profile.py --stats")
        print("  python github_profile.py --report")
        print("  python github_profile.py --save json")


if __name__ == '__main__':
    main()
