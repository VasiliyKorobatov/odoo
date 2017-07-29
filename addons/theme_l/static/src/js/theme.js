$(document).ready(function() {

            var $body   = $(document.body);
var navHeight = $('.navbar').outerHeight(true) + 10;

$('#sidebar').affix({
      offset: {
        top: 150,
        bottom: function(){
            return ($("footer").outerHeight(true)+$("div#sidebar").outerHeight(true)-$(document).outerHeight(true))
//            return ($("footer").outerHeight(true)+$("div#sidebar").outerHeight(true)-$("#wrapwrap").outerHeight(true))
        }
      }
});


$body.scrollspy({
	target: '#leftCol',
	offset: 250
});
});
