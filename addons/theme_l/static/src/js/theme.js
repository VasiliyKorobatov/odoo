$(document).ready(function() {
//    var $body   = $(document.body);
//    var navHeight = function(){ return($("#oe_main_menu_navbar").length ? ($("#oe_main_menu_navbar").outerHeight(true)+$(".navbar-fixed-top").outerHeight(true)+$("header").outerHeight(true)) :($(".navbar-fixed-top").outerHeight(true)+$("header").outerHeight(true))) };
//    $('#sidebar').affix({
//          offset: {
//            top: navHeight,
//            bottom: function(){return ($("footer").outerHeight(true)+$("div#sidebar").outerHeight(true)-$(document).outerHeight(true))}
//          }
//    });
//    $body.scrollspy({
//        target: '#leftCol',
//        offset: navHeight
//    });
});
$(window).load(function() {
    var $body   = $(document.body);
    var navHeight = function(){ return($("#oe_main_menu_navbar").length ? ($("#oe_main_menu_navbar").outerHeight(true)+$(".navbar-fixed-top").outerHeight(true)+$("header").outerHeight(true)) :($(".navbar-fixed-top").outerHeight(true)+$("header").outerHeight(true))) };
    $('#sidebar').affix({
          offset: {
            top: navHeight,
            bottom: function(){return ($("footer").outerHeight(true)+$("div#sidebar").outerHeight(true)-$(document).outerHeight(true))}
          }
    });
    if($("div#wrap").length && $("#sidebar").outerHeight(true)>$("div#wrap").outerHeight(true)){
//        $("#sidebar div.oe_structure").hide();
    } else {
        $body.scrollspy({
            target: '#leftCol',
            offset: navHeight
        });
    }
});