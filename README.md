# django_vue_5

## Notes
This setup combine `frontend` and `backend` in one root folder, you would probably want to have separate root for `frontend` and `backend`. One way to do this by nesting Vue's folder inside django root folder.

**Known Problems For This Kind of Setup:**
**Disclaimer:** There's probably a fix for this, I just haven't searched for it.
1. When you refreshed the page, the Vue page that was run on `localhost:8000` after `npm run build` was executed, and was controlled by Vue's router, will automatically replaced by Django's default router which will resulting in **404 Page not found** error. To go back to Vue's routing, you need to go back to its `home` page and start over there again.

## MIME Problem
If you got an error that states something about `MIME` type mismatch for your static files (`.js`, `.css`)after executing `npm run build` and run the compiled scripts inside Django's `localhost:8000`, odds are there's a conflict on how Django wants you to store your static files and how Vue store its static files by default.

One way to solve this was by look at `STATIC_URL` config inside `core/settings.py`, and match the Vue's directory placement accordingly. For example, `STATIC_URL = '/static/'` mean that you should put your Vue's static files (by default inside of `dist` folder) inside `static` folder (make a new one if no such folder), so that the routing matches with what Django wanted it to be.

Another possibility was that it related to CORS. Just download `django-cors-headers` via `pip install django-cors-headers`, follow the installation instruction [here](https://github.com/adamchainz/django-cors-headers#setup) and set `CORS_ALLOWED_ORIGINS = ['yourhostname']` or `CORS_ALLOW_ALL_ORIGINS` to `True` (not really recommended).

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
