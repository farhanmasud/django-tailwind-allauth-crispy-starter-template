# Django + Tailwind Starter Template

Getting started -

1. Clone repo 
2. Setup .env file following the example env file
3. Make all bash scripts executable with `find . -type f -iname "*.sh" -exec chmod +x {} \;`
4. Run `bash remove-git-remote.sh` script to remove git remote link
5. Add your own remote repo link
6. Setup database [requires step 2] with `bash setup-db.sh`
7. Setup venv and install dependencies with `bash setup-venv-pip-tools.sh`
8. Activate virtual environment with `source venv/bin/activate`
9. Install tailwind CSS dependencies `python manage.py tailwind init`
10. Uncomment "theme" app under installed apps on config/settings/base.py file
11. Install tailwind dependencies with `python manage.py tailwind install`
12. Uncomment "django_browser_reload" under installed apps and "django_browser_reload.middleware.BrowserReloadMiddleware" under middlewares on config/settings/base.py file
11. Run migrations with `python manage.py migrate`
12. Collect static `python manage.py migrate --no-input`