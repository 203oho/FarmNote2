<script>
</script>

<template>
  <router-link to="/createNote">
    <button class="circle-button">
      <span class="plus">+</span>
    </button>
  </router-link>
</template>

<style scoped>
.circle-button {
  width: 60px;
  height: 60px;
  background-color: #0a7c00;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
  cursor: pointer;
  transition: background-color 0.3s;
}

.circle-button:active {
  background-color: #0a6300;
}

.plus {
  font-size: 35px;
  color: black;
  font-weight: bold;
  line-height: 0;
}
</style>