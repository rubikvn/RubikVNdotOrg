function updateEventTable(entries) {
    $("html, body").animate({scrollTop: 0}, "fast");

    var eventsTable = $("#eventsTable");
    eventsTable.empty();
    $.each(entries, function() {
        var entry = $(this)[0];
        var row = rankingtable.append(
            "<tr>"
            + "<td>" + entry["category"] + "</td>"
            + "<td>" + entry["name"] + "</td>"
            + "<td>" + entry["start_date"] + "</td>"
            + "<td>" + entry["location"] + "</td>"
            + "</tr>"
        );
    });
}

function preparePage() {
    $.getJSON(eventBrowseApi, function(response) {
        updateEventTable(response["events"]);
    });
}
