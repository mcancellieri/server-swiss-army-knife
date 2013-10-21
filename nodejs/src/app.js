var express = require('express');


var app = express();

app.configure(function(){
	app.use(express.bodyParser());
});
var pluginloader = require('./pluginloader');

app.get('/list', function(req, res) {
  var p = pluginloader.getPlugins();
  res.json(p);
});


pluginloader.loadPlugins("./src/plugins",app);

app.use("/", express.static(__dirname + '/../client'));
app.use(express.bodyParser());

app.listen(process.env.PORT || 3000);
