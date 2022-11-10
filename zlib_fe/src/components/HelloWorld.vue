<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
        <el-input
          v-model="input"
          placeholder="请输入内容"
          style="width: 50%;"
          empty-text="NULL"
        ></el-input>
        <el-button @click="book_query">Find</el-button>
        <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="id"
        label="zlib ID"
        sortable
        >
      </el-table-column>
      <el-table-column
        prop="title"
        label="title"
        sortable
        >
      </el-table-column>
      <el-table-column
        prop="author"
        label="author"
        sortable
        >
      </el-table-column>
      <el-table-column
        prop="year"
        label="year"
        sortable
        >
      </el-table-column>
      <el-table-column
        prop="publisher"
        label="publisher"
        sortable
        >
      </el-table-column>
      <el-table-column
        prop="description"
        label="description"
        sortable
        :show-overflow-tooltip="true"
        >
      </el-table-column>
      <el-table-column
        prop="torrent"
        label="torrent"
        sortable
        >
      </el-table-column>
      <el-table-column
        prop="in_libgen"
        label="in_libgen"
        sortable
        >
      </el-table-column>
      <el-table-column label="操作">
      <template slot-scope="scope">
        <el-button
          size="small"
          type="primary"
          @click="handleEdit(scope.$index, scope.row)">查看全部信息</el-button>
      </template>
    </el-table-column>
    </el-table>

    <el-divider>@2022 
      <a
       href="mailto:palpitate.xus@outlook.com"
       style="color: black; text-decoration: none;">
        palpitate.xus@outlook.com
      </a> 
      All rights reserved
    </el-divider>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Z-library Books Query System',
      input: '',
      tableData: [],
    }
  },
  methods:{
    async book_query(){
      await axios.post('http://localhost:8000/api/book_query', this.input).then((res) => {
            console.log(res.data.data);
            this.$alert('共找到' + res.data.data.length + '条内容', 'Info', {
                confirmButtonText: '确定',
            });
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
