'use strict';

var mw = require('nodemw'),
    client = new mw({
        server: 'en.wiktionary.org',
        path: '/w',
        debug: false
    });
client.getArticle('olla', function(error, data) {
    console.log(data);
});
