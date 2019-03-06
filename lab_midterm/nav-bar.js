Vue.component("nav-bar", {
  data() {
    return {
      searchText: ""
    };
  },
  methods: {
    getSearch() {
      this.$emit("get-search", this.searchText);
    }
  },
  template: `
    <nav class='navbar navbar-expand-sm bg-light navbar-light'>
    <div class='container'>
        <ul class="navbar-nav">
             <li class="nav-item">
      <a class="nav-link" href="#">Home</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">About</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Contact</a>
    </li>
        </ul>
    
        <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search"  v-model="searchText" aria-label="Search" @input="getSearch()">
    </form>
    </div>
    </nav>`
});
