import {NotesApi} from "http-client";
import SessionService from "@/services/SessionService.js";



class NoteService {
    notesApi = new NotesApi();

    async getAllNotes() {
        return SessionService.getToken().then((token) => {
            console.log("Request with token: " + token)
            return this.notesApi.readNotes({
                token: token
            }).then(notes => {
                return notes;
            });
        });
    }

    async createNote(note) {
        return SessionService.getToken().then((token) => {
            console.log("Request with token: " + token)
            return this.notesApi.createNote({
                token: token,
                noteCreate: note
            }, request => {
                return {
                    ...request.init,
                    body: {
                        ...request.init.body,
                        temperature: note.temperature
                    }}}

                    );
        });
    }


    async getNote(id){
        return SessionService.getToken().then((token) => {
            console.log("Request with token: " + token)
            return this.notesApi.readNote({
                token: token,
                noteId: id
            });
        });
    }

    async deleteNote(id){
        return SessionService.getToken().then((token) => {
            console.log("Request with token: " + token)
            return this.notesApi.deleteNote({
                token: token,
                noteId: id
            });
        });
    }

     async updateNote(id, newNote){
        return SessionService.getToken().then((token) => {
            console.log("Request with token: " + token)
            return this.notesApi.updateNote({
                token: token,
                noteId: id,
                 noteUpdate: newNote
            });
        });
    }

}

export default new NoteService();