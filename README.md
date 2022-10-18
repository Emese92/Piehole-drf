## Deployment
### Heroku
1. sign in or create account on heroku (https://id.heroku.com/login)
2. Create new app (add unique name and choose closest region)
3. Add resources (Heroku postgres)
4. Go to settings and Reveal Config Vars:
* CLOUDINARY_URL,
* DATABASE_URL,
* SECRET_KEY
* DISABLE_COLLECTSTATIC
5. In Deploy tab connect to Github and add your repository
6. Go to Manual Deployment choose main branch and press Deploy