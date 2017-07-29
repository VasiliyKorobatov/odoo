$(document).ready(function() {

var $body   = $(document.body);
var navHeight = function(){
            return $("#oe_main_menu_navbar").length ? ($("#oe_main_menu_navbar").outerHeight(true)+$(".navbar-fixed-top").outerHeight(true)+$("header").outerHeight(true)):($(".navbar-fixed-top").outerHeight(true)+$("header").outerHeight(true))
       }

}
$('#sidebar').affix({
      offset: {
        top: navHeight,
        bottom: function(){
            return ($("footer").outerHeight(true)+$("div#sidebar").outerHeight(true)-$(document).outerHeight(true))
//            return ($("footer").outerHeight(true)+$("div#sidebar").outerHeight(true)-$("#wrapwrap").outerHeight(true))
        }
      }
});


$body.scrollspy({
	target: '#leftCol',
	offset: navHeight
});
});
