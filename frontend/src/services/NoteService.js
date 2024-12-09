import {NotesApi} from "http-client";
import SessionService from "@/services/SessionService.js";
import {ref} from "vue";




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
                        }
                    }
                }
            );
        });
    }


    async getNote(id) {
        return SessionService.getToken().then((token) => {
            console.log("Request with token: " + token)
            return this.notesApi.readNote({
                token: token,
                noteId: id
            });
        });
    }

    async deleteNote(id) {
        return SessionService.getToken().then((token) => {
            console.log("Request with token: " + token)
            return this.notesApi.deleteNote({
                token: token,
                noteId: id
            });
        });
    }

    async updateNote(id, noteData, updatetemperature) {
        return SessionService.getToken().then((token) => {
            console.log(token)
            console.log(id)
            console.log(updatetemperature)
            const requestParameters = {
                token: token,
                noteId: id,
                noteUpdate: noteData // noteData should be of type NoteUpdate
            };
            return this.notesApi.updateNote(
                requestParameters,
                request => {
                    return {
                        ...request.init,
                        body: {
                            ...request.init.body,
                            temperature: updatetemperature.value
                        }
                    }
                }
            )
                .then(note => {
                    return note;
                });
        });
    }
}

export default new NoteService();