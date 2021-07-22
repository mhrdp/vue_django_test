# Welcome
This is a test site I try to build utilizing Django for backend and VueJS for frontend, mainly to try to learn about Vue. Initially I want to use Django Template together with Vue's SPA, but ultimately decided to separate the two. Django, combined with Django REST Framework responsible for entire backend process while VueJS handle all things frontend and communicating to backend through API.

## Notes
This setup combine <code>frontend</code> and <code>backend</code> in one root folder, you would probably want to have separate root for <code>frontend</code> and <code>backend</code>. This not optimized for production. This site use token authentication from <code>restframework_simplejwt</code>.

## Tools
### Primary
The tools that act as a core of the site and responsible for operating the main system.
- Django 3.1
- Django REST Framework (Web API)
- Restframework_simplejwt (DRF's token authentication)
- VueJS 3.x (together with router, axios, components, store)
- Bootstrap 5.2

### Secondary
Complimentary tools to complete the site's features.
- Bootstrap Icons
- Bulma Toast

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
