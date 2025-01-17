<script>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faTimes } from '@fortawesome/free-solid-svg-icons';
import SessionService from "@/services/SessionService.js";
import { ref, onMounted } from "vue";  // Make sure to import onMounted

library.add(faTimes);

export default {
  components: { FontAwesomeIcon },
  setup() {
    const qrCodeUrl = ref(""); // URL with /login
    const token = ref(""); // Session token
    const isLoading = ref(true); // Loading indicator

    onMounted(async () => {
      try {
        token.value = await SessionService.getToken(); // Get token from SessionService
        qrCodeUrl.value = `${SessionService.getQRCodeUrl()}/session/qrcode?token=${token.value}`;
      } catch (error) {
        console.error("Failed to fetch session token or QR code URL:", error);
      } finally {
        isLoading.value = false;
      }
    });

    const copyLink = () => {
      navigator.clipboard.writeText(`http://localhost:5174/join/${token.value}`);
      this.$toast.open({ message: "Copied to Clipboard", duration: 3000, type: "success" });
    };

    return {
      token,
      qrCodeUrl,
      isLoading,
      copyLink,
    };
  },
};
</script>

<template>
  <header class="header">
    <router-link to="/home">
      <button class="back-button">
        <font-awesome-icon icon="times" />
      </button>
    </router-link>
  </header>

  <div class="title">FARMNOTE</div>
  <div class="flexContainer" v-if="token">
    <label class="linkLabel" @click="copyLink">http://localhost:5174/join/{{ token }}</label>
    <div class="qrcode-container">
      <img v-if="!isLoading && qrCodeUrl" :src="qrCodeUrl" alt="Session QR Code" />
      <p v-else-if="isLoading">Loading QR Code...</p>
      <p v-else>Failed to load QR Code.</p>
    </div>

  </div>
</template>

<style scoped>
.linkLabel {
  padding: 4px;
  border: 2px solid #617777;
  background-color: #eaeaea;
  border-radius: 8px;
  width: 80%;
  margin-top: 20px;
  margin-bottom: 40px;
}

.header {
  display: flex;
  justify-content: end;
  height: 56px;
}

.title {
  font-size: 38px;
  background: #0a6300;
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100%;
}

.flexContainer {
  margin-top: 12px;
  display: flex;
  align-items: center;
  flex-direction: column;
}

.qrcode-container {
  text-align: center;
  margin-top: 20px;
}

img {
  max-width: 95%;
  height: auto;
}

.back-button {
  margin-right: 10px;
  font-size: 24px;
}
</style>
