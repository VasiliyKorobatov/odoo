$(document).ready(function() {
    $('#sidebar').on('show.bs.collapse', function(){
        $('#sidebar').css("min-height", $('#wrap').outerHeight(true)+'px');
        $("main").attr("class","col-md-9");
    });
    $('#sidebar').on('hidden.bs.collapse', function(){
        $("main").attr("class","col-md-12");
    });
    $("#yes-city").click(function(){
        $("#your-city").popover('hide');
        Cookies.set('city', $("#user-city").text());
    });
});
$(window).load(function() {
//
//    if($("div#wrap").length && $("#sidebar").outerHeight(true)>$("div#wrap").outerHeight(true)){
////        $("#sidebar div.oe_structure").hide();
//    } else {
//        var $body   = $(document.body);
//        var navHeight = function(){ return($("#oe_main_menu_navbar").length ? ($("#oe_main_menu_navbar").outerHeight(true)+$(".navbar-fixed-top").outerHeight(true)+$("header").outerHeight(true)) :($(".navbar-fixed-top").outerHeight(true)+$("header").outerHeight(true))) };
//        $('#sidebar').affix({
//              offset: {
//                top: navHeight,
//                bottom: function(){return ($("footer").outerHeight(true)+$("div#sidebar").outerHeight(true)-$(document).outerHeight(true))}
//              }
//        });
//        $body.scrollspy({
//            target: '#leftCol',
//            offset: navHeight
//        });
//    }
});