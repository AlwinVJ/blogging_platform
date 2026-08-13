Django Blog Application — Project & Git Workflow

A practical Django blog application built by following the tutorial Python Django Basics To Advanced | Complete Blog Application by Rathan Kumar.

This repository is being implemented as a learning project, with an additional focus on using Git and GitHub properly throughout the development process.

Tutorial Reference

Tutorial: Python Django Basics To Advanced | Complete Blog Application
Instructor: Rathan Kumar
Platform: Udemy
Course page: https://www.udemy.com/course/python-django-for-beginners-build-3-practical-projects/

The tutorial covers Django fundamentals and progressively builds a real-world blog application with authentication, authorization, CRUD operations, search, custom dashboards, comments, and deployment.

YouTube courtesy: The exact YouTube URL for the tutorial used as the source of this project was not present in the supplied transcript, and I have not added an unverified URL. If the tutorial has a corresponding YouTube video, add its verified URL here:

YouTube: PASTE VERIFIED YOUTUBE URL HERE

Project Goals

This project has two learning objectives:

Build a complete Django blog application from scratch.

Practice a professional Git/GitHub workflow while developing the application.

The Git workflow is intentionally more structured than simply committing directly to main.

Technology Stack

Python

Django

SQLite during development

HTML

CSS

Bootstrap

JavaScript

Git

GitHub

Main Features

The tutorial progressively implements:

Django project setup

Homepage and templates

Static files

Media files

Category model

Blog model

Slug generation

Django Admin customization

Featured and recent posts

Posts by category

Custom 404 page

Template inheritance

Context processors

Single blog pages

About page

Social links

Search functionality

User registration

Login and logout

Authentication and authorization

Groups and permissions

Editor and manager dashboards

Category CRUD

Blog post CRUD

User management

Comments

Deployment

Git & GitHub Workflow

Branching Strategy

main is treated as the stable branch.

Major features are developed in dedicated feature branches.

main
│
├── feature/blog-foundation
├── feature/blog-display
├── feature/category-pages
├── feature/single-blog
├── feature/about-social-links
├── feature/search
├── feature/authentication
├── feature/authorization
├── feature/dashboard
├── feature/category-crud
├── feature/blog-management
├── feature/user-management
├── feature/comments
└── feature/deployment

We do not create a new branch for every tutorial video. A branch represents a coherent feature or subsystem.

Commit Convention

Commits use a Conventional Commits-style format.

Examples:

feat: add category model
feat: configure media files
feat: add blog model
feat: implement blog search
feat: add user registration
fix: handle missing category
refactor: implement template inheritance
chore: upgrade project dependencies
docs: update deployment instructions

Commit Rule

A commit should represent a meaningful, working state.

Avoid commits such as:

did some stuff
changes
update
final
test

Prefer:

feat: add category model

Git Development Roadmap

Tutorial Area

Branch

Example Commits

Project setup & homepage

main

chore: initialize Django blog project

Blog foundation

feature/blog-foundation

category, media, blog model, slug, admin

Homepage blog content

feature/blog-display

categories, featured posts, recent posts

Category pages

feature/category-pages

category page, 404, templates, URLs

Single blog

feature/single-blog

single blog page

About & social links

feature/about-social-links

about page, social links

Search

feature/search

search functionality and layout

Authentication

feature/authentication

registration, login, logout

Authorization

feature/authorization

groups and permissions

Dashboard

feature/dashboard

dashboards, sidebar, statistics

Category CRUD

feature/category-crud

create, edit, delete category

Blog management

feature/blog-management

create, edit, delete posts

User management

feature/user-management

add, edit, delete users

Comments

feature/comments

comment model and functionality

Deployment

feature/deployment

production configuration and deployment

Standard Workflow

Before starting a new feature:

git switch main
git pull origin main
git switch -c feature/<feature-name>

After completing a meaningful unit:

git status
git add .
git commit -m "feat: describe the change"

Push the feature branch:

git push -u origin feature/<feature-name>

When the feature is complete and tested:

git switch main
git pull origin main
git merge --no-ff feature/<feature-name>
git push origin main

The feature branch can then be removed:

git branch -d feature/<feature-name>
git push origin --delete feature/<feature-name>

Initial Git Setup

The project should have a .gitignore before the first GitHub push.

Important files/folders to keep out of the repository include:

.venv/
venv/
env/

__pycache__/
*.py[cod]

db.sqlite3

media/

.env

Do not ignore Django migration files.

Migrations are part of the application's source code and should normally be committed:

blogs/migrations/

Useful Git Commands

Check current state:

git status

View branches:

git branch

View all branches:

git branch -a

View commit history:

git log --oneline --graph --decorate --all

View unstaged changes:

git diff

View staged changes:

git diff --cached

Check the remote:

git remote -v

Synchronize with GitHub:

git pull origin main

Development Checkpoint Philosophy

The tutorial contains periodic Git Push sections. This project uses those sections as natural milestone boundaries, but commits are made more frequently.

For example:

Create Category Model
        ↓
Test migrations
        ↓
COMMIT
        ↓
Configure Media
        ↓
Test media upload
        ↓
COMMIT
        ↓
Create Blog Model
        ↓
Test admin
        ↓
COMMIT
        ↓
Feature complete
        ↓
PUSH FEATURE BRANCH
        ↓
MERGE INTO MAIN

This gives the repository a useful development history instead of one large commit per tutorial section.

Project Status

Progress will be tracked here as the tutorial is implemented.

Project initialization

Homepage

Static files

Git/GitHub setup

Category model

Media configuration

Blog model

Slug generation

Admin customization

Homepage blog content

Category pages

Single blog page

About page

Social links

Search

Registration

Login/logout

Authorization

Groups and permissions

Dashboard

Category CRUD

Blog CRUD

User management

Comments

Deployment

Learning Notes

This project is not intended to be only a copy of the tutorial.

For each major feature, the goal is to understand:

Why the Django feature is needed.

How the model/view/template flow works.

How database relationships are represented.

How URLs map to views.

How authentication and authorization differ.

How Django ORM queries retrieve related data.

How Git commits represent development milestones.

Why a feature belongs on a separate branch.

How branches are merged into main.

Source

The project structure and feature roadmap are based on the supplied tutorial transcript.

The tutorial's course listing identifies the instructor as Rathan Kumar and describes the project as a real-world Django blog application with CRUD, authentication, authorization, dynamic pages, custom dashboards, search, and template functionality.

Official course reference:

https://www.udemy.com/course/python-django-for-beginners-build-3-practical-projects/