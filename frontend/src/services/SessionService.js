
import {NotesApi} from "../../http-client";

class SessionService {
    sessionApi = new SessionApi();

    async getToken() {
        if (sessionStorage.getItem('token') === null || "") {
            const session = await this.sessionApi.createSession();
            sessionStorage.setItem('token', session.token)
            return sessionStorage.getItem('token');
        } else {
            return sessionStorage.getItem('token');
        }
    }

    async joinSession(token) {
        const notes = await this.sessionApi.joinSession({token:token});
        return notes != null
    }

    getQRCodeUrl() {
        return import.meta.env.VITE_API_URL; // API-Basis-URL
    }
}

export default new SessionService();