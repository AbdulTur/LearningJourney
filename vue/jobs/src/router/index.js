import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '@/views/AboutView.vue'
import Jobs from '@/views/Jobs/Jobs.vue'
import JobDetails from '@/views/Jobs/JobDetails.vue'
import NotFound from '@/views/NotFound.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/Jobs',
    name: 'Jobs',
    component: Jobs
  },
  {
    path: '/Jobs/:id',
    name: 'JobDetails',
    component: JobDetails,
    props: true
  },
  {
    path: '/all-jobs',
    redirect:'/Jobs',
  },
  {
    path: '/:catchAll(.*)',
    name:'NotFound',
    component: NotFound
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
