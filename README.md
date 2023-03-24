# Django + Tailwind + Allauth + Crispy Forms Starter Template

> :hourglass_flowing_sand: Under development

Getting started -

1. Clone repo with your project name `git clone git@github.com:farhanmasud/django-tailwind-starter-template.git your-project-name`
2. Setup .env file following the example env file
3. Make all bash scripts executable with `find . -type f -iname "*.sh" -exec chmod +x {} \;`
4. Run `bash update-git-remote.sh` script to remove existing git remote link (of this repo) and update with your on git repo link. Copy your remote URL from GitHub and run the bash script, it'll propmt to enter the new link, paste and hit Enter.
5. Setup database [requires step 2] with `bash setup-db.sh`
6. Setup venv and install dependencies with `bash setup-venv-pip-tools.sh`
7. Activate virtual environment with `source venv/bin/activate`
8. Install tailwind dependencies with `python manage.py tailwind install`
9. Run migrations with `python manage.py migrate`
10. Collect static `python manage.py collectstatic --no-input`
