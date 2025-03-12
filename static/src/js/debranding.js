odoo.define('my_debranding.title', function (require) {
    "use strict";
    var WebClient = require('web.WebClient');
    WebClient.include({
        set_title: function (title) {
            document.title = "My Company" + (title ? " - " + title : "");
        }
    });
});