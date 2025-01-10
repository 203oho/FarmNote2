<script setup>
import NoteList from "@/components/NoteList.vue";
import CreateButton from "@/components/CreateButton.vue";
import Title from "@/components/Title.vue";
import ShareButton from "@/components/ShareButton.vue";
import NoteService from "@/services/NoteService.js";
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

const isLoading = ref(true);
const router = useRouter();

const leaveSession = () => {
  sessionStorage.removeItem("token");
  router.push("/"); // Redirect to a homepage or login page after leaving the session
};

onMounted(() => {
  if (router.currentRoute.value.path.includes("join")) {
    const token = router.currentRoute.value.params.token;

    if (token?.length === 6) {
      sessionStorage.setItem("token", token.toUpperCase());
      NoteService.getAllNotes()
        .then(() => {
          this.$toast.open({
            message: `Successfully joined with token: ${token}`,
            duration: 3000,
          });
          router.push("/home");
        })
        .catch(() => {
          sessionStorage.removeItem("token");
          this.$toast.open({
            message: "Invalid Token",
            duration: 3000,
            type: "error",
          });
        })
        .finally(() => {
          isLoading.value = false;
        });
    } else {
      sessionStorage.removeItem("token");
      this.$toast.open({
        message: "Invalid Token format!",
        duration: 3000,
        type: "error",
      });
      isLoading.value = false;
    }
  } else {
    isLoading.value = false;
  }
});
</script>

<template>
  <main>
    <!-- Loading State -->
    <div v-if="isLoading" class="loading-container">
      <div class="spinner"></div>
      <p>Loading...</p>
    </div>

    <!-- Main Content -->
    <div v-else class="content-container">
      <!-- Title -->
      <div class="header">
        <Title />
      </div>

      <!-- Buttons Section -->
      <div class="button-section">
        <div class="create-button-wrapper">
          <CreateButton />
        </div>
        <div class="share-button-wrapper">
          <ShareButton />
        </div>
      </div>

      <!-- Notes List -->
      <section class="notes-list-section">
        <NoteList :showDate="true" />
      </section>

      <!-- Leave Session Button -->
      <div class="leave-session-wrapper">
        <button class="leave-session-button" @click="leaveSession">
          Leave Session
        </button>
      </div>
    </div>
  </main>
</template>

<style scoped>
/* General Container */
main {
  font-family: "Arial", sans-serif;
  background-color: #f8f9fa;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: 20px;
  box-sizing: border-box;
}

/* Loading Section */
.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  font-size: 1.2rem;
  color: #666;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 6px solid #ccc;
  border-top-color: #4caf50;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 10px;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Content Container */
.content-container {
  width: 100%;
  max-width: 800px;
}

/* Header */
.header {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

/* Button Section */
.button-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.create-button-wrapper,
.share-button-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}

.create-button-wrapper {
  flex: 1;
  justify-content: flex-end;
}

.share-button-wrapper {
  flex: 1;
  justify-content: flex-start;
}

/* Notes List Section */
.notes-list-section {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 15px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* Leave Session Button */
.leave-session-wrapper {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.leave-session-button {
  background-color: #dc3545;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 1rem;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.leave-session-button:hover {
  background-color: #c82333;
}
</style>
