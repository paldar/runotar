'use strict';

var _ = require('lodash'),
    BBPromise = require('bluebird'),
    mongoose = require('mongoose'),
    autoIncrement = require('mongoose-auto-increment'),
    moment = require('moment'),
    Schema = mongoose.Schema;

var WordSchema = new Schema({
    updated: Date,
    title: String,
    language: String,
    hashValue: {
        type: String,
        unique: true
    },
    content: String,
    type: [],
});

WordSchema.methods = {
};

mongoose.model('Word', WordSchema);
