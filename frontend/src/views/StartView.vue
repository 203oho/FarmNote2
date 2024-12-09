<script setup>
// Imports
import Title from "@/components/Title.vue";
import PopUp from "@/components/PopUp.vue";
import { ref } from "vue";
import { useRouter } from "vue-router";

// State
const showPopup = ref(false);
const router = useRouter();

// Methods
const newSession = () => {
  sessionStorage.removeItem("token");
  router.push("/home");
};
</script>

<template>
  <div class="container">
    <!-- Title Component -->
    <Title />

    <!-- Buttons -->
    <div class="button-container">
      <button class="home-button" @click="newSession">
        <span>New Session</span>
      </button>

      <button class="join-button" @click="showPopup = true">
        <span>Join Session</span>
      </button>
    </div>
  </div>

  <!-- Pop-Up Component -->
  <PopUp :visible="showPopup" @close="showPopup = false" />
</template>

<style scoped>
/* Page Container */
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #f4fdf8; /* Light green background */
  padding: 20px;
  font-family: "Arial", sans-serif;
}

/* Button Container */
.button-container {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 100%;
  max-width: 400px;
  margin-top: 30px;
  text-align: center;
}

/* Base Button Styles */
button {
  font-size: 18px;
  font-weight: bold;
  padding: 12px 20px;
  border: none;
  border-radius: 50px;
  color: #fff;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
}

button:hover {
  transform: translateY(-2px);
}

button:active {
  transform: translateY(0);
}

/* Home Button */
.home-button {
  background-color: #0a7c00;
}

.home-button:hover {
  background-color: #067200;
}

.home-button:active {
  background-color: #065800;
}

/* Join Button */
.join-button {
  background-color: #027a5f;
}

.join-button:hover {
  background-color: #026a4e;
}

.join-button:active {
  background-color: #025a3d;
}


</style>

