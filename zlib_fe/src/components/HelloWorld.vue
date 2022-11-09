<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
        <el-input
          v-model="input"
          placeholder="请输入内容"
          style="width: 50%;"
        ></el-input>
        <el-button @click="book_query">Find</el-button>
        <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="title"
        label="日期"
        width="180">
      </el-table-column>
      <el-table-column
        prop="title"
        label="author"
        width="180">
      </el-table-column>
      <el-table-column
        prop="author"
        label="地址">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      input: '',
      tableData: [],
    }
  },
  methods:{
    async book_query(){
      await axios.post('http://localhost:8000/api/book_query', this.input).then((res) => {
            console.log(res.data.data);
            this.tableData = res.data.data
          })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

</style>
