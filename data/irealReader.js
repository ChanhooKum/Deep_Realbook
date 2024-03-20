const fs = require('fs');
const iRealReader = require('ireal-reader');

fs.readFile("Jazz_1410.html", "utf8", function(err, data) {
    if (err) {
        console.error("Error reading file:", err);
        return;
    }
    try {
        const playlist = iRealReader(data);
        const jsonContent = JSON.stringify(playlist, null, 4); // Convert the playlist object to a JSON string

        fs.writeFile("playlist.json", jsonContent, "utf8", function (err) {
            if (err) {
                console.error("An error occurred while writing JSON to file:", err);
            } else {
                console.log("JSON file has been saved.");
            }
        });
    } catch (error) {
        console.error("An error occurred while parsing the playlist:", error);
    }
});
