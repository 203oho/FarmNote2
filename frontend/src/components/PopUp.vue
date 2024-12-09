<script>
import NoteService from "@/services/NoteService.js";

export default {
  data() {
    return {
      token: ""
    }
  },
  props: {
    visible: {
      type: Boolean,  // making the visible attribute accessible for the parent allows the parent to show the popup when it wants
                      // but it does not allow it to close it since the props are readonly
      required: true,
    },
  },
  emits: ['close'],
  methods: {
    close() {
      this.$emit('close');    // this causes the popup to close
    },
    joinSession() {
      if (this.token.length === 6) {
        sessionStorage.setItem('token', this.token)
        // use basic request to check token
        NoteService.getAllNotes().then((notes) => {
          // overwrite token with new token -> joins session
          this.$router.push('/home');   // return to home
        }).catch(e => {
          sessionStorage.removeItem('token') // clear token if its incorrect
          this.$toast.open({message: "Invalid Token", duration: 3000, type: "error"});
        })

      } else {
        this.$toast.open({message: "Invalid Token format!", duration: 3000, type: "error"});
      }
    }
  },
};
</script>

<template>
  <div v-if="visible" class="popup-overlay" @click.self="close">
    <!-- @click.self ="close" -> activates the close function if the user clicks outside of the popup -->
    <div class="popup-content">
      <input
          maxlength="6"
          class="tokenInput"
          placeholder="token"
          v-model="token"
      />
      <div class="button-container">
        <button @click="joinSession">Join</button>
        <button class="cancel-button" @click="close">Cancel</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.tokenInput {
  min-width: 100px;
  border: 1px solid black;
  display: inline-block;
  outline: none;
  font: inherit;
  cursor: text;
  padding: 8px;
  font-size: 20px;
}

button {
  margin-top: 20px;
  font-size: 25px;
  padding: 5px;
  width: 100px;
  height: auto;
  background-color: #0a7c00;
  border-radius: 5%;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
  cursor: pointer;
  transition: background-color 0.3s;
}

button:active {
  background-color: #0a6300;
}

.cancel-button {
  background-color: #ff3131;
}

.cancel-button:active {
  background-color: #c62121;
}


.button-container {
  display: flex;
  gap: 30px;
  align-items: center;
  flex-direction: row;
}

.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.popup-content {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
  max-width: 400px;
  width: 90%;
}
</style>
