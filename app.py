#!/usr/bin/env python3
"""
Jenkins Freestyle Job Build Script
This script demonstrates Jenkins built-in environment variables with colored output
No external dependencies required - uses only Python standard library
"""

import os
import sys

# ANSI Color codes for terminal output
class Colors:
    HEADER = '\033[95m'      # Magenta
    BLUE = '\033[94m'        # Blue
    CYAN = '\033[96m'        # Cyan
    GREEN = '\033[92m'       # Green
    YELLOW = '\033[93m'      # Yellow
    RED = '\033[91m'         # Red
    ENDC = '\033[0m'         # End color
    BOLD = '\033[1m'         # Bold
    UNDERLINE = '\033[4m'    # Underline

def print_header(text):
    """Print a formatted header"""
    print(f"{Colors.BOLD}{Colors.HEADER}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}{text.center(60)}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}{'='*60}{Colors.ENDC}\n")

def print_section(title):
    """Print a section title"""
    print(f"{Colors.BOLD}{Colors.CYAN}>>> {title}{Colors.ENDC}")

def print_variable(name, value):
    """Print a variable with colors"""
    print(f"{Colors.BLUE}{name}:{Colors.ENDC} {Colors.GREEN}{value}{Colors.ENDC}")

def print_info(text):
    """Print informational text"""
    print(f"{Colors.YELLOW}{text}{Colors.ENDC}")

def print_success(text):
    """Print success message"""
    print(f"{Colors.GREEN}{Colors.BOLD}✓ {text}{Colors.ENDC}")

def main():
    # Main welcome header
    print_header("Hi, Welcome to Jenkins!")
    
    # Get Jenkins built-in environment variables
    print_section("Jenkins Build Information")
    
    job_name = os.getenv('JOB_NAME', 'Not Set')
    build_number = os.getenv('BUILD_NUMBER', 'Not Set')
    build_id = os.getenv('BUILD_ID', 'Not Set')
    workspace = os.getenv('WORKSPACE', 'Not Set')
    jenkins_url = os.getenv('JENKINS_URL', 'Not Set')
    build_url = os.getenv('BUILD_URL', 'Not Set')
    
    print_variable("Job Name", job_name)
    print_variable("Build Number", build_number)
    print_variable("Build ID", build_id)
    print_variable("Workspace", workspace)
    print_variable("Jenkins URL", jenkins_url)
    print_variable("Build URL", build_url)
    
    print()
    
    # Additional useful variables
    print_section("Build Configuration")
    
    build_user = os.getenv('BUILD_USER', 'Not Set')
    git_commit = os.getenv('GIT_COMMIT', 'Not Set')
    git_branch = os.getenv('GIT_BRANCH', 'Not Set')
    node_name = os.getenv('NODE_NAME', 'Not Set')
    
    print_variable("Build User", build_user)
    print_variable("Git Commit", git_commit)
    print_variable("Git Branch", git_branch)
    print_variable("Node Name", node_name)
    
    print()
    
    # Build status information
    print_section("Build Execution Details")
    
    build_timestamp = os.getenv('BUILD_TIMESTAMP', 'Not Set')
    executor_number = os.getenv('EXECUTOR_NUMBER', 'Not Set')
    
    print_variable("Build Timestamp", build_timestamp)
    print_variable("Executor Number", executor_number)
    
    print()
    
    # Success message
    print_success("Build script executed successfully!")
    print_info(f"Build Date: {os.getenv('BUILD_DISPLAY_NAME', 'Unknown')}")
    
    print()
    print(f"{Colors.BOLD}{Colors.GREEN}Jenkins Freestyle Job Execution Complete!{Colors.ENDC}\n")

if __name__ == "__main__":
    main()
