const baseWcaUrlPerson = "https://www.worldcubeassociation.org/persons/";
const baseWcaUrlCompetition = "https://www.worldcubeassociation.org/competitions/";

function updateRankingTable(entries) {
    $("html, body").animate({scrollTop: 0}, "fast");
    var rankingTable = $("#rankingTable");
    rankingTable.empty();
    $.each(entries, function() {
        var entry = $(this)[0];
        var row = rankingTable.append(
            "<tr>"
            + "<td>" + entry["countryrank"] + "</td>"
            + "<td>"
            + "<a href='" + baseWcaUrlPerson + entry["personid"] + "' target='_blank'>"
            + entry["personid__name"] + "</a>" + "</td>"
            + "<td>" + entry["best"] + "</td>"
            + "<td>"
            + "<a href='" + baseWcaUrlCompetition + entry["competitionid"] + "' target='_blank'>"
            + entry["competitionid__name"] + "</a>" + "</td>"
            + "</tr>"
        );
    })
}

function preparePage() {
    $.getJSON(rankingApi, function(response) {
        updateRankingTable(response["results"]);
    });
}

$(document).ready(function() {
    preparePage();
})
