// musicbox.js
// David Bianco
// Oct. 2014

var audioId = document.getElementById("audio-id"),
    audio_playpause = document.getElementById("audio-playpause");

function audioPlay(){
    //alert("I hit play!");

    // Update the Button
    var pause = audio_playpause.innerHTML === 'Pause';
    audio_playpause.innerHTML = pause ? 'Play &nbsp;' : 'Pause';
  
    // Update the Audio
    var method = pause ? 'pause' : 'play';
    audioId[method]();
    event_data["event"] = method;
    postEvent;
   
    // Prevent Default Action
    return false;
}

function audioPause(){
    audioId["pause"]();
}
function audioVolume(){}
function audioSkip(){}

jQuery('#audio-volume').slider({
        orientation: "horizontal",
        value: 0.73,
        min: 0,
        max: 1,
        range: 'min',
        animate: true,
        step: .03,
        slide: function(e, ui) { audioId.volume = ui.value; }
});

var event_data = ({
    "user": "guest"
});
event_data["timestamp"] = "now";

var search = function search(e) {
    jQuery.ajax({
        url: "/search",
        type: "POST",
        data: {
            "query_type": "{{ search['query_type'] }}",
            "query_string": "{{ search['query_string'] }}"
        },
        datatype: "json",
        success: function(data) { success_function(data);}
    });
};

function success_function(data) {
    jQuery('#display-search-results').html(data.message)
}

var postEvent = function postEvent(e) {
    //alert("THUMBS UP!");
    jQuery.ajax({
        url: "/event",
        data: event_data,
        type: "POST"
        //data: {
            //"user": "{{ event['user'] }}", 
            //"event": "tup", 
            //"songid": "{{ event['songid'] }}",
            //"timestamp": "now",
            //"ipv4": "123.123.123.123"
        //}
    });
    event_data["event"] = "";
};


//jQuery("#audio-thumbs-up").click(event_data["event"]="tup";postEvent);
//jQuery("#audio-thumbs-dn").click(event_data["event"]="tdn";postEvent);
//jQuery("#audio-play").click(event_data["event"]="play";postEvent;audioPlay);
jQuery("#audio-playpause").click(audioPlay);
//jQuery("#audio-skip").click(event_data["event"]="skip";postEvent;audioSkip);
//jQuery("#search").click(event_data["event"]="search";postEvent);
//jQuery("#audio-pause").click(event_data["event"]="pause";postEvent;audioPause);
//jQuery("#logoff").click(event_data["event"]="logoff";postEvent);

