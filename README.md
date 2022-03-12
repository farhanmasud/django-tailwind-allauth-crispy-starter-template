# Django + Tailwind + Allauth Starter Template

> :hourglass_flowing_sand: Under development

Getting started -

1. Clone repo with your project name `git clone git@github.com:farhanmasud/django-tailwind-starter-template.git your-project-name`
2. Setup .env file following the example env file
3. Make all bash scripts executable with `find . -type f -iname "*.sh" -exec chmod +x {} \;`
4. Run `bash remove-git-remote.sh` script to remove git remote link
5. Add your own remote repo link with `git remote add origin git@github.com:your-username/your-repo.git`
6. Setup database [requires step 2] with `bash setup-db.sh`
7. Setup venv and install dependencies with `bash setup-venv-pip-tools.sh`
8. Activate virtual environment with `source venv/bin/activate`
9. Install tailwind dependencies with `python manage.py tailwind install`
10. Run migrations with `python manage.py migrate`
11. Collect static `python manage.py collectstatic --no-input`