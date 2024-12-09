<script>
import Note from "@/components/Note.vue";
import NoteService from "@/services/NoteService.js";
import SessionService from "@/services/SessionService.js";

export default {
  components: {Note},
  data() {
    return {
      notes: [],
      showError: false
    }
  },
  mounted() {
    NoteService.getAllNotes().then(notes => this.notes = [...notes]).catch(e => {
      if (e.response.status === 401) {
        this.$toast.open({message: "Invalid Token!", duration: 10000, type: "error"})
      } else {
        alert(`backend is offline or GET endpoint /notes/ does not exist (${e.response.statusText})`)
      }
    });
  },
  methods: {
    goToNote(id) {
      this.$router.push('/Note/' + id);
    }
  }

}
</script>

<template>
  <div class="notes-container">
    <!-- This block is for adjusting the notes so they dont begin behind the create button -->
    <label style="width: 100%; height: 60px"></label>

    <Note class="note" v-for="note in notes" :key="note" :note="note" @click="goToNote(note.id)"></Note>
  </div>
</template>

<style>
.notes-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
  background: #d8dce1;
}

.note {
  width: 85%;
  max-width: 800px;
  cursor: pointer;
}
</style>