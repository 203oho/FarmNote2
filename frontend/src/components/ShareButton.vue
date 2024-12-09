<script>
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {library} from '@fortawesome/fontawesome-svg-core';
import {faShareNodes} from '@fortawesome/free-solid-svg-icons';
library.add(faShareNodes);

export default {
  components: {FontAwesomeIcon}
}
</script>

<template>

  <router-link to="/share">
    <button class="circle-button">
      <font-awesome-icon icon="fa-solid fa-share-nodes"/>
    </button>
  </router-link>

</template>
<style scoped>

.circle-button {
  width: 40px;
  height: 40px;
  background-color: #0a7c00;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
  cursor: pointer;
  transition: background-color 0.3s;
  position: fixed;
}

.circle-button:active {
  background-color: #0a6300;
}

.plus {
  font-size: 35px;
  color: white;
  font-weight: bold;
  line-height: 0;
}
</style>