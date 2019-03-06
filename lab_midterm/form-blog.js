Vue.component("form-blog", {
  data() {
    return {
      title: "",
      text: "",
      comment: ""
    };
  },
  methods: {
    getTitle() {
      this.$emit("get-title", this.title);
    },
    getText() {
      this.$emit("get-text", this.text);
    },
    getComment() {
      this.$emit("get-comment", this.comment);
    }
  },
  template: `
    <form class='mt-5 card'>
    <div class='card-body p-4'>
        <div class='form-group row'>
            <label class='col-form-label col-2'>Title : </label>
            <input type='text' class='form-control col-10' v-model="title" @input='getTitle()'/>
        </div>
         <div class='form-group row'>
            <label class='col-form-label col-2'>Text : </label>
            <input type='text' class='form-control col-10' v-model="text" @input='getText()'/>
        </div>
         <div class='form-group row'>
            <label class='col-form-label col-2'>Comment : </label>
            <input type='text' class='form-control col-10' v-model="comment" @input='getComment()'/>
        </div>
        <button class='form-control btn btn-success' @click='$emit("create-blog")'>Create blog</button>
        </div>
    </form>
    `
});
