'use strict';

var _ = require('lodash');

var http = require('http');
var options = {
    host: 'en.wiktionary.org',
    path: '/wiki/olla'
};

//var request = _.cloneDeep(options).path+="olla";
http.request(options, function(res) {
    console.log(res);
}).end();
