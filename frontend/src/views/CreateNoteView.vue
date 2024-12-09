<script>
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";
import { library } from "@fortawesome/fontawesome-svg-core";
import { faTimes } from "@fortawesome/free-solid-svg-icons";
import NoteService from "@/services/NoteService.js";
import LocationService from "@/services/LocationService.js";
import Map from "@/components/Map.vue";

library.add(faTimes);

export default {
  components: { FontAwesomeIcon, Map },
  data() {
    return {
      noteContent: "", // For note content
      temperature: "", // For temperature input
      location: { lat: 0, lng: 0 }, // User location
    };
  },
  mounted() {
    // Fetch user location
    LocationService.getUserLocation((location) => {
      this.location.lat = location.lat;
      this.location.lng = location.lng;
    });
  },
  methods: {
    createNote() {
      // Convert temperature to string and ensure validity
      const temperatureValue = this.temperature.toString().trim();
      if (this.noteContent.trim() && temperatureValue) {
        const note = {
          content: this.noteContent,
          latitude: this.location.lat,
          longitude: this.location.lng,
          temperature: this.temperature // Convert to float for backend
        };

        // Save note to the server
        NoteService.createNote(note)
          .then((response) => {
            this.$toast.open({
              message: "Note Created, ID: " + response.id,
              duration: 3000,
            });
            this.$router.push("/home");
          })
          .catch((error) => {
            this.$toast.open({
              message: "Error: " + error.response.statusText,
              duration: 5000,
              type: "error",
            });
          });
      } else {
        // Handle missing input
        this.$toast.open({
          message: "Content and Temperature are required",
          duration: 3000,
          type: "error",
        });
      }
    },
  },
};
</script>

<template>
  <div class="note-container">
    <!-- Header -->
    <header class="header">
      <router-link to="/home">
        <button class="back-button">
          <font-awesome-icon icon="times" />
        </button>
      </router-link>
    </header>

    <!-- Content Input -->
    <div class="section">
      <label for="content">Note Content</label>
      <textarea
        id="content"
        class="content-input"
        v-model="noteContent"
        placeholder="Enter your note content here..."
      ></textarea>
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

    <!-- Map -->
    <div class="section map-container">
      <Map :lat="location.lat" :lng="location.lng" />
    </div>

    <!-- Save Button -->
    <div class="section button-container">
      <button class="save-button" @click="createNote">Save Note</button>
    </div>
  </div>
</template>

<style scoped>
/* Container */
.note-container {
  font-family: Arial, sans-serif;
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* Header */
.header {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 10px;
}

.back-button {
  font-size: 20px;
  color: #444;
  background: none;
  border: none;
  cursor: pointer;
}

.back-button:hover {
  color: #222;
}

/* Section */
.section {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
  color: #555;
}

.content-input,
.temperature-input {
  width: 100%;
  padding: 8px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
}

.content-input {
  height: 100px;
  resize: vertical;
}

.temperature-input {
  max-width: 200px;
}

/* Map */
.map-container {
  margin: 15px 0;
  border-radius: 4px;
  overflow: hidden;
}

/* Button */
.button-container {
  text-align: center;
}

.save-button {
  background-color: #4caf50;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.save-button:hover {
  background-color: #45a049;
}
</style>
