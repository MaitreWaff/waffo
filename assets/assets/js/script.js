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

    $('.update').hover(function(){
        $(this).addClass('zebraHover');
//        alert(this);
    }, function(){
        $(this).removeClass('zebraHover');
//        alert('mouseout');
    });

});