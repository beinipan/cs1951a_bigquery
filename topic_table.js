	// the table rows, typically loaded from data file using d3.csv
    var topics = [
        { topic: "Topic 1", words: "just, will, like, hillary, vote" },
        { topic: "Topic 2", words: "people, just, like, can, will" },
        { topic: "Topic 3", words: "one, just, gt, know, like" },
        { topic: "Topic 4", words: "people, sanders, gt, just, bernie" },
        { topic: "Topic 5", words: "removal, politics, please, comment, message" },
    ];

    // column definitions
    var columns = [
        { head: 'Topic', cl: 'title', html: ƒ('topic') },
        { head: 'Words', cl: 'center', html: ƒ('words') },
    ];

    // create table
    var table = d3.select('body')
        .append('table');

    // create table header
    table.append('thead').append('tr')
        .selectAll('th')
        .data(columns).enter()
        .append('th')
        .attr('class', ƒ('cl'))
        .text(ƒ('head'));

    // create table body
    table.append('tbody')
        .selectAll('tr')
        .data(movies).enter()
        .append('tr')
        .selectAll('td')
        .data(function(row, i) {
            return columns.map(function(c) {
                // compute cell values for this specific row
                var cell = {};
                d3.keys(c).forEach(function(k) {
                    cell[k] = typeof c[k] == 'function' ? c[k](row,i) : c[k];
                });
                return cell;
            });
        }).enter()
        .append('td')
        .html(ƒ('html'))
        .attr('class', ƒ('cl'));

    function length() {
        var fmt = d3.format('02d');
        return function(l) { return Math.floor(l / 60) + ':' + fmt(l % 60) + ''; };
    }