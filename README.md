# no_idea_AI
Alex, Luke, Haydon and Nathans AI

- Specification
--   Purpose: The purpose of this service to have users create an account, log in and generate phrases and save the seed (original phrase)
--   Needed: Custom Model, Log in system, AI external API

- Plan B: If no accepable AI API service is reasonable than we will move toward using a random text generator service.


# How to setup on local repo
- Create .venv
`>>>python -m venv .venv`
- Activate venv
`>>>.venv\scripts\activate`
- Install requirements
`>>>pip install -r requirements.txt`
- Migrate changes
`>>>python manage.py migrate`

Should be good to run. I'm also sharing .env to make things easier.

# Ajax config
- jQuery is called at the head level of base.html
- Within article_detail, we are checking for csrf safety with jQuery ajax with the 3 functions above 'aibutton' click handler
- Todo 
  - Error handling for ajax calls that are empty, to long, etc.
  - AI Button needs better styling (not attribute level)
  - CRUD logic hooked up to ajax functionality
