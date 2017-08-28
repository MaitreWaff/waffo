function feednewsupdate(){
        update_holder = $("#update-holder");
        most_recent = update_holder.find("div:first");
        $.getJSON("/blog/feed-news/update_after/" + most_recent.attr('id') + "/",
        function(data){
            jQuery.each(data, function(){
                update_holder.prepend('<div class="card mb-4 update" id="' + this.pk + '">'
                +'<img class="card-img-top" src="http://placehold.it/750x300" alt="Card image cap">'
                +'<div class="card-body">'
                    + '<h2 class="card-title">' + this.fields.titre + '</h2>'
                    + '<p class="card-text">' + this.fields.text + '</p>'
                    + '<a href="#" class="btn btn-primary">Read More &rarr;</a>'
                +'</div>'
                +'<div class="card-footer text-muted">'
                    + 'Posted on ' + this.fields.date_post + ' by <a href="/profile/' + this.fields.auteur.id + '/">' + this.fields.auteur + '</a>'
                +'</div>'
                +'</div>');
            });
        });
}

$(document).ready(function(){
    setInterval("feednewsupdate()", 6000);
//    alert("Waff");
})













