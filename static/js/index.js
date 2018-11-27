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

$(document).ready(function() {
    triggerActive(requestPath);
});
