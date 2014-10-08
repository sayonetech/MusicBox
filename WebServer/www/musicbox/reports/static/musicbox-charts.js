
jQuery(function () {
    jQuery('#report-container').highcharts({
        chart: {
            zoomType: 'x'
        },
        title: {
            text: 'MusicBox Report',
            x: -20 //center
        },
        subtitle: {
            text: '{{ data['search_type'] }}: {{ data['search_result'] }}',
            x: -20
        },
        xAxis: {
            type: 'datetime',
            title: {
                text: 'Timeline'
            }
        },
        yAxis: {
            title: {
                text: 'Count'
            },
            floor: 0,
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: ''
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        plotOptions: {
            series: {
                pointStart: Date.UTC(2010, 0, 1),
                pointInterval: 24 * 3600 * 1000 // one day
            }
        },
        series: [{
            name: 'Plays',
            type: 'column',
            data: {{ data['plays']|safe }},
        }, {
            name: 'Thumbs Up',
            data: {{ data['tup']|safe }},
        }, {
            name: 'Thumbs Down',
            data: {{ data['tdn']|safe }},
        }, {
            name: 'Skip',
            data: {{ data['skip']|safe }},
        }]
    });
});

