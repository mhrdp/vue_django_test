import { createRouter, createWebHistory } from "vue-router";
import Login from "../views/Home.vue";
import Dashboard from "../views/Dashboard.vue";
import Register from "../views/Register.vue";

const routes = [
  {
    path: "/login",
    name: "Login",
    component: Login,
	meta: {
		asGuest: true,
	}
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
	meta: {
		requireLogin: true,
	}
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
	meta: {
		asGuest: true,
	}
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Before each is a function that will executed before going to each routes
// Do it like this to apply it globally, or wrote inside each route to apply it locally
router.beforeEach((to, from, next) => {
	if(to.matched.some(record => record.meta.requireLogin)){
		if(localStorage.getItem('token') == null){
			next({
				name: 'Login',
				query: {
					to: to.path
				}
			})	
		} else {
			next()
		}
	} else if(to.matched.some(record => record.meta.asGuest)){
		if(localStorage.getItem('token') == null){
			next()
		} else {
			next({
				name: 'Dashboard',
			})
		}
	} else {
		next()
	}
})

export default router;
