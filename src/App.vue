<template>
  <nav class="navbar navbar-expand-lg sticky-top">
      <div class="container-fluid">
        <a class="navbar-brand">Wlog</a>
      </div>
    </nav>
  <router-view />
</template>

<script>
export default {
  data() {
    return {
      showMobileMenu: false,
    }
  },
}
</script>

<style>
#app {
  font-family: 'Open Sans', sans-serif;
  text-align: center;
  color: #2c3e50;
}

.navbar {
  box-shadow: 0 1px 5px 1px #cccccc;
  background-color: #fff;
}
</style>
