// musicbox.js
// David Bianco
// Oct. 2014

jQuery("#thumbs-up").click( function(e) {
        alert("THUMBS UP!");
        jQuery.ajax({
            url: "/event",
            type: "POST",
            data: {"user": "{{ event['user'] }}", "event": "tup", "songid": "{{ event['songid'] }}"}
            });
        });

