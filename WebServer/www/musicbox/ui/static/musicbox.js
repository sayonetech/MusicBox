// musicbox.js
// David Bianco
// Oct. 2014

var audioId = document.getElementById("audio-id"),
    audio_playpause = document.getElementById("audio-playpause"),
    eventJson = document.getElementById("event-json");

var startVol = 0.73;
audioId.volume = startVol;

function audioPlay(){
    //alert("I hit play!");

    // Update the Button
    var pause = audio_playpause.innerHTML === 'Pause';
    audio_playpause.innerHTML = pause ? 'Play' : 'Pause';
  
    // Update the Audio
    var method = pause ? 'pause' : 'play';
    audioId[method]();
    postEvent(method);

    event_data["songid"] = "TR89384997KKJF8399KF"
   
    // Prevent Default Action
    return false;
}

function audioSkip(){
    postEvent("skip");
    // choose next song, and play it
    return false;
}

function rateSongUp(){
    //alert("Inside rateSongUp");
    postEvent("tup");
    return false;
}
function rateSongDn(){
    //alert("Inside rateSongDn");
    postEvent("tdn");
    return false;
}

jQuery('#audio-volume').slider({
        orientation: "horizontal",
        value: startVol,
        min: 0,
        max: 1,
        range: 'min',
        animate: true,
        step: .03,
        slide: function(e, ui) { audioId.volume = ui.value; }
});


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
    jQuery('#display-search-results').html(data.message);
}

function postEventSuccess(data) {
    eventJson.innerHTML = data.message;
    //jQuery("#event-json").html(data.message);
}

var postEvent = function postEvent(eventData) {
    event_data["event"] = eventData;
    event_data["clicktime"] = audioId.currentTime;
    //alert("THUMBS UP!");
    jQuery.ajax({
        url: "/event",
        data: event_data,
        type: "POST",
        datatype: "json",
        success: function(data) { 
            var eventJsonStr = JSON.stringify(data, null, 2).replace(/\\"/g, '&quot;'); // indentation level = 2
            eventJson.innerHTML = eventJsonStr;
            //jQuery("#event-json").html(eventJsonStr);
            //jQuery("#event-json").html(data);
        }
    });
    //var eventJsonStr = JSON.stringify(event_data, undefined, 2); // indentation level = 2
    //eventJson.innerHTML = eventJsonStr;
    event_data["event"] = "";
};


jQuery("#audio-playpause").click(audioPlay);
jQuery("#audio-skip").click(audioSkip);
jQuery("#audio-thumbs-up").click(rateSongUp);
jQuery("#audio-thumbs-dn").click(rateSongDn);
//jQuery("#search").click(event_data["event"]="search";postEvent);
//jQuery("#logoff").click(event_data["event"]="logoff";postEvent);

