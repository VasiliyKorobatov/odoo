$(document).ready(function() {

            var $body   = $(document.body);
var navHeight = $('.navbar').outerHeight(true) + 10;

$('#sidebar').affix({
      offset: {
        top: 150,
        bottom: 1000
      }
});


$body.scrollspy({
	target: '#leftCol',
	offset: navHeight
});
});
