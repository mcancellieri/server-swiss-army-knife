var vm = require("vm");
var fs = require("fs");
var walk    = require('walk');
var pd = require('pretty-data').pd;
var htmlencoder = require('htmlencode');
var express = require('express');
var atob = require('atob');

module.exports = {
  getPlugins: function () {
    return PLUGINS;
  },
  loadPlugins : function(path, app){
  console.log("loadplugins");
  var files   = [];
  console.log(path);
  // Walker options
  var walker  = walk.walk(path, { followLinks: false });
  
  walker.on('file', function(root, stat, next) {
    // Add this file to the list of files
    console.log(stat.name);
    var plugin = {
  		name:"",
  		description:"",
  		convert:"",
  		log:console,
  		utils: {
  			prettydata:pd,
  			htmlencoder:htmlencoder,
  			atob:atob,
  		}
    }
    var path = (root + '/' + stat.name);
    if (stat.name.substr(-2)==='js'){
	    var data = fs.readFileSync(path);
	    var context={};
	    vm.runInNewContext(data, plugin, path);
    	console.log(plugin.name);
    	initPlugin(app, plugin);
    	PLUGINS.push(plugin);
    }
    next();
  });
}
  
};

var PLUGINS=new Array();

function initPlugin(app, plugin){

	app.post('/'+plugin.name, function(req, res) {
		var final = plugin.convert(decodeURI(req.body.toConvert));
		res.type('text/html');
		res.send(final);
	});
}
