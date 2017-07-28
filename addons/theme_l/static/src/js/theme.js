$(document).ready(function() {

            var $body   = $(document.body);
var navHeight = $('.navbar').outerHeight(true) + 10;

$('#sidebar').affix({
      offset: {
        top: 150,
        bottom: function(){
            return $("footer").outerHeight(True)-$("#wrapwrap").outerHeight(True)
        }
      }
});


$body.scrollspy({
	target: '#leftCol',
	offset: navHeight
});
});
