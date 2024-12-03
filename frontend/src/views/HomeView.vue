<script setup>
  import NoteList from "@/components/NoteList.vue";
</script>

<template>
  <div class="home-container">
    <!-- Header Section -->
    <header class="home-header">
      <h1>Welcome to FarmNote</h1>
      <p>Your farming journal, simplified</p>
    </header>

    <!-- Main Content Section -->
    <div class="main-content">
      <div class="note-summary">
        <h2>Your Latest Notes</h2>
        <div class="notes-list">
          <div v-if="notes.length === 0" class="no-notes">
            <p>No notes available. Start adding your farm details!</p>
          </div>
          <div v-for="note in notes" :key="note.id" class="note-item">
            <h3>{{ note.content }}</h3>
            <p><strong>Date:</strong> {{ formatDate(note.creationDate) }}</p>
            <p><strong>Location:</strong> Latitude: {{ note.latitude }}, Longitude: {{ note.longitude }}</p>
            <p><strong>Temperature:</strong> {{ note.temperature }}°C</p>
            <button @click="viewNote(note.id)">View Note</button>
          </div>
        </div>
      </div>

      <div class="add-note">
        <h2>Add a New Note</h2>
        <button @click="navigateToAddNote">Create Note</button>
      </div>
    </div>

    <!-- Footer Section -->
    <footer class="home-footer">
      <p>&copy; 2024 FarmNote. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      notes: [
        {
          id: 1,
          content: 'Planted corn seeds',
          latitude: 48.1271,
          longitude: 15.1247,
          temperature: 18.3,
          creationDate: '2024-12-03T12:00:00.000Z'
        },
        {
          id: 2,
          content: 'Checked irrigation system',
          latitude: 48.1300,
          longitude: 15.1300,
          temperature: 20.1,
          creationDate: '2024-12-02T10:30:00.000Z'
        }
      ]
    };
  },
  methods: {
    formatDate(dateString) {
      const date = new Date(dateString);
      return date.toLocaleDateString('en-US', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      });
    },
    navigateToAddNote() {
      this.$router.push('/add-note');
    },
    viewNote(noteId) {
      this.$router.push(`/note/${noteId}`);
    }
  }
};
</script>

<style scoped>
/* Base Styles */
.home-container {
  font-family: Arial, sans-serif;
  padding: 20px;
  background-color: #f5f5f5;
  max-width: 100%;
  margin: 0 auto;
}

.home-header {
  text-align: center;
  margin-bottom: 20px;
}

.home-header h1 {
  font-size: 2rem;
  color: #2d6a4f;
}

.home-header p {
  font-size: 1rem;
  color: #3e8e41;
}

.main-content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.note-summary {
  width: 100%;
  max-width: 100%;
  margin-bottom: 20px;
}

.notes-list {
  margin-top: 10px;
}

.note-item {
  background-color: #ffffff;
  padding: 12px;
  margin-bottom: 12px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  font-size: 0.9rem;
}

.note-item h3 {
  font-size: 1.2rem;
  margin: 0;
}

.note-item p {
  margin: 5px 0;
  font-size: 0.9rem;
}

.no-notes {
  color: #666;
  font-size: 1rem;
  text-align: center;
}

.add-note {
  width: 100%;
  max-width: 320px;
  text-align: center;
  margin-top: 20px;
}

.add-note button {
  padding: 12px 20px;
  font-size: 1rem;
  background-color: #2d6a4f;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 100%;
}

.add-note button:hover {
  background-color: #3e8e41;
}

.home-footer {
  text-align: center;
  margin-top: 30px;
  color: #555;
  font-size: 0.9rem;
}

/* Media Queries for Mobile First */

@media (min-width: 600px) {
  /* Adjust the font size for larger screens */
  .home-header h1 {
    font-size: 2.5rem;
  }

  .home-header p {
    font-size: 1.2rem;
  }

  .note-item {
    font-size: 1rem;
  }

  .note-item h3 {
    font-size: 1.4rem;
  }

  .add-note button {
    font-size: 1.2rem;
  }
}

@media (min-width: 768px) {
  /* Larger tablets and desktop screens */
  .home-container {
    max-width: 960px;
    padding: 40px;
  }

  .note-summary {
    width: 80%;
  }

  .notes-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }

  .note-item {
    width: 48%;
    margin-bottom: 20px;
  }

  .add-note {
    width: 100%;
    max-width: 350px;
  }
}

@media (min-width: 1024px) {
  /* Desktops and larger screens */
  .note-summary {
    width: 70%;
  }

  .note-item {
    width: 45%;
  }
}
</style>

