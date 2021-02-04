<template>
  <el-container>
    <el-header ><detaiHeader /></el-header>
    <el-main ><DetailContent /></el-main>
    <el-footer><Footer /></el-footer>
  </el-container>
</template>

<script>
import detaiHeader from '@/components/detaiHeader'
import DetailContent from '@/components/DetailContent'
export default {
  name: 'Details',
  components: { detaiHeader, DetailContent }
}
</script>

<style scoped>

</style>
