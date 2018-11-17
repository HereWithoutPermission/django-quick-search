var t = '';
function gText(e) {

    t = (document.all) ? document.selection.createRange().text : document.getSelection();
    console.log("nbhd", t);

    document.getElementById('input').value = t

var node;
    if(t) {
        node = document.getElementById('if-part');
        node.style.visibility = 'visible';
        document.getElementById('if-part').style.display='block';
    }
}
function searchOnclick() {
	// document.getElementById('id01').style.display='block';
  //       var xhttp = new XMLHttpRequest();
  // xhttp.onreadystatechange = function() {
  //   if (this.readyState == 4 && this.status == 200) {
  //    document.getElementById("demo").innerHTML = this.responseText;
  //   }
  // };
  // xhttp.open("POST", "/quick_search", true);
  // xhttp.send();
  var u = document.getElementById('input').value;
  $.ajax({
       url: '/quick_search/',
       type: 'POST',
       cache: false,
       contentType: 'application/json',
       data: JSON.stringify({
         "query" : u
       }),
       success: function(data){
         	document.getElementById('id01').style.display='block';
           document.getElementById("demo").innerHTML = data;
       },
       error: function(error) {
         console.log(error);
       }
   });

}
document.onmouseup = gText;
if (!document.all) { document.captureEvents(Event.MOUSEUP);}

function load() {
    document.getElementById("quick_search").innerHTML='<object type="text/html" data="/quick_search/html" ></object>';
}
