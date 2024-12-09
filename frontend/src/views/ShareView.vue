<script>
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome';
import {library} from '@fortawesome/fontawesome-svg-core';
import {faTimes} from '@fortawesome/free-solid-svg-icons';

library.add(faTimes);

export default {
  components: {FontAwesomeIcon},
  data() {
    return {
      token: "",
      valid: true
    }
  },
  mounted() {
    this.token = sessionStorage.getItem('token')
    this.valid = this.token !== undefined
  },
  methods: {
    copyLink() {
      navigator.clipboard.writeText("http://localhost:5174/join/" + this.token);
      this.$toast.open({message: "Copied to Clipboard", duration: 3000, type: "success"});
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

  <div class="title">FARMNOTE</div>
  <div class="flexContainer" v-if="valid">
    <label class="linkLabel" @click="copyLink()">http://localhost:5174/join/{{ token }}</label>
    <div class="qr-code" style="height: 256px; width: 256px; background-color: gray"></div>
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

.back-button {
  margin-right: 10px;
  font-size: 24px;
}
</style>