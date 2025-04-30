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


class SoftwareEngineer:
    """
    Interactive profile class that showcases skills and generates project recommendations
    based on visitor's interests. Can be run locally after cloning.
    """
    def __init__(self):
        """Initialize with personal and professional information."""
        self.name = "Kenn Macharia"
        self.role = "Back-End Developer"
        self.location = "Nairobi, Kenya"
        self.mission = "Creating robust software architecture that scales"
        self.github_username = "SuperiorKe"
        self.languages = {
            "Python": {
                "level": "Expert", 
                "years": 5, 
                "frameworks": ["FastAPI", "Django", "Flask"],
                "strengths": ["API Development", "Data Processing", "Automation"]
            },
            "JavaScript": {
                "level": "Advanced", 
                "years": 4, 
                "frameworks": ["Node.js", "Express"],
                "strengths": ["Server-side Applications", "RESTful APIs"]
            },
            "TypeScript": {
                "level": "Advanced", 
                "years": 3, 
                "frameworks": ["NestJS"],
                "strengths": ["Type-safe Backend Development", "Enterprise Applications"]
            },
            "Go": {
                "level": "Intermediate", 
                "years": 2, 
                "frameworks": ["Gin"],
                "strengths": ["High-performance Services", "Concurrent Applications"]
            }
        }
        self.cloud_skills = [
            {"name": "AWS", "level": "Certified", "services": ["Lambda", "ECS", "S3", "DynamoDB"]},
            {"name": "Kubernetes", "level": "Advanced", "focus": "Production Deployments"},
            {"name": "Terraform", "level": "Intermediate", "focus": "Infrastructure as Code"},
            {"name": "CI/CD", "level": "Advanced", "tools": ["GitHub Actions", "GitLab CI", "Jenkins"]}
        ]
        self.interests = ["Cloud Architecture", "DevOps", "AI/ML", "Open Source"]
        self.github = f"https://github.com/{self.github_username}"
        self.availability = self._check_availability()
        
        # Projects information with tech stacks and descriptions
        self.projects = [
            {
                "name": "Carbon Footprint Calculator",
                "url": f"{self.github}/Carbon_Footprint_Calculator",
                "tech_stack": ["Go", "Kubernetes", "AWS", "PostgreSQL"],
                "category": "Sustainability",
                "description": "Microservices platform for measuring carbon emissions",
                "key_features": [
                    "Service mesh architecture",
                    "Real-time data processing",
                    "Scalable analytics dashboard"
                ]
            },
            {
                "name": "AI Chatbot",
                "url": f"{self.github}/django_chatbot",
                "tech_stack": ["Python", "Django", "TensorFlow", "React"],
                "category": "AI/ML",
                "description": "Intelligent conversational AI with context awareness",
                "key_features": [
                    "Natural language processing",
                    "Contextual memory",
                    "Multi-channel integration"
                ]
            }
        ]
        
        # Repositories for starter projects
        self.starter_repos = {
            "serverless": f"{self.github}/serverless-starter",
            "ai_ml": f"{self.github}/sentiment-analysis-api",
            "devops": f"{self.github}/cicd-starter",
            "api": f"{self.github}/fastapi-starter"
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
            project_types = ["Backend Development", "Cloud Architecture", "Technical Consulting"]
        else:
            project_types = [
                "Backend Development", 
                "Cloud Architecture", 
                "Technical Consulting",
                "Open Source Collaboration",
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
        
        # Cloud/AWS recommendations
        if any(keyword in interest for keyword in ["cloud", "aws", "infrastructure", "serverless"]):
            recommendation.update({
                "project_idea": "Serverless API with AWS Lambda",
                "difficulty": "Intermediate",
                "estimated_time": "1-2 weeks",
                "resources": [
                    "AWS Lambda documentation", 
                    "Serverless Framework docs", 
                    "AWS API Gateway tutorials"
                ],
                "starter_repo": self.starter_repos["serverless"],
                "technologies": ["AWS Lambda", "API Gateway", "DynamoDB", "Serverless Framework"]
            })
            
        # AI/ML recommendations
        elif any(keyword in interest for keyword in ["ai", "ml", "machine learning", "artificial intelligence", "nlp"]):
            recommendation.update({
                "project_idea": "Sentiment Analysis API",
                "difficulty": "Intermediate",
                "estimated_time": "2-3 weeks",
                "resources": [
                    "TensorFlow tutorials", 
                    "NLTK documentation", 
                    "FastAPI documentation"
                ],
                "starter_repo": self.starter_repos["ai_ml"],
                "technologies": ["Python", "TensorFlow/PyTorch", "NLTK", "FastAPI"]
            })
            
        # DevOps recommendations
        elif any(keyword in interest for keyword in ["devops", "ci/cd", "pipeline", "automation"]):
            recommendation.update({
                "project_idea": "CI/CD Pipeline with GitHub Actions",
                "difficulty": "Intermediate",
                "estimated_time": "1-2 weeks",
                "resources": [
                    "GitHub Actions documentation", 
                    "Docker tutorials", 
                    "Testing automation guides"
                ],
                "starter_repo": self.starter_repos["devops"],
                "technologies": ["GitHub Actions", "Docker", "Testing frameworks", "Infrastructure as Code"]
            })
            
        # Default API recommendation
        else:
            recommendation.update({
                "project_idea": "RESTful API with FastAPI",
                "difficulty": "Beginner to Intermediate",
                "estimated_time": "1 week",
                "resources": [
                    "FastAPI documentation", 
                    "PostgreSQL tutorials", 
                    "API design best practices"
                ],
                "starter_repo": self.starter_repos["api"],
                "technologies": ["Python", "FastAPI", "PostgreSQL", "SQLAlchemy", "Pydantic"]
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
                return {
                    "status": "success",
                    "total_repos": len(repos),
                    "stars": sum(repo["stargazers_count"] for repo in repos),
                    "forks": sum(repo["forks_count"] for repo in repos),
                    "most_popular": max(repos, key=lambda x: x["stargazers_count"])["name"],
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
            greeting = f"{time_greeting}, {visitor_name}! Thanks for checking out my profile."
        else:
            greeting = f"{time_greeting}! Thanks for dropping by my profile."
            
        # Add a random tip or project highlight
        random_interest = random.choice(self.interests)
        random_project = random.choice(self.projects)
        
        if random.choice([True, False]):
            # Highlight a technical interest
            highlight = f"I'm currently exploring {random_interest}. Have any interesting projects in that area?"
        else:
            # Highlight a project
            highlight = f"Check out my {random_project['name']} project if you're interested in {random_project['category']}!"
            
        # Format availability information
        availability_info = (
            f"Current Status: {colored(self.availability['status'], 'green' if self.availability['percentage'] > 60 else 'yellow')}\n"
            f"Available for: {', '.join(self.availability['project_types'])}\n"
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
            f"{self.name} - {self.role}".center(50),
            f"{'=' * 50}",
            f"",
            f"MISSION:",
            f"  {self.mission}",
            f"",
            f"TECHNICAL SKILLS:",
            f"  Languages:"
        ]
        
        # Add language details
        for lang, details in self.languages.items():
            report.append(f"    - {lang}: {details['level']} ({details['years']} years)")
            report.append(f"      Frameworks: {', '.join(details['frameworks'])}")
            
        report.extend([
            f"",
            f"  Cloud & DevOps:"
        ])
        
        # Add cloud skills
        for skill in self.cloud_skills:
            report.append(f"    - {skill['name']}: {skill['level']}")
            
        report.extend([
            f"",
            f"PROJECTS:"
        ])
        
        # Add project details
        for project in self.projects:
            report.append(f"  - {project['name']}: {project['description']}")
            report.append(f"    Tech: {', '.join(project['tech_stack'])}")
            
        report.extend([
            f"",
            f"CURRENT AVAILABILITY:",
            f"  Status: {self.availability['status']}",
            f"  Available for: {', '.join(self.availability['project_types'])}",
            f"  Can start: {self.availability['start_date']}",
            f"",
            f"CONTACT:",
            f"  GitHub: {self.github}",
            f"",
            f"{'=' * 50}",
            f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"{'=' * 50}"
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
    
    me = SoftwareEngineer()
    
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
