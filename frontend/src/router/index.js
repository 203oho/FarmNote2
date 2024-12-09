import {createRouter, createWebHistory} from 'vue-router'
import HomeView from "@/views/HomeView.vue";
import StartView from "@/views/StartView.vue"
import CreateNoteView from "@/views/CreateNoteView.vue";
import EditNoteView from "@/views/EditNoteView.vue";
import JoinView from "@/views/JoinView.vue";
import ShareView from "@/views/ShareView.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'start',
            component: StartView
        },
        {
            path: '/home',
            name: 'home',
            component: HomeView
        },
        {
            path: '/join/:token',
            name: 'join-home',
            component: HomeView
        },
        {
            path: '/createNote',
            name: 'Create Note',
            component: CreateNoteView
        },
        {
            path: '/note/:id',
            name: 'Edit Note',
            component: EditNoteView
        },
        {
            path: '/share',
            name: 'share',
            component: ShareView
        },
    ]
})

export default router
