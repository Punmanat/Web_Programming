Vue.component("blog", {
  props: ["blog"],
  template: `
    <div class='card'>
        <div class='card-header bg-primary text-white text-center'>
            <p>{{blog.title}}</p>
        </div>
         <div class='card-body bg-light text-center'>
            <p class='card-text'>{{blog.text}}</p>
            <button class='btn btn-success' @click="$emit('show-comment')">show comment</button>
            <div class='card mt-3' v-show="blog.show">
                <div class='body'>
                    <p class='card-text p-4'>{{blog.comment}}</p>
                </div>
            </div>
        </div>
    </div>`
});
