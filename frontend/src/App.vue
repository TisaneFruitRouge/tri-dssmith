<template>
  <div id="tri-container">
    <Tri />
  </div>
</template>

<script>
import { ref, reactive, onMounted } from  'vue';

import Tri from '@/components/Tri.vue'

export default {
  name: 'App',
  components: {
    Tri
  },
  setup()
  {

    
    return {}
  }
}
</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  font-size: 20px;
}

#tri-container{
  display: flex;
  justify-content: center;
}

</style>
