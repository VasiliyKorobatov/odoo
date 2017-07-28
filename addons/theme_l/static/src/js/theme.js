$(document).ready(function() {

            var $body   = $(document.body);
var navHeight = $('.navbar').outerHeight(true) + 10;

$('#sidebar').affix({
      offset: {
        top: 60,
        bottom: 600
      }
});


$body.scrollspy({
	target: '#leftCol',
	offset: 600
});
});
