function feednewsupdate(){
        //alert("Hello Waff000rld!");
        $("#update-holder").prepend('<div class="card mb-4 update" id="100">\
                <img class="card-img-top" src="http://placehold.it/750x300" alt="Card image cap">\
                <div class="card-body">\
                    <h2 class="card-title">Nothing to show.</h2>\
                    <p class="card-text">Revenez prochainement.</p>\
                    <!--<a href="#" class="btn btn-primary">Read More &rarr;</a>-->\
                </div>\
                <div class="card-footer text-muted">\
                    Posted on January 1, 2017 by <a href="#">W@luc</a>\
                </div>\
            </div>');

}

$(document).ready(function(){
    setInterval("feednewsupdate()", 6000);
//    alert("Waff");
})













