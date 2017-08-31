function feednewsupdate(){
        update_holder = $("#update-holder");
        most_recent = update_holder.find("div:first");
        $.getJSON("/blog/feed-news/update_after/" + most_recent.attr('id') + "/",
            function(data){
                jQuery.each(data, function(){

                update_holder.prepend('<div class="card mb-4 update" id="' + this.pk + '">'
                +'<img class="card-img-top" src="/blog/media/' + this.fields.illustration +'/" alt="Card image cap">'





                +'<div class="card-body">'
                    + '<h2 class="card-title">' + this.fields.titre + '</h2>'
                    + '<p class="card-text">' + this.fields.text + '</p>'
                    + '<a href="/blog/post/details/' + this.fields.slug + '/" class="btn btn-primary">Read More &rarr;</a>'
                +'</div>'






                +'<div class="card-footer text-muted">'
                    + 'Posted on ' + this.fields.date_post + ' by <a href="/profile/' + this.fields.blog[2] + '/">' + this.fields.blog[1] + '</a>'
                +'</div>'








                +'</div>');



                });
        });
//        console.log("Hello from feednewsupdate");
}

function test(){
    alert("Hey Waff!");
//    update_holder.prepend('<div class="card mb-4 update" id="25"> Waffo </div>');
}

$(document).ready(function(){
    setInterval("feednewsupdate()", 6000);
//    alert("Waff");
//    setInterval("test()", 6000)
})













