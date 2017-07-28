$(document).ready(function() {

            var $body   = $(document.body);
var navHeight = $('.navbar').outerHeight(true) + 10;

$('#sidebar').affix({
      offset: {
        top: 150,
        bottom: function () {
            return $("footer").outerHeight(true)
        }
      };
      console.log(offset.bottom);
});


$body.scrollspy({
	target: '#leftCol',
	offset:  function () {
            return $("footer").outerHeight(true)
        }
});
});
