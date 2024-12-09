<script>
import ShareButton from "@/components/ShareButton.vue";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import noteService from "@/services/NoteService.js";
import NoteService from "@/services/NoteService.js";
import Map from "@/components/Map.vue";
import {ref} from "vue";
const updatetemperature= ref(0);

export default {
  components: {FontAwesomeIcon, ShareButton, Map},
  data() {
    return {
      note: {},

    };
  },

  mounted() {
    noteService.getNote(this.$route.params.id).then((note) => {
      this.note = note
    })
  },
  methods: {
    saveNote() {
      console.log(this.note)
      NoteService.updateNote(this.note.id, this.note, this.temperature).then(() => {
        this.$toast.open({message: "Saved!", duration: 3000});
        this.$router.go(0); //reload page for update date to refresh
      }).catch((error)=>{
            this.$toast.open({message: "Error: "+error, duration: 5000, type:"error"});
            console.log(error)
        });
    },
    deleteNote() {
      NoteService.deleteNote(this.note.id).then((delNote) => {
        this.$toast.open({message: "Deleted!", duration: 3000, type: "warning"});
        console.log("Note Deleted: " + delNote)
        this.$router.push('/home');
      }).catch((error)=>{
            this.$toast.open({message: "Error: "+error.response.statusText, duration: 5000, type:"error"});
        });
    },
    getDateData() {
      if (this.note.id !== undefined) {
        return {
          "created":
              this.note.creationDate.toLocaleString('de-DE', {
                year: 'numeric',
                month: '2-digit',
                day: '2-digit',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit',
              }),
          "updated":
              this.note.updatedDate.toLocaleString('de-DE', {
                year: 'numeric',
                month: '2-digit',
                day: '2-digit',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit',
              })
        }
      } else {
        return {
          "created": "",
          "update": ""
        }
      }
    }
  }
}
</script>

<template>
  <header class="header">
    <router-link to="/home">
      <button class="back-button">
        <font-awesome-icon icon="times"/>
      </button>
    </router-link>
  </header>

  <div class="Title">
    <input
        maxlength="30"
        oninput="if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);"
        class="titleInput"
        placeholder="Note Title"
        v-model="this.note.title"
    />
  </div>

  <div class="flexContainer">
  <textarea
      class="descriptionInput"
      v-model="this.note.content"
      placeholder="Note Description"
  />
  </div>
    <!-- Temperature Input -->
    <div class="section">
      <label for="temperature">Temperature (°C)</label>
      <input
        id="temperature"
        class="temperature-input"
        v-model="temperature"
        placeholder="Enter temperature"
        type="number"
        step="0.1"
      />
    </div>

  <Map :lat="this.note.latitude" :lng="this.note.longitude"></Map>

  <div class="flexContainer">
    <button class="create-button" @click="saveNote()">Save</button>
    <button class="delete-button" @click="deleteNote()">Delete</button>
  </div>

  <div class="flexContainer">
    <div class="DateData">
      Created on: {{ this.getDateData().created }} <br>
      Updated on: {{ this.getDateData().updated }}
    </div>
  </div>
</template>

<style scoped>

.DateData {
  margin-top: 10px;
  margin-bottom: 8px;
  width: 90%;
  max-width: 350px;
  background: #b1f3b1;
  border-radius: 10px;
  padding: 6px;
  color: gray;
  font-size: 14px;
}

.dropdown {
  width: 90%;
  max-width: 350px;
  background: #b1f3b1;
  border-radius: 10px;
  padding: 6px;
}

.delete-button {
  margin-top: 15px;
  margin-left: 30px;
  padding: 5px;
  width: 100px;
  height: auto;
  background-color: #ff3131;
  border-radius: 5%;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
  cursor: pointer;
  transition: background-color 0.3s;
}

.delete-button:active {
  background-color: #c62121;
}

.create-button {
  margin-top: 15px;
  padding: 5px;
  width: 100px;
  height: auto;
  background-color: #0a7c00;
  border-radius: 5%;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
  cursor: pointer;
  transition: background-color 0.3s;
}

.create-button:active {
  background-color: #0a6300;
}

.flexContainer {
  margin-top: 12px;
  display: flex;
  justify-content: center;
}

.descriptionInput {
  margin: 10px;
  background: #b1f3b1;
  border-radius: 10px;
  padding: 5px;
  width: 90%;
  max-width: 500px;
  height: 150px;
}

.descriptionInput::placeholder {
  color: black;
}

.titleInput {
  min-width: 100px;
  color: white;
  background: transparent;
  display: inline-block;
  outline: none;
  font: inherit;
  cursor: text;
  padding: 8px;
  font-size: 20px;
}

.titleInput::placeholder {
  color: black;
}

.header {
  display: flex;
  justify-content: end;
}

.Title {
  background: #0a6300;
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.back-button {
  margin-right: 10px;
  font-size: 24px;
}
</style>