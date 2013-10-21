var PLUGINS = new Array();
var PLUGINTOLOAD = ["Base64"];

$(function() {
		$.getJSON( "/list", function( data ) {
			var items = [];
			$.each( data, function( key, val ) {
				jQuery('<div/>', {
					id: data[key].name,
					text: data[key].name,
					class: 'button',
				}).appendTo('.buttonRow');
				PLUGINS.push(data[key].name);
				$("#"+data[key].name).click(function(){
					selectButton(data[key].name);
			});
			if (PLUGINS.length>0){
				$("#"+PLUGINS[0]).addClass('buttonSelected');
			}
			$("#loader").hide();
		});
	});
});

function selectButton(bname){
	$.each(PLUGINS, function(i, value){
		if(PLUGINS[i] != bname){
			$("#"+PLUGINS[i]).removeClass('buttonSelected');
		}
	});
	$("#"+bname).addClass('buttonSelected');
}


function convertPasted(text){
	$.each(PLUGINS, function(index, value){
		if ($("#"+PLUGINS[index]).hasClass('buttonSelected')){
			$("#loader").show();
			$.post( "/"+PLUGINS[index],{toConvert: encodeURI(text)}, function( data ) {
				$("#result").html(data);
				prettyPrint();
				$("#loader").hide();
			});
		}		
	});
}

function fixhtml(){
	
	var html = $("#result").html();
	html = html.replace(/\n/g, "<br/>");
	$("#result").html(html);
	
}

//placeholder
(function ($) {
    $('div[data-placeholder]').on('keydown keypress input', function() {
        if (this.textContent) {
            this.dataset.divPlaceholderContent = 'true';
        }
        else {
            delete(this.dataset.divPlaceholderContent);
        }
    });
})(jQuery);



//PASTE EVENT HANDLER
function handlepaste (elem, e) {
    var savedcontent = elem.innerHTML;
    if (e && e.clipboardData && e.clipboardData.getData) {// Webkit - get data from clipboard, put into editdiv, cleanup, then cancel event
        /*if (/text\/html/.test(e.clipboardData.types)) {
            elem.innerHTML = e.clipboardData.getData('text/html');
        }
        else if (/text\/plain/.test(e.clipboardData.types)) {*/
            elem.innerHTML = e.clipboardData.getData('text/plain');
			convertPasted(e.clipboardData.getData('text/plain'));
			//}
        /*else {
            elem.innerHTML = "";
        }*/
        waitforpastedata(elem, savedcontent);
        if (e.preventDefault) {
                e.stopPropagation();
                e.preventDefault();
        }
        return false;
    }
    else {// Everything else - empty editdiv and allow browser to paste content into it, then cleanup
        elem.innerHTML = "";
        waitforpastedata(elem, savedcontent);
        return true;
    }
}

function waitforpastedata (elem, savedcontent) {
    if (elem.childNodes && elem.childNodes.length > 0) {
        processpaste(elem, savedcontent);
    }
    else {
        that = {
            e: elem,
            s: savedcontent
        }
        that.callself = function () {
            waitforpastedata(that.e, that.s)
        }
        setTimeout(that.callself,20);
    }
}

function processpaste (elem, savedcontent) {
    pasteddata = elem.innerHTML;
    //^^Alternatively loop through dom (elem.childNodes or elem.getElementsByTagName) here
    elem.innerHTML = savedcontent;
    // Do whatever with gathered data;
}
