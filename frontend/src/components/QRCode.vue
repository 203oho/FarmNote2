<template>
  <div class="qrcode-container">
    <h2>Scan this QR Code to join the session</h2>
    <img v-if="qrCodeUrl" :src="qrCodeUrl" alt="QR Code" />
    <p v-else>Loading QR Code...</p>
  </div>
</template>

<script>
import SessionService from "@/services/SessionService";

export default {
  data() {
    return {
      isLoading: true,
    };
  },
  async mounted() {
    try {
      const token = await SessionService.getToken();
      this.qrCodeUrl = `${SessionService.getQRCodeUrl()}/login?token=${token}`;
    } catch (error) {
      console.error("Failed to load QR Code URL:", error);
    } finally {
      this.isLoading = false;
    }
  },
};

</script>

<style scoped>
.qrcode-container {
  text-align: center;
  margin-top: 20px;
}

img {
  max-width: 95%;
  height: auto;
}
</style>



