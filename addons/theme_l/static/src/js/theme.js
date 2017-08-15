$(document).ready(function() {
    $('#sidebar').on('show.bs.collapse', function(){
        $("#leftCol").css("display","table-row");
        $('#sidebar').css("min-height", $('#wrap').outerHeight(true)+'px');
        $("main").attr("class","col-md-9");
    });
    $('#sidebar').on('hidden.bs.collapse', function(){
        $("#leftCol").css("display","none");
        $("main").attr("class","col-md-12");
    });
    $("#city a").click(function(){
        var city = $(this).text();
        $("#user-city").text(city);
        Cookies.set('city', city, { expires: 365 });
        $("#city").modal('hide');
    });
    update_variant();
    $("select.js_variant_change").change(function(){
        update_variant();
    });
});

function update_variant(){
	Array.prototype.diff = function(a) {
		return this.filter(function(i) {return a.indexOf(i) < 0;});
	};
	var attrs = [];
	var price;
	if($(".js_variant_change").length){
        $(".js_variant_change").each(function(i,e){attrs.push(parseInt($(e).val()))});
        prc = $.parseJSON($("ul.js_add_cart_variants").attr("data-attribute_value_ids"));
        prc.forEach(function (item,i,arr) { if (attrs.diff(item[1]).length == 0){
            variant_id = arr[i][0];
            price = arr[i][3];
        }});
        if(typeof price != "undefined")
            $(".oe_currency_value").text((price.toFixed(2)).replace('.',','));
        odoo.define('website.product', function(require) {'use strict'; var Model = require('web.Model');
            var Product = new Model('product.product');
            Product.call('read', [[variant_id],['weight','volume','length','width','height','default_code']]).then(function(result){
                $("#weight-value").text(result[0]['weight']);
                $("#volume-value").text(result[0]['volume']);
                $("#lhw-value").text(result[0]['length']+'x'+result[0]['width']+'x'+result[0]['height']);
                $('#default_code').text(result[0]['default_code']);
            });
        });
        $("#xzoom-default").attr("src",'/website/image/product.product/'+variant_id+'/image');
        $("#xzoom-default").attr("xoriginal",'/website/image/product.product/'+variant_id+'/image');
    }
}
