// src/services/NoteService.js
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/notes/';

export default {
  async getNotes() {
    try {
      const response = await axios.get(API_URL);
      return response.data;
    } catch (error) {
      console.error('Error fetching notes:', error);
      return [];
    }
  },

  async createNote(noteData) {
    try {
      const response = await axios.post(API_URL, noteData);
      return response.data;
    } catch (error) {
      console.error('Error creating note:', error);
      return null;
    }
  },

  async updateNote(noteId, updatedNoteData) {
    try {
      const response = await axios.put(`${API_URL}${noteId}`, updatedNoteData);
      return response.data;
    } catch (error) {
      console.error('Error updating note:', error);
      return null;
    }
  },

  async deleteNote(noteId) {
    try {
      await axios.delete(`${API_URL}${noteId}`);
    } catch (error) {
      console.error('Error deleting note:', error);
    }
  },
};
