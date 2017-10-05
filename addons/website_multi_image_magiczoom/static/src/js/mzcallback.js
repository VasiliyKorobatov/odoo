$(document).ready(function() {
    var mzOptions = {};
    mzOptions = {
        onZoomReady: function() {
            console.log('onReady', arguments[0]);
        },
        onUpdate: function() {
            console.log('onUpdated', arguments[0], arguments[1], arguments[2]);
        },
        onZoomIn: function() {
            console.log('onZoomIn', arguments[0]);
        },
        onZoomOut: function() {
            console.log('onZoomOut', arguments[0]);
        },
        onExpandOpen: function() {
            console.log('onExpandOpen', arguments[0]);
        },
        onExpandClose: function() {
            console.log('onExpandClosed', arguments[0]);
        }
    };
});
