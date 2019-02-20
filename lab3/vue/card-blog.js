Vue.component('card-blog',{
    props:['blog'],
    template :`
    <div class="col-md-4">
        <div class="card my-3">
        <img src="https://pbs.twimg.com/profile_images/875996174305472512/upM71pVR_400x400.jpg" alt="..." class="card-img-top img-fluid"> 
        <div class="card-body">
            <h5 class="card-title">
                    {{blog.title}}
                    <span class="badge badge-success ml-5">Likes: {{ blog.likes }}</span>
            </h5> 
            <p class="card-text">
            Some quick example text to build on the card title and make up
            the bulk of the card's content.<br>
            <small class="text-muted">Create By: {{ blog.createBy }}</small>
            <small class="text-muted ml-5">Create Date: {{ blog.createDate }}</small>
            </p> 
            <button class="btn btn-success" @click="$emit('add-like')">
                I like this!
            </button>
            <button class="btn btn-info" @click= "$emit('show-comment')">
            Show comment...
            </button> 
  <div class="card mt-2 text-dark" v-show="blog.isShow" v-for="comment in blog.comments">
    <div class="card-body">
        <h6 class="card-title">Comment</h6>
        <p class="card-text">
            {{ comment.text }}<br> 
            <small class="text-muted">Create By: {{ comment.createBy }}</small> 
            <small class="text-muted ml-5">Create Date:</small>
        </p>
    </div>
    </div>
        </div>
        </div></div>`
});