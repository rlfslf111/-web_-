import Vue from 'vue'
import VueRouter from 'vue-router'

import LoginView from '../views/accounts/LoginView.vue'
import SignupView from '../views/accounts/SignupView.vue'

import ArticleListView from '../views/articles/ArticleListView.vue'
import ArticleCreateView from '../views/articles/ArticleCreateView.vue'
import ArticleDetailView from '../views/articles/ArticleDetailView.vue'
import ArticleUpdateView from '../views/articles/ArticleUpdateView.vue'

import MovieListView from '../views/movies/MovieListView.vue'
Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'MovieListView',
    component: MovieListView
  },
  {
    path: '/articles',
    name: 'ArticleListView',
    component: ArticleListView
  },
  {
    path: '/articles/create',
    name: 'ArticleCreateView',
    component: ArticleCreateView
  },
  {
    path: '/accounts/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/accounts/signup',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/articles/:id',
    name: 'ArticleDetailView',
    component: ArticleDetailView
  },
  {
    path: '/articles/:id/update',
    name: 'ArticleUpdateView',
    component: ArticleUpdateView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
