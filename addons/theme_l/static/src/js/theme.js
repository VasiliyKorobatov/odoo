var $body   = $(document.body);
var navHeight = $('.navbar').outerHeight(true) + 10;

$('#sidebar').affix({
      offset: {
        top: 245,
        bottom: navHeight
      }
});


$body.scrollspy({
	target: '#leftCol',
	offset: navHeight
});