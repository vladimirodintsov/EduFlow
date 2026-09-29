<template>
  <main>
    <h1>EduFlow</h1>
    <p>{{ status }}</p>
  </main>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import api from '../api/client'

const status = ref('checking backend...')

onMounted(async () => {
  try {
    const { data } = await api.get('/users/ping')
    status.value = `backend: ${data.status}`
  } catch (e) {
    status.value = 'backend не отвечает'
  }
})
</script>
