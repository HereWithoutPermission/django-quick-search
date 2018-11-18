=====
Quick Search
=====

Pending

Quick start
-----------

1. Add "quick_search" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'quick_search',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('quick_search/', include('quick_search.urls')),

3. Run `python manage.py migrate` to create the quick_search models.

4. Copy the following content into your Base.html::

This goes in your scripts
    <script>
        var t = '';
        function gText(e) {
        
            t = (document.all) ? document.selection.createRange().text : document.getSelection();
        
            console.log(t);
                document.getElementById('input').value = t
            var node;
                if(t) {
                    document.getElementById('input').value = t
                    node = document.getElementById('if-part');
                    node.style.visibility = 'visible';
                    document.getElementById('if-part').style.display='block';
                }
                if(!document.getElementById('input').value){
        node = document.getElementById('if-part');
            node.style.visibility = 'hidden';
            document.getElementById('if-part').style.display='hidden';
        }
            }
        
        function searchOnclick() {
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
    </script>

And this in body::
    <body class="wide">
        <div id='if-part' style='visibility: hidden; text-align: center; bottom:0px; width:100%; height:600px; left:0px; right:0px; overflow:hidden;' class="modal" >
            <div  style='display: inline-block; width:25%' class="modal-content w3-animate-zoom">
                <span onclick="this.parentElement.parentElement.style.display='none'"
                    class="w3-button w3-large w3-display-topright">&times;</span>
                <h4 align="center">Search this selection?</h4>
                <input align="center" style='text-align:center; margin-bottom: 10px; width:100%; font-size:18px' type='text' id='input' />
                <center><button style='margin-bottom: 10px; font-size: 15px;' onclick="searchOnclick()" type="button" class="btn btn-info btn-rounded">Search</button></center>
            </div>
            <div id="id01" class="w3-modal">
                <div style='text-align: left;' class="w3-modal-content w3-animate-zoom">
                    <header class="w3-container">
                    <span onclick="document.getElementById('id01').style.display='none'"
                        class="w3-button w3-display-topright">&times;</span>
                    <h3>Search Results</h3>
                    </header>
                    <div id="demo" class="w3-container">
                    <p>Some text..</p>
                    </div>
                </div>
            </div>
        </div>
    </body>

4. GGWP
