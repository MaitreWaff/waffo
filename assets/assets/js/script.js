$(document).ready(function(){
//    alert("Welcome To jQuery!");
//    alert($('#update-holder .update:even').length + ' elements!');
//    var fontSize = $('#update-holder .update:even').css('background-color', '#dddddddd');
//    alert(fontSize);
//    $('#update-holder .update:even').css('background-color', '#dddddddd');
//    $('#update-holder .update:even').css('color', '#66666666');
//    $('#update-holder .update:even').css({
//    'background-color', '#dddddddd',
//    'color': '#66666666',
//    'font-size': '11pt',
//    'line-height': '2.5em'});
//    $('#update-holder .update').click(function(){
////        $(this).hide();
////        if($('div.text-muted').is(':visible')){
////            $('div.text-muted').hide();
////        }else{
////            $('div.text-muted').show();
////        }
//        $('div.text-muted').toggle();
//
////        $('div.text-muted').hide();
////        $('div.text-muted').css('background-color', '#CCCCCC');
//    });
//
//    $('.update div.card-body p').hover(function(){
//        $(this).addClass('zebraHover');
////        alert(this);
//    }, function(){
//        $(this).removeClass('zebraHover');
////        alert('mouseout');
//    });

    $('p').animate({
        padding : '1px',
        fontSize: '10px',
        backgroundColor: '#AFEEEE',
    }, 6000);

//
//    $('#navbarResponsive li').hover(function(){
//        $(this).animate({ fontSize: '+=35px'}, 3000, 'linear');
//    },function(){
//        $(this).animate({ fontSize: '-=35px'}, 3000, 'linear');
//    });
//


    $('p.m-0').animate({ opacity: 'hide', height: 'hide'}, 10000);

    $('.update').animate({'backgroundColor': '#F8F8FF'}, 3000);



    $('.update:first').click(function(){
        $(this).hide().delay(2000).slideDown(6000).delay(3000).fadeOut().delay(4000).fadeIn();
    });


//
//    $('p:first').toggle(function() {
//        $(this).animate({'height':'+=150px'}, 2000, 'linear');
//        alert('toggled');
//    }, function() {
//        $(this).animate({'height':'-=150px'}, 2000, 'swing');
////        alert('toggled again');
//    });
//


    $('p:first').animate({height: '+=300px'}, 2000, 'easeOutBounce');
    $('p:first').animate({height: '-=300px'}, 2000, 'easeInOutExpo');
    $('p:first').animate({height: 'hide'}, 2000, 'easeOutCirc');
    $('p:first').animate({height: 'show'}, 2000, 'easeOutElastic');

    $('<div id="navigation_blob"></div>').css({
        width: 0,
        height: $('#navbarResponsive li:first a').height() + 10
    }).appendTo('#navbarResponsive');


    $('#navbarResponsive a').hover(function() {
        // Mouseover function
        $('navigation_blob').animate({
            width: $(this).width() + 10,
            left: $(this).position().left
        },{
            duration: 'slow',
            easing: 'easeOutCirc',
            queue: false
        });
    }, function() {
        // Mouseout function
        $('navigation_blob').animate({
            width: $(this).width() + 10,
            left: $(this).position().left
        },{
            duration: 'slow',
            easing: 'easeOutCirc',
            queue: false
        }).animate({
            left: $('navbarResponsive li:first a').position().left
        }, 'fast');
    });


});