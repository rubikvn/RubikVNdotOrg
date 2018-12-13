const navbarMap = {
    "home" : "#navHome",
    "info" : "#navInfo",
    "results" : "#navResults",
    "events" : "#navEvents",
    "tutorials" : "#navTutorials",
}

function triggerActive(pathName) {
    var appName = pathName.split("/")[1];
    if (appName === undefined) {
        console.log("Error occurred in function triggerActive()");
    } else {
        $(navbarMap[appName]).addClass("active");
    }
};

$(window).scroll(function() {
    if ($(this).scrollTop() < 50) {
        $("#goTop").css("visibility", "hidden");
    } else {
        $("#goTop").css("visibility", "visible");
    }
});

$(document).ready(function() {
    triggerActive(requestPath);
    $("#goTop").click(function() {
        $("html, body").animate({scrollTop: 0}, "fast");
    });
});
